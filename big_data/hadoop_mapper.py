
#!/usr/bin/python3
import re
from collections import Counter
import sys
from xml.etree import ElementTree as xml

def get_data():
    """
    Read and parse XML
    """
    xml_data = open('posts.xml', 'r').read()  
    paser_root = ET.XML(xml_data)  
    return paser_root

def chunkify(seq, size):
    """
    Split seq list into N chunks
    """
    return (seq[i::size] for i in range(size))

def get_post_accept(post):
    """
    Extract Accepted Answer Id and type of post
    clean characters type of post
    """
    post_accept = post.get('AcceptedAnswerId')
    post_tags = post.get('Tags')
    if post_accept != None:
        return re.findall(r'<([^>]+)>' , post_tags)

def mapper(chunker_list):
    """
    Obteined pairs key
    and value [type_post,type_post_count]
    convert to list unique value pair
    return counter pair of list mapped
    """
    mapper_data = (map(get_post_accept, chunker_list))
    mapper_data = ([x for x in mapper_data if x is not None])
    mapper_data = [item for subl in mapper_data for item in subl]
    mapper_data= Counter(mapper_data)
    # print stdout mapper data pairs key, values 
    for key, value in mapper_data.items():
        print('%s\t%s' % (key, value))


if '__main__' == __name__:
    """
    Get data of xml file
    divide list in 100 chunks
    Get Top 10 most 
    accepted post type
    """
    xml_data = get_data()
    chunker_list = chunkify(xml_data, 100)
    mapped =list(map(mapper, chunker_list))