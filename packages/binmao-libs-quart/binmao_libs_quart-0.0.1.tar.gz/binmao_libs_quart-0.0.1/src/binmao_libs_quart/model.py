#模型管理
import yaml
from ftplib import FTP
import os
import logging
from zipfile import ZipFile
import io
import math
import hashlib


BUCKET = "models"

def download_model(model_name: str, dest: str):
    """
    下载模型文件到本地
    @param 
        model_name 模型名字

        dest 本地保存目录
    """
    with __open_client__() as ftp:
        try:
            if __module_exist__(ftp, model_name):
                __module_download__(ftp, model_name, dest)
            else:
                raise Exception(f"模型文件={model_name}不存在")
        finally:
            ftp.quit() if ftp else None

def upload_model(local_dir: str, model_name: str):
    """
    上传模型文件到远程仓库
    @param 
        local_dir 本地模型目录
        
        model_name 模型名字
    """
    with __open_client__() as ftp:
        try:
            zip_path = f'{model_name}.zip'
            hash_path = f'{model_name}.md5hash.txt'
            with ZipFile(zip_path, 'w') as zip:
                files = __file_iterator__(local_dir)
                for (file, filename) in files:
                    zip.write(file, filename)
                    logging.debug(f"写入文件到压缩包 ======> {filename}")
            with open(zip_path, 'rb') as file:
                stats = {"total_bytes": 0, "hasher": hashlib.md5()}
                def print_progress(complete: bool = False):
                    state = "结束" if complete else "中"
                    print_msg = f"上传模型{model_name}{state}, bytes ======> {pybyte(stats['total_bytes'])}"
                    return print_msg
                def upload_progress(bytes):
                    stats["total_bytes"] += len(bytes)
                    stats["hasher"].update(bytes)
                    print(print_progress(), end="\r")
                ftp.storbinary("STOR " + f'{BUCKET}/{zip_path}', file, callback=upload_progress)
                print("")
                logging.debug(print_progress(True))
                # 上传md5hash文件
                md5_digest = stats['hasher'].hexdigest()
                ftp.storbinary("STOR " + f'{BUCKET}/{hash_path}', io.BytesIO(bytes(md5_digest, encoding="utf-8")))
                logging.debug(f"上传模型{model_name} md5hash: {md5_digest}")
            os.remove(zip_path)
        finally:
            ftp.quit() if ftp else None


def __get_yaml__():
    with open('binmao-libs.yaml', 'r') as cfgs:
        return yaml.load(cfgs, yaml.Loader)

def __open_client__():
    cfgs = __get_yaml__()
    host = cfgs['model']['ftp']['host']
    pwd = cfgs['model']['ftp']['pwd']
    usr = cfgs['model']['ftp']['usr']
    ftp = FTP(host, user=usr, passwd=pwd)
    logging.debug(f"建立ftp连接, host={host}, usr={usr}")
    return ftp

def __module_exist__(ftp: FTP, model_name: str):

    file_names = ftp.nlst(BUCKET)
    # logging.debug(f"file_names ======> {file_names}")
    zip_filename = f"{BUCKET}/{model_name}.zip"
    md5hash_filename = f"{BUCKET}/{model_name}.md5hash.txt"
    return (zip_filename in file_names) and (md5hash_filename in file_names)

def __module_download__(ftp: FTP, model_name, dest):

    local_dir = os.path.join(dest, model_name)
    os.makedirs(local_dir) if not os.path.exists(local_dir) else None
    
    remote_model_file_path = f"/{BUCKET}/{model_name}.zip"
    remote_md5hash_path = f"/{BUCKET}/{model_name}.md5hash.txt"
    local_model_file_path = os.path.join(dest, model_name, f"{model_name}.zip")
    local_md5hash_path = os.path.join(dest, model_name, f"{model_name}.md5hash.txt")

    #检测是否已经下载
    if os.path.exists(local_md5hash_path):
        local_md5hash_value = ""
        with open(local_md5hash_path, 'r') as file:
            local_md5hash_value = file.readline()
        remote_md5hash_value = __get_remote_md5hash__(ftp, remote_md5hash_path)
        logging.debug(f"模型{remote_model_file_path} md5hash文件存在，进行md5比较, local_hash={local_md5hash_value}, remote_hash={remote_md5hash_value}")
        if(local_md5hash_value == remote_md5hash_value):
            logging.debug(f"模型{remote_model_file_path}文件已经存在，无须下载")
    else:
        for (remote_file_path, local_file_path) in [(remote_model_file_path, local_model_file_path), (remote_md5hash_path, local_md5hash_path)]:
            with open(local_file_path, "wb") as writeable_file:
                write_stats = {"total_bytes": 0, "hasher": hashlib.md5()}
                def print_progress(complete: bool = False):
                    state = "结束" if complete else "中"
                    print_msg = f"下载文件{remote_file_path}{state}, bytes ======> {pybyte(write_stats['total_bytes'])}"
                    return print_msg
                def write_bytes(bytes):
                    writeable_file.write(bytes)
                    write_stats["total_bytes"] += len(bytes)
                    write_stats["hasher"].update(bytes)
                    print(print_progress(), end='\r')
                ftp.retrbinary('RETR ' + remote_file_path, callback=write_bytes)
                #hashcode
                md5hash = write_stats['hasher'].hexdigest()
                print("")
                logging.debug(f'{print_progress(True)}, md5hash: {md5hash}')
        #解压缩
        with ZipFile(local_model_file_path, 'r') as zip:
            for file in zip.namelist():
                zip.extract(file, os.path.join(dest, model_name))
                logging.debug(f"解压文件 ======> {file}")
            logging.debug(f"解压{remote_model_file_path}完毕")


