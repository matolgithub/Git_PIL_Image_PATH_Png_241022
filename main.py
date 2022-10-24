from PIL import Image
from pathlib import Path
from os import walk
from rembg import remove


def change_jpg_png():
    file_path = f"{Path.cwd()}/input_imgs"
    list_all_files = [item for item in [x[2] for x in walk(file_path)][0]]
    list_jpgs_files = [item for item in list_all_files if item[-3:] == "jpg" or item[-3:] == "png"]

    list_png_files = [f"{item[:-4]}.png" for item in list_jpgs_files if item[-3:] == "jpg"]

    for item in list_jpgs_files:
        write_file = Image.open(f"{Path.cwd()}/input_imgs/{item}")
        write_file.save(f"{Path.cwd()}/png_imgs/{item[:-4]}.png")

    return list_jpgs_files, list_png_files


def png_without_bg():
    list_files = change_jpg_png()[0]
    step = 1
    for item in list_files:
        jpg_file = Image.open(f"{Path.cwd()}/input_imgs/{item}")
        print(f"Start process: step {step} from {len(list_files)},")
        new_file = remove(jpg_file)
        new_file.save(f"{Path.cwd()}/new_imgs/{item[:-3]}png")
        print(f"End step {step} from {len(list_files)}.")
        step += 1


def add_some_png():
    background = Image.open("input_imgs/sea_.jpg")
    foreground = Image.open("new_imgs/smartlamps.png")
    background.paste(foreground, (400, 400), foreground)
    # background.show()
    # foreground.show()
    background.save("new_imgs/add_photos.png")
    photo_1 = Image.open("new_imgs/add_photos.png")
    foreground_2 = Image.open("new_imgs/pic_1 .png")
    photo_1.paste(foreground_2, (0, 600), foreground_2)
    # photo_1.show()
    photo_1.save("new_imgs/he-he-he.png")

def main():
    # png_without_bg()
    add_some_png()


if __name__ == "__main__":
    main()
