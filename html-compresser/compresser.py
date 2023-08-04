# 压缩HTML，CSS和JavaScript代码
# import os
#
# import htmlmin
# from csscompressor import compress as compress_css
# from jsmin import jsmin
#
#
# def compress_html_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         html = f.read()
#     compressed_html = htmlmin.minify(html, remove_comments=True, remove_all_empty_space=True,
#                                      reduce_empty_attributes=True, remove_optional_attribute_quotes=False)
#     compressed_html = compressed_html.replace('\n', '')  # 移除换行符
#     compressed_html = compressed_html.replace('\t', '')  # 移除制表符
#     compressed_html = compressed_html.replace('\r', '')  # 移除回车符
#     compressed_css = compress_css(compressed_html)  # 压缩 CSS 代码
#     print(f'Compressed CSS in {file_path}')
#     compressed_js = jsmin(compressed_html, quote_chars="'\"`")  # 压缩 JavaScript 代码
#     print(f'Compressed JavaScript in {file_path}')
#     # 将压缩后的 CSS 和 JavaScript 代码插入到 HTML 文件中
#     compressed_html = compressed_html.replace('<style>' + compressed_css + '</style>',
#                                               '<style>' + compressed_css + '</style><script>' + compressed_js + '</script>')
#     compressed_html = compressed_html.strip()  # 移除首尾空格
#     with open(file_path, 'w', encoding='utf-8') as f:
#         f.write(compressed_html)
#
# def compress_html_files_in_folder(folder_path):
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.endswith('.html'):
#                 file_path = os.path.join(root, file)
#                 compress_html_file(file_path)
#
# if __name__ == '__main__':
#     folder_path = 'input'
#     compress_html_files_in_folder(folder_path)
#     print('HTML files compressed successfully')

# 只压缩HTML文件
import os
import htmlmin

def compress_html_files(input_dir, options):
    # 遍历目录及其子目录中的所有文件和文件夹
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.html'):
                # 读取HTML文件内容
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # 压缩HTML文件内容
                compressed_content = htmlmin.minify(content, **options)

                # 将压缩后的内容写回到源文件中
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(compressed_content)
                    print(f'Compressed {file_path}')
# 调用函数
input_dir = './input'
options = {
    'remove_comments': True,
    'remove_empty_space': True,
    'remove_all_empty_space': True,
    'reduce_boolean_attributes': True,
    'remove_optional_attribute_quotes': True,
}
compress_html_files(input_dir, options)