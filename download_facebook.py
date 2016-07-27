from urllib import urlopen
from json import loads
from sys import argv
import dateutil.parser as dateparser
import logging

# plugin your username and access_token (Token can be get and
# modified in the Explorer's Get Access Token button):
# https://graph.facebook.com/USER_NAME/photos?type=uploaded&fields=source&access_token=ACCESS_TOKEN_HERE
FACEBOOK_USER_ID = "100012912911204"
FACEBOOK_ACCESS_TOKEN = "CAACEdEose0cBAG3VUz3IbZCk79kZAs5uCkeXW6ZCVZASBuRXGAA3t6CAQpcUAxKjGFYZAmTKiu6Ja5rrAb7ZAYnglEgrBgqK1CQZC6uXVpnxYIRWbMeiY8w8FWpNL4qaqZCEF1tzWXqmacL7rXiUQZCOaCdh8AU9L8Bx4rUFkwgicwAeubZAQC8ABOXPLihRvJXNkaXZBjq1ZAeZB7hXsmbEZCYkji"

def get_logger(label='lvm_cli', level='INFO'):
    """
    Return a generic logger.
    """
    format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=format)
    logger = logging.getLogger(label)
    logger.setLevel(getattr(logging, level))
    return logger

def urlrequest(url):
    """
    Make a url request
    """
    req = urlopen(url)
    data = req.read()
    return data

def get_json(url):
    """
    Make a url request and return as a JSON object
    """
    res = urlrequest(url)
    data = loads(res)
    return data

def get_next(data):
    """
    Get next element from facebook JSON response,
    or return None if no next present.
    """
    try:
        return data['paging']['next']
    except KeyError:
        return None

def get_images(data):
    """
    Get all images from facebook JSON response,
    or return None if no data present.
    """
    try:
        return data['data']
    except KeyError:
        return []

def get_all_images(url):
    """
    Get all images using recursion.
    """
    data = get_json(url)
    images = get_images(data)
    next = get_next(data)

    if not next:
        return images
    else:
        return images + get_all_images(next)

def get_url(userid, access_token):
    """
    Generates a useable facebook graph API url
    """
    root = 'https://graph.facebook.com/'
    endpoint = '%s/photos?type=uploaded&fields=source,updated_time&access_token=%s' % \
                (userid, access_token)
    return '%s%s' % (root, endpoint)

def download_file(url, filename):
    """
    Write image to a file.
    """
    data = urlrequest(url)
    path = 'C:/photos/%s' % filename
    f = open(path, 'w')
    f.write(data)
    f.close()

def create_time_stamp(timestring):
    """
    Creates a pretty string from time
    """
    date = dateparser.parse(timestring)
    return date.strftime('%Y-%m-%d-%H-%M-%S')

def download(userid, access_token):
    """
    Download all images to current directory.
    """
    logger = get_logger()
    url = get_url(userid, access_token)
    logger.info('Requesting image direct link, please wait..')
    images = get_all_images(url)

    for image in images:
        logger.info('Downloading %s' % image['source'])
        filename = '%s.jpg' % create_time_stamp(image['created_time'])
        download_file(image['source'], filename)

if __name__ == '__main__':
    download(FACEBOOK_USER_ID, FACEBOOK_ACCESS_TOKEN)