def __file_iterator__(local_dir: str):
    """
    遍历目录下的所有文件
    """
    for root, ds, fs in os.walk(local_dir):
        for f in fs:
            fullname = os.path.join(root, f)
            yield (fullname, os.path.join(root[(root.index(local_dir) + len(local_dir)):], f))

def __get_remote_md5hash__(ftp: FTP, remote_md5hash_path: str):
    
    write_stats = {"bytes": None}
    def write_bytes(bytes):
        write_stats["bytes"] = bytes
    ftp.retrbinary('RETR ' + remote_md5hash_path, callback=write_bytes)
    return str(write_stats['bytes'], encoding="utf-8")

def pybyte(size, dot=2):
    """
    字节展示
    """
    size = float(size)
    # 位 比特 bit
    if 0 <= size < 1:
        human_size = str(round(size / 0.125, dot)) + 'b'
    # 字节 字节 Byte
    elif 1 <= size < 1024:
        human_size = str(round(size, dot)) + 'B'
    # 千字节 千字节 Kilo Byte
    elif math.pow(1024, 1) <= size < math.pow(1024, 2):
        human_size = str(round(size / math.pow(1024, 1), dot)) + 'KB'
    # 兆字节 兆 Mega Byte
    elif math.pow(1024, 2) <= size < math.pow(1024, 3):
        human_size = str(round(size / math.pow(1024, 2), dot)) + 'MB'
    # 吉字节 吉 Giga Byte
    elif math.pow(1024, 3) <= size < math.pow(1024, 4):
        human_size = str(round(size / math.pow(1024, 3), dot)) + 'GB'
    # 太字节 太 Tera Byte
    elif math.pow(1024, 4) <= size < math.pow(1024, 5):
        human_size = str(round(size / math.pow(1024, 4), dot)) + 'TB'
    # 拍字节 拍 Peta Byte
    elif math.pow(1024, 5) <= size < math.pow(1024, 6):
        human_size = str(round(size / math.pow(1024, 5), dot)) + 'PB'
    # 艾字节 艾 Exa Byte
    elif math.pow(1024, 6) <= size < math.pow(1024, 7):
        human_size = str(round(size / math.pow(1024, 6), dot)) + 'EB'
    # 泽它字节 泽 Zetta Byte
    elif math.pow(1024, 7) <= size < math.pow(1024, 8):
        human_size = str(round(size / math.pow(1024, 7), dot)) + 'ZB'
    # 尧它字节 尧 Yotta Byte
    elif math.pow(1024, 8) <= size < math.pow(1024, 9):
        human_size = str(round(size / math.pow(1024, 8), dot)) + 'YB'
    # 千亿亿亿字节 Bront Byte
    elif math.pow(1024, 9) <= size < math.pow(1024, 10):
        human_size = str(round(size / math.pow(1024, 9), dot)) + 'BB'
    # 百万亿亿亿字节 Dogga Byte
    elif math.pow(1024, 10) <= size < math.pow(1024, 11):
        human_size = str(round(size / math.pow(1024, 10), dot)) + 'NB'
    # 十亿亿亿亿字节 Dogga Byte
    elif math.pow(1024, 11) <= size < math.pow(1024, 12):
        human_size = str(round(size / math.pow(1024, 11), dot)) + 'DB'
    # 万亿亿亿亿字节 Corydon Byte
    elif math.pow(1024, 12) <= size:
        human_size = str(round(size / math.pow(1024, 12), dot)) + 'CB'
    # 负数
    else:
        raise ValueError('{}() takes number than or equal to 0, but less than 0 given.'.format(pybyte.__name__))
    return human_size