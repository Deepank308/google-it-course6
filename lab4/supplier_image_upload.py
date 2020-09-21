#! /usr/bin/env python3

import os
import requests
import json

IP_ADDRESS = '127.0.0.1'

supplier_image_path = '~/supplier-data/images/'
fruit_catalog_url = 'http://{}/upload/'.format(IP_ADDRESS)

def process_supplier_image(filename):

    if filename.endswith('.jpeg') == False:
        return

    with open(filename, 'rb') as fb:
        response = requests.post(fruit_catalog_url, files={'file': fb})
        response.raise_for_status()

def process_supplier_images():
    
    for supplier_image in os.listdir(supplier_image_path):
        process_supplier_image(os.path.join(supplier_image_path, supplier_image))

def main():
    
    print('Posting supplier_images from {} folder'.format(supplier_image_path))
    print('Posting supplier_images to {}'.format(fruit_catalog_url))
    
    process_supplier_images()

    print('Done... Exiting')

if __name__ == '__main__':
    main()

