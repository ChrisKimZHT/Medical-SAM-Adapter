import os
from PIL import Image
from tqdm import tqdm

def split_images(input_dir, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 获取输入目录中所有图片文件的列表
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # 遍历每张图片并切分
    for image_file in tqdm(image_files):
        input_path = os.path.join(input_dir, image_file)
        original_image = Image.open(input_path)
        
        # 获取图片尺寸
        width, height = original_image.size

        # 计算切分的位置
        split_point = width // 2

        # 切分图片
        left_image = original_image.crop((0, 0, split_point, height))
        right_image = original_image.crop((split_point, 0, width, height))

        # 保存切分后的图片
        left_output_path = os.path.join(output_dir, f"left_{image_file}")
        right_output_path = os.path.join(output_dir, f"right_{image_file}")

        # 翻转右侧图像
        right_image = right_image.transpose(Image.FLIP_LEFT_RIGHT)

        left_image.save(left_output_path)
        right_image.save(right_output_path)


# 指定输入目录和输出目录
input_directory = "./data/test/image"
output_directory = "./data/test/image_splited"

# 调用函数进行切分
split_images(input_directory, output_directory)
