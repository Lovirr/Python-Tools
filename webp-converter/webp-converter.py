# 作者：小骆同学
# 日期:2023年07月07日
from PIL import Image, ImageCms
import os
import glob

# 记录已转换的文件数量
converted_count = 0

# 定义输入和输出文件夹路径
input_folder = 'input'
output_folder = 'output'

# 获取文件夹中所有JPEG
image_list = glob.glob(os.path.join(input_folder, '*.jpg'))

# 获取文件夹中所有PNG
# image_list = glob.glob(os.path.join(input_folder, '*.jpg')+os.path.join(input_folder, '*.png'))

# 获取文件夹中所有PNG和JPEG
# image_list = glob.glob(os.path.join(input_folder, '*.jpg'))+glob.glob(os.path.join(input_folder, '*.png'))

# 构造sRGB颜色转换器
srgb_profile = ImageCms.createProfile('sRGB')
srgb_transform = ImageCms.buildTransformFromOpenProfiles(srgb_profile, srgb_profile, 'RGB', 'RGB')

# 遍历所有图像文件并进行转换
for image_path in image_list:
    # 打开图像并转换为sRGB格式
    with Image.open(image_path) as im:
        srgb_im = ImageCms.applyTransform(im, srgb_transform)

        # 构造输出文件路径
        output_path = os.path.join(output_folder, os.path.basename(image_path).split('.')[0] + '.webp')

        # 保存转换后的图像文件
        srgb_im.save(output_path)

        # 更新已转换的文件数量并打印进度信息
        converted_count += 1
        print(f'Converted {converted_count} of {len(image_list)} files')
print('success!')