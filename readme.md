# Install WEB SCRAPPING LIBRARIES

1. pip install requests
2. pip install lxml
3. pip install bs4 - Beautiful Soup

=====================================

# GRAB IMAGE AND DISPLAY IN NOTEBOOK

1. Change the (celltype , cell) to Cell -> Markdown which support basic HTML.
2. Inside the markdown cell :-

# Inside Markdown cell :-

# <img src ="image.png -- url"> -> Enter

# DOUBLE CLICK ON MARKDOWN SRC -- TO EDIT THE ENTERED CONTENT

# DISPLAYS THE IMAGE FROM THE SOURCE THROUGH IMAGE URL

======================================

# DOWNLOAD IMAGE FROM WEB USING SCRAPPING

1. requests.get('https:// image url') -- '# https # infront of img src url is necessary to download image'
2. img variable.content = contains raw content of image binary file

# image_link.content == contains the raw binary data of the image

# mode - 'wb' notes writing the binary data into a file created.

<!-- with open('mycomputer_image.png','wb') as image:
    image.write(image_link.content) -->

==========================================
