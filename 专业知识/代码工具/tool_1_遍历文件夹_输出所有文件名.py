# -*- coding:utf-8 -*-
import os
import sys
# dir_path = os.path.abspath(__file__)
dir_path = os.path.abspath(os.getcwd())


# 定义遍历文件夹的函数
def list_files(path):
    # 定义一个空列表用于存储所有文件名
    files_list = []
    # 获取该目录下所有文件和文件夹的名称列表
    files = os.listdir(path)
    # 遍历该列表
    for file in files:
        # 获取当前文件/文件夹的完整路径
        file_path = os.path.join(path, file)
        # 如果是文件夹，则递归调用该函数
        if os.path.isdir(file_path):
            files_list.extend(list_files(file_path))
        # 如果是文件，则将文件名添加到列表中
        else:
            files_list.append(file_path)
    # 返回所有文件名的列表
    return files_list

# 调用函数，传入需要遍历的文件夹路径
files = list_files(dir_path)
print(files)
