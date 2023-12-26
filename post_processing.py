import cv2
import os
import numpy as np
from tqdm import tqdm

def filter_small_connected_components(binary_image, threshold):
    nb_components, output, stats, _ = cv2.connectedComponentsWithStats(binary_image, connectivity=8)
    sizes = stats[:, -1]

    filtered_image = np.zeros(output.shape)
    for i in range(1, nb_components):
        if sizes[i] >= threshold:
            filtered_image[output == i] = 255

    return filtered_image



def process_images_in_directory(input_dir, output_dir, threshold):
    os.makedirs(output_dir, exist_ok=True)

    for filename in tqdm(os.listdir(input_dir)):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_dir, filename)
            binary_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            filtered_image = filter_small_connected_components(binary_image, threshold)

            output_path = os.path.join(output_dir, f"filtered_{filename}")
            cv2.imwrite(output_path, filtered_image)

if __name__ == "__main__":
    input_directory = './logs/mydataset_2023_12_26_09_41_08/Samples_merged_binary'
    output_directory = input_directory + '_filtered'
    threshold = 0  # 根据需要调整阈值

    process_images_in_directory(input_directory, output_directory, threshold)
