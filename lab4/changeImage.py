#!/usr/bin/env python3

from PIL import Image
import os

save_path = '~/supplier-data/images/'

def process_one_image(img_path, size=(128, 128), cw_rotate_angle=0):
    try:
        img = Image.open(img_path)
     
        img_name = os.path.basename(img_path)
        img_name = os.path.splitext(img_name)[0]

        img = img.convert('RGB')
        rsz_img = img.resize(size)
        new_img = rsz_img.rotate(cw_rotate_angle)
        
        new_img.save(save_path + '{}.jpeg'.format(img_name))
    except:
        print('Error processing: {}'.format(img_path))
        return
    

def process_images(folder='./', size=(128, 128), cw_rotate_angle=0):
    folder_path = os.path.abspath(folder)

    for img_file in os.listdir(folder):
        process_one_image(os.path.join(folder_path, img_file), size, cw_rotate_angle)


def main():
    print('Start processing...')

    size = (600, 400)
    cw_rotate_angle = 0
    
    os.makedirs(save_path, exist_ok=True)

    folder_path = '~/supplier-data/images/'
    process_images(folder_path, size, cw_rotate_angle)

    print('Done processing... Exiting')


if __name__ == '__main__':
    main()


