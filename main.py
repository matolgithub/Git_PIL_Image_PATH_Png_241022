from PIL import Image
from pathlib import Path
from os import walk
# from rembg import remove


def change_jpg_png():
    file_path = f"{Path.cwd()}/input_imgs"
    list_all_files = [item for item in [x[2] for x in walk(file_path)][0]]
    list_jpgs_files = [item for item in list_all_files if item[-3:] == "jpg" or item[-3:] == "png"]
    print(list_jpgs_files)

def png_without_bg():
    change_jpg_png()


def main():
    png_without_bg()


if __name__ == "__main__":
    main()
