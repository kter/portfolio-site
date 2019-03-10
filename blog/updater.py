import os
import feedparser
import re
from jinja2 import Environment, FileSystemLoader
import boto3

BLOG_URL = os.environ.get('BLOG_URL', 'https://blog.kter.jp/feed.xml')
DISPLAY_LIMIT = 5

d = feedparser.parse(BLOG_URL)
TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

del d['entries'][DISPLAY_LIMIT:]
 
for i, entry in enumerate(d['entries']):
    d['entries'][i]['remove_tags_content'] = remove_tags(entry.content[0].value)[:30]

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('_blog.html.py')
output_from_parsed_template = template.render(entries=d['entries'])

with open("_blog.html", "w") as fh:
    fh.write(output_from_parsed_template)

BUCKET_NAME = os.environ.get('BUCKET_NAME', 'kter.jp')
s3 = boto3.resource('s3')
s3.Bucket(BUCKET_NAME).upload_file('_blog.html', '_blog.html')