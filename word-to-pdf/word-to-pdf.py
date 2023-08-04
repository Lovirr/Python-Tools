import office # 导入python-office
import os
import win32com.client as win32 # 导入win32com

# path填写你存放word文件的位置
path = 'input/'
office.word.docx2pdf(path=path)
# 关闭word文档

