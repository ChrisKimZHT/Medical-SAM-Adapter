from PIL import Image
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

input_directory = "./logs/mydataset_2023_12_26_09_14_16/Samples"
output_directory = "./logs/mydataset_2023_12_26_09_14_16/Samples_merged"

merge_images(input_directory, output_directory)
