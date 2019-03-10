import os
import json
import requests
from jinja2 import Environment, FileSystemLoader
import boto3

GITHUB_URL = os.environ.get('GITHUB_URL', 'https://api.github.com/users/kter/repos')
r = requests.get(GITHUB_URL)
content = r.json()

content.sort(key=lambda x: x['updated_at'], reverse=True)


for i, entry in enumerate(content):
   content[i]['short_description'] = entry['description'][:30] if entry['description'] else 'No Description Provided'

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('_github.html.py')
output_from_parsed_template = template.render(entries=content)

with open("_github.html", "w") as fh:
    fh.write(output_from_parsed_template.encode('utf-8'))

BUCKET_NAME = os.environ.get('BUCKET_NAME', 'tomohiko.io')
s3 = boto3.resource('s3')
s3.Bucket(BUCKET_NAME).upload_file('_github.html', '_github.html')
