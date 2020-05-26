from bs4 import BeautifulSoup
import urllib.request
import re

url = input("Enter the URL : \n").strip()
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser', from_encoding=response.info().get_param('charset'), )
links = []
text = []
images = []

#to extract the html content of the webpage
html = soup.prettify()
#
# #strores the html content of the webpage into html.txt file
# with open("Extracted_html.txt", 'w') as file:
#
#     for line in html:
#         try:
#             file.write(line)
#         except:
#             pass

#Extracting all the hyperlinks in the webpage
for link in soup.find_all('a', href=True):
    if link['href'].startswith("http"):
        links.append(link["href"])

# Extracting text only present in 'p' element in the webpage
p = re.findall(r'<p>(.*)</p>', html)
for paragraph in p:
    text.append(paragraph)

# img_tags = soup.find_all('img')

#Extracting the source link for all images in the webpage
img_tags = re.findall(r'src="(.*)/>', html)
for image in img_tags:
    images.append(image)

print(links)
print(text)
print(images)

