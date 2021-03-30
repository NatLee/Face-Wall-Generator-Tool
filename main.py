"""
Face Wall!
"""
from pathlib import Path
import random

from loguru import logger

import cv2
import numpy as np
import fire


FACE_FOLDER = './faces'

def get_faces(folder_path:str, extensions=['.png', '.jpg'], size=(72, 72)) -> list:
    return [cv2.resize(cv2.imread(img_path.absolute().as_posix()), size) for img_path in Path(folder_path).glob('*') if img_path.suffix in extensions]

def generate_face_wall(x:int, y:int, save_path='./wall.jpg'):
    """
    Generate wall!
    Parameters
    -------------
    x : int
    y : int
    save_path : str
        Location for saving output image.
    """
    imgs = get_faces(FACE_FOLDER)

    wall = np.concatenate(
        [
            np.concatenate(
                [random.choice(imgs) for _ in range(x)], axis=1
            ) for _ in range(y)
        ]
    )
    cv2.imwrite(save_path, wall)
    return

if __name__ == '__main__':
    fire.Fire(generate_face_wall)