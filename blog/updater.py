import os
import requests
import xml.etree.ElementTree as ET

BLOG_URL = os.environ.get('BLOG_URL', 'https://blog.kter.jp/feed.xml')
xml = requests.get(BLOG_URL)
xml_root = ET.fromstring(xml.content)

#for xml_child in xml_root:
#    print(xml_child.tag, xml_child.attrib)

for xml_child in xml_root.iter('{http://www.w3.org/2005/Atom}entry'):
    print("tag", xml_child.tag)
    print("attrib", xml_child.attrib)

