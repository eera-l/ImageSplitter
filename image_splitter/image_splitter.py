from matplotlib import image
import numpy as np
import os


def split_image(filepath: str, img_size: int = 64, step: int = 0,
                output_directory: str = 'extracted_images/') -> None:
    """
    Splits an image sprite into single images.
    :param filepath: Path of the sprite file. Width and height must
                     be multiples of img_size + step.
    :param img_size: Size of the images to be extracted.
    :param step: Step between images, if there is some blank space between them.
    :param output_directory: Directory to save the extracted images in.
    """
    img = image.imread(filepath)
    height, width = img.shape[:2]
    if height % (img_size + step) != 0:
        raise ValueError('The sprite height is not divisible by the specified image size plus the step.')

    if width % (img_size + step) != 0:
        raise ValueError('The sprite width is not divisible by the specified image size plus the step.')
    counter = 1

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for i in np.arange(height - (img_size + step + 1), step=img_size + step):
        for j in np.arange(width - (img_size + step + 1), step=img_size + step):
            im = img[i + (step // 2):i + img_size + (step // 2), j + (step // 2):j + img_size + (step // 2)]
            image.imsave(f'{output_directory}img_{counter:04}.png', im)
            counter += 1