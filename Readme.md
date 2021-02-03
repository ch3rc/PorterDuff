###How to run
___
python3 porter-duff.py [-h, --help] [img_file] [img_file] [mask_file] [mask_file]
___
- -h --help: brings up a help message
- If no input is provided then a blue circle and red cross will be drawn and run through the operations
- If only images are provided then program will create the masks for you
- if all input is provided then you will get same results as if you only provided images
___
###Known issues
___
The pre-drawn masks dont seem to be working quite so well with the images. The in function required 0 to 255
threshold where as the other functions required 225 to 255 threshold. Not sure where the issue is with it.
___
##links
___
- [github](www.https://github.com/ch3rc/PorterDuff "github account") for code and logs under master branch
- contact me at my [UMSL email](ch3rc@umsystem.edu) if you have any questions