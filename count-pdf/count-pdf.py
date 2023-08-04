# 作者：小骆同学
# 日期:2023年07月18日
import os
# python3.10 以上版本导入PyPDF4模块，3.10以下导入PyPDF2模块
from PyPDF4 import PdfFileReader

# 指定pdf所在目录
pdf_dir = 'input/'

# 初始化总页数
total_pages = 0

# 遍历pdf_dir下的所有pdf文件
for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        # 打开pdf文件
        with open(pdf_dir + filename, 'rb') as pdf_file:
            # 创建PdfFileReader对象
            pdf_reader = PdfFileReader(pdf_file)
            # 获取pdf文件页数
            num_pages = pdf_reader.getNumPages()
            # 更新总页数
            total_pages += num_pages
            # 输出文件名和页数
            print(f'{filename}: {num_pages} pages')
# 输出总页数
print(f'Total pages: {total_pages}')

# 暂停（防止cmd中运行时一闪而过）
os.system('pause')