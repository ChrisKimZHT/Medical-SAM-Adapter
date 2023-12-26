import os
from PIL import Image
from tqdm import tqdm

def split_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for image_file in tqdm(image_files):
        input_path = os.path.join(input_dir, image_file)
        original_image = Image.open(input_path)
        
        width, height = original_image.size

        split_point = width // 2

        left_image = original_image.crop((0, 0, split_point, height))
        right_image = original_image.crop((split_point, 0, width, height))

        left_output_path = os.path.join(output_dir, f"left_{image_file}")
        right_output_path = os.path.join(output_dir, f"right_{image_file}")

        right_image = right_image.transpose(Image.FLIP_LEFT_RIGHT)

        left_image.save(left_output_path)
        right_image.save(right_output_path)

def split_images_2(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for image_file in tqdm(image_files):
        input_path = os.path.join(input_dir, image_file)
        original_image = Image.open(input_path)
        
        width, height = original_image.size

        split_point = width // 2

        left_image = original_image.crop((30, 0, split_point + 30, height))
        right_image = original_image.crop((split_point - 30, 0, width, height))

        left_output_path = os.path.join(output_dir, f"left_{image_file}")
        right_output_path = os.path.join(output_dir, f"right_{image_file}")

        right_image = right_image.transpose(Image.FLIP_LEFT_RIGHT)

        left_image.save(left_output_path)
        right_image.save(right_output_path)


input_directory = "./data/predict"
output_directory = input_directory + "_split"

# split_images(input_directory, output_directory)
split_images_2(input_directory, output_directory)