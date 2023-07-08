from PIL import Image
import os

path = r'C:\Users\USERNAME\AppData\Local\Tibia\packages\Tibia\minimap' # Path to your minimap folder

floor = 7           # Which floor you want turn into a image
map_type = 'Color'  # "Minimap_Color_31744_30976_2.png" It checks if File has this string in it because there are few types of minimap I guess


def get_minmax_coords():
    coords_x = []
    coords_y = []
    for file in os.listdir(path):
        if map_type in file and f'{floor}.png' in file:
            coord_x, coord_y = file.split('_')[2], file.split('_')[3]
            coords_x.append(int(coord_x))
            coords_y.append(int(coord_y))
    return min(coords_x), min(coords_y), max(coords_x), max(coords_y)


def create_png(min_x, min_y, max_x, max_y):
    output = Image.new('RGB', (max_x - min_x + 256, max_y - min_y + 256), 'black')  # If some floors aren't calculated properly
    # (there aren't all minimap files) you can replace "(max_x - min_x + 256, max_y - min_y + 256)" with desired resolution eg. (2560, 2048)
    # output = Image.new('RGB', (2560, 2048), 'black')
    for file in os.listdir(path):
        # print(file)
        if 'Color' in file and f'_{floor}.png' in file:
            print(file, 'approved!')
            map_part = Image.open(path + '\\' + file).convert('RGB')
            coord_x, coord_y = file.split('_')[2], file.split('_')[3]
            output.paste(map_part, (int(coord_x) - min_x, int(coord_y) - min_y))
            print(f'Paste @ [{coord_x}, {coord_y}] was successful!')
    output.save(f'output/{map_type}-level-{floor}.png')
    print(f'File was saved as "{map_type}-level-{floor}.png" in output directory.')
    print(f"It's resolution is {max_x - min_x + 256}x{max_y - min_y + 256}.")


if __name__ == '__main__':
    mix_x, min_y, max_x, max_y = get_minmax_coords()
    create_png(mix_x, min_y, max_x, max_y)
