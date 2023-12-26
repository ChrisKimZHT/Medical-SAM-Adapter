from PIL import Image, ImageChops
import os
from tqdm import tqdm

def merge_images(input_dir, output_dir):
    files = os.listdir(input_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for file in tqdm(files):
        if file.startswith("predictleft_") and file.endswith(".jpg"):
            left_image_path = os.path.join(input_dir, file)
            right_image_id = file.split("_")[1].split(".")[0]
            right_image_path = os.path.join(input_dir, f"predictright_{right_image_id}.jpg")
            
            if os.path.exists(right_image_path):
                left_image = Image.open(left_image_path)
                right_image = Image.open(right_image_path)

                right_image = right_image.transpose(Image.FLIP_LEFT_RIGHT)
                
                merged_image = Image.new("RGB", (640, 320))
                merged_image.paste(left_image, (0, 0))
                merged_image.paste(right_image, (320, 0))
                
                output_path = os.path.join(output_dir, f"{right_image_id}.jpg")
                merged_image.save(output_path)
            else:
                print(f"右侧图片不存在: {right_image_path}")


def merge_images_2(input_dir, output_dir):
    files = os.listdir(input_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for file in tqdm(files):
        if file.startswith("predictleft_") and file.endswith(".jpg"):
            left_image_path = os.path.join(input_dir, file)
            right_image_id = file.split("_")[1].split(".")[0]
            right_image_path = os.path.join(input_dir, f"predictright_{right_image_id}.jpg")
            
            if os.path.exists(right_image_path):
                left_image = Image.open(left_image_path)
                right_image = Image.open(right_image_path)

                right_image = right_image.transpose(Image.FLIP_LEFT_RIGHT)
                
                left_temp = Image.new("1", (640, 320))
                right_temp = Image.new("1", (640, 320))
 
                left_temp.paste(left_image, (30, 0))
                right_temp.paste(right_image, (290, 0))

                merged_image = Image.eval(ImageChops.logical_or(left_temp, right_temp), lambda px: 255 if px > 0 else 0)
                
                output_path = os.path.join(output_dir, f"{right_image_id}.jpg")
                merged_image.save(output_path)
            else:
                print(f"右侧图片不存在: {right_image_path}")

input_directory = "./logs/mydataset_2023_12_26_09_41_08/Samples"
output_directory = input_directory + "_merged"

# merge_images(input_directory, output_directory)
merge_images_2(input_directory, output_directory)
