import os
import feedparser
import re

BLOG_URL = os.environ.get('BLOG_URL', 'https://blog.kter.jp/feed.xml')
d = feedparser.parse(BLOG_URL)
TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)
 
for entry in d['entries']:
    print("title:", entry.title)
    print("published: ", entry.published)
    print("link: ", entry.link)
    print("content: ", remove_tags(entry.content[0].value)[:30])

