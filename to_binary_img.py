import os
from PIL import Image

def convert_to_binary(image_path, threshold=128):
    img = Image.open(image_path)
    gray_img = img.convert('L')
    binary_img = gray_img.point(lambda pixel: 0 if pixel < threshold else 255, '1')
    return binary_img

def batch_convert_to_binary(input_directory, output_directory, threshold=128):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(".jpg"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename.replace("predict", "").replace(".jpg", ".png"))
            binary_image = convert_to_binary(input_path, threshold)
            binary_image.save(output_path)

if __name__ == "__main__":
    input_dir = "./logs/mydataset_2023_12_26_09_41_08/Samples_merged"
    output_dir = input_dir + "_binary"
    threshold_value = 128
    batch_convert_to_binary(input_dir, output_dir, threshold_value)
