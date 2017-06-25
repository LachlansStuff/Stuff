import random
import urllib.request

image_number = 10

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)

for i in range(image_number):
    download_web_image('https://ih0.redbubble.net/image.304240988.5655/flat,800x800,075,f.u1.jpg')
