# 作者：小骆同学
# 日期:2023年07月18日
import os
# python3.10 以上版本导入PyPDF4模块，3.10以下导入PyPDF2模块
from PyPDF4 import PdfFileReader

# 指定pdf所在目录
pdf_dir = 'input/'

# 初始化总价格
total_price = 0

print('说明：如果满减为15-10，那么满减门槛为15，满减价格为10')

# 输入单价
price = input('请输入打印一页的单价(按下回车默认为0.05)：') or 0.05
price = float(price)

# 输入满减门槛
threshold = input('请输入满减门槛(按下回车默认为15)：') or 15
threshold = int(threshold)

# 输入满减价格
discount = input('请输入满减价格(按下回车默认为10)：') or 10
discount = int(discount)

# 输入最低消费
min_price = input('请输入最低消费(按下回车默认为10)：') or 10
min_price = int(min_price)

# 是否自定义页数
is_custom = input('是否自定义页数？(自定义页数直接输入数字，否则按下回车)：') or '0'
if is_custom == '0':
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
else:
    # 转换为int类型
    total_pages = int(is_custom)

# 计算总价格
if total_pages >= threshold:
    total_price = total_pages * price - discount
else:
    total_price = total_pages * price

if total_price < min_price:
    total_price = min_price

# 输出总页数
print(f'总页数为：{total_pages}')

# 输出总价格,保留两位小数
print(f'总价格为：{total_price:.2f}')

# 暂停（防止cmd中运行时一闪而过）
# os.system('pause')
input('按回车键退出')
