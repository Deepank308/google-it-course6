#! /usr/bin/env python3

import os
import requests
import json

IP_ADDRESS = '127.0.0.1'

supplier_descriptions_path = '~/supplier-data/descriptions/'
post_data_keys = ['name', 'weight', 'description', 'image_name']
fruits_descriptions_url = 'http://{}/fruits/'.format(IP_ADDRESS)

def process_supplier_descriptions(filename, img_name):

    post_data = {}
    with open(filename, 'r') as fb:
        lines = fb.readlines()

        for k, line in zip(post_data_keys, lines):
            post_data.update({k: line})

    post_data.update({'image_name': img_name})
    post_data['weight'] = int(post_data['weight'].strip(' lbs'))
    response = requests.post(fruits_descriptions_url, json=post_data)
    response.raise_for_status()

def process_supplier_descriptionss():
    
    for supplier_descriptions in os.listdir(supplier_descriptions_path):
        img_name = os.path.splitext(supplier_descriptions)[0] + '.jpeg'
        process_supplier_descriptions(os.path.join(supplier_descriptions_path, supplier_descriptions), img_name)

def main():
    
    print('Posting supplier_descriptions from {} folder'.format(supplier_descriptions_path))
    print('Posting supplier_descriptions to {}'.format(fruits_descriptions_url))
    
    process_supplier_descriptionss()

    print('Done... Exiting')

if __name__ == '__main__':
    main()

