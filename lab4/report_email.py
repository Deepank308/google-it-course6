#! /usr/bin/env python3

import os
import requests
import json
from datetime import datetime
import reports
import emails


supplier_descriptions_path = '~/supplier-data/descriptions/'

def process_supplier_descriptions(filename, paragraph):

    with open(filename, 'r') as fb:
        name = fb.readline()
        weight = fb.readline()

        info = '<br/>name: {}<br/>weight: {}<br/>'.format(name, weight)

    paragraph += info
    return paragraph
    

def process_supplier_descriptions(paragraph=''):
    
    for supplier_descriptions in os.listdir(supplier_descriptions_path):
        paragrpah = process_supplier_descriptions(os.path.join(supplier_descriptions_path, supplier_descriptions), paragraph)

    return paragraph

def main():
    
    print('Posting supplier_descriptions from {} folder'.format(supplier_descriptions_path))
    print('Posting supplier_descriptions to {}'.format(fruits_descriptions_url))
    
    title = 'Processed Update on {}'.format(datetime.today().strftime('%b %d, %Y'))
    paragraph = process_supplier_descriptions()
    attachment = '/tmp/processed.pdf'

    reports.generate_report(attachment, title, paragraph)

    sender = 'automation@example.com'
    to = '{}@example.com'.format(os.environ.get('USER'))
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    msg = emails.generate_email(sender, to, subject, body, attachment)
    emails.send_email(msg)
    print('Done... Exiting')

if __name__ == '__main__':
    main()

