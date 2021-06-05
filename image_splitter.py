import argparse
from matplotlib import image
import numpy as np
import os


def read_image(filename):
    img = image.imread(filename)
    return img


def split_chunks(img, img_size, step, output_directory):
    height, width = img.shape[:2]
    assert height % (img_size + step) == 0
    assert width % (img_size + step) == 0
    counter = 1

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for i in np.arange(height - (img_size + step + 1), step=img_size + step):
        for j in np.arange(width - (img_size + step + 1), step=img_size + step):
            im = img[i + (step // 2):i + img_size + (step // 2), j + (step // 2):j + img_size + (step // 2)]
            image.imsave(f'{output_directory}img_{counter:04}.png', im)
            counter += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filepath', help='Path of the file of the main image. Width and height must'
                                           'be multiples of the step.',
                        required=True)
    parser.add_argument('--output_directory', help='Directory to save the extracted images in. '
                                                   'Default: extracted_images/',
                        default='extracted_images/')
    parser.add_argument('--img_size', help='Size of the images to be extracted.',
                        default=64, type=int, required=True)
    parser.add_argument('--step', help='Step in between images, if there is some blank space between them.',
                        default=0, type=int)

    args = parser.parse_args()
    img = read_image(args.filepath)
    split_chunks(img, args.img_size, args.step, args.output_directory)