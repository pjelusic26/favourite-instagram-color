# favourite-instagram-color
Have you ever wondered what your favourite color is? I have, and the answer is a pretty boring one.

----------

A few years ago, I wanted to find out what my favourite color was. So I decided to download all the images from my Instagram profile, inspected them in Photoshop, and calculated pixel values for each color channel (R, G, B). The result was pretty gray, as I used each channel similarly.

Now that I started working with Python, I decided to make the process more seamless, and make a magical script that would replace what Photoshop did in the version from a few years back. As I will be working with CMYK images in the future, the magical script is also able to calculate pixel values in that format.

The result I got is, again, very gray and boring:

![alt text](https://github.com/pjelusic26/favourite-instagram-color/blob/master/favourite_instagram_color.jpg)

- R: 118 (34.37%)
- G: 114 (32.91%)
- B: 113 (32.72%)

Looks like I still can not find my favourite color, and who knows if I ever will. Still, the magical script does what it is told, and does not care about my indecisiveness.

----------

A couple of notes below:
- the script can only read .jpg files
- to read images, create 'images/' folder, and place images inside it
- the script prints:
  - percentage value of each color channel in image (example: R: 40% G: 30% B: 30%)
  - average pixel values for each channel (example: R: 120 G: 90 B: 180)
- for future development: It would be nice to create a Photoshop Action that will somehow modify images to get a more meaningful result (example: total area coverage of 'mostly' Red/Green/Blue channels; etc.)

----------

Resources I found useful for the project:

Chrome Instagram Downloader
https://chrome.google.com/webstore/detail/downloader-for-instagram/olkpikmlhoaojbbmmpejnimiglejmboe

Matplotlib Image Tutorial
https://matplotlib.org/1.5.3/users/image_tutorial.html
