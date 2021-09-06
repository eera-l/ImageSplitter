# Image splitter

Split a collection of images into single images. <br>
* `img_size` specifies the size of each extracted image 
* `step` specifies the step between images, if there is any blank space between them

![split image](https://github.com/eera-l/image_splitter/blob/master/image_splitter/images/split_emojis.png)


Usage:
```
pip install image_splitter
```

```
from image_splitter import image_splitter

image_splitter.split_image(filepath='sheet_twitter_64.png', img_size=64, step=2)
```

Twitter emojis from: [CDNPKG.com](https://www.cdnpkg.com/emoji-datasource/file/sheet_twitter_64.png/)


