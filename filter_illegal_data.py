from PIL import Image
import os
from tqdm import tqdm


def is_binary_image_all_zeros(image_path):
    try:
        with Image.open(image_path) as img:
            img = img.convert('L')
            pixels = list(img.getdata())
            return all(pixel == 0 for pixel in pixels)
    except Exception as e:
        print(f"发生错误: {e}")
        return False
    

def get_illegal_data(input_dir):
    illegal_data = []
    for filename in tqdm(os.listdir(input_dir)):
        if filename.endswith(".png"):
            image_path = os.path.join(input_dir, filename)
            if is_binary_image_all_zeros(image_path):
                illegal_data.append(filename)
    return illegal_data


def perform_delete(iliiegal_data):
    for filename in iliiegal_data:
        image_path = os.path.join("./data/train/image_splited", filename)
        mask_path = os.path.join("./data/train/mask_splited", filename)
        os.remove(image_path)
        os.remove(mask_path)

if __name__ == "__main__":
    input_dir = "./data/train/mask_splited"
    illegal_data = get_illegal_data(input_dir)
    print(f"共有{len(illegal_data)}个非法数据")
    print(illegal_data)
    input("确认删除？")
    perform_delete(illegal_data)
    print("非法数据已删除")


