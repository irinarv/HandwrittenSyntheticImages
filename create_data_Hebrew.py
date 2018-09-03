from PIL import Image, ImageDraw, ImageFont
import os
import itertools  # iterator tools
import image_functions 
from scipy.misc import imread, imsave
import numpy as np
#===============================================================================
# CONSTANTS
#===============================================================================
OUT_DIR = "pics/"
FONT_PREFIX = "hebrew_fonts/"
DEFAULT_IMAGE_SIZES = [(200, 100), (240, 120)]
DEFAULT_FONT_SIZES = [40, 45, 50, 55, 60]
DEFAULT_LOCATIONS = [(25, 25), (30, 30), (33, 33)] 


#===============================================================================
# create the image with given text on it
# label is the string with a word (e.g. "green")
# word is the string with word number (e.g. "1")
#===============================================================================
def process_single_image(label, word, size, font, fontsize, loc, prefix=""):
    # create output directory for this word image

    if not os.path.exists(OUT_DIR + word):
        os.makedirs(OUT_DIR + word)
        
    # Drawing on image 
    blank_image = Image.new("L", size, 'white')
    img_draw = ImageDraw.Draw(blank_image)
    
    fnt = ImageFont.truetype(font, fontsize)  # creating font
    label = label[::-1]  # Hebrew is written right to left, so we need to reverse it to get the right image    
     
    img_draw.text(loc, label , fill='black', font=fnt)
    
    # save the image
    direc = OUT_DIR + word
    img_path = '/' + prefix + 'original.png'
    
    #print (direc + img_path)
    
    blank_image.save(direc + img_path)    
    blank_image.close()
    
    # create copies
    create_copies(direc, img_path, prefix)


#===============================================================================
# # direc + org = path to the picture
# # this functions, reads the picture in path and creates different versions of it
# # using the functions in image_functions.get()
#===============================================================================
def create_copies(direc, org, img_id):
    
    image_data = imread(direc + org).astype(np.float32)
    size = image_data.shape[0]  # dimension of the image
    prefix = direc + '/test_out'
    index = 0
    funcs = image_functions.get()
    for f in funcs:
        ims = f(image_data, size)
        for im in ims:
            imsave(prefix + img_id + '-' + str(index) + '.png', im)
            index += 1

#===============================================================================
# 
#===============================================================================
def create_data(word, label, sizes=DEFAULT_IMAGE_SIZES,
        font_sizes=DEFAULT_FONT_SIZES,
        locations=DEFAULT_LOCATIONS,
        default_dir=OUT_DIR):
    
    
    fonts = os.listdir(FONT_PREFIX)
    for i in range(len(fonts)):
        fonts[i] = FONT_PREFIX + fonts[i]
    
    i = 0
    # itertool.product is a cartesian product, equivalent to a nested for-loop
    for (size, font, font_size, location) in itertools.product(
            sizes, fonts, font_sizes, locations):
        process_single_image(word, label, size, font, font_size, location, str(i))
        i += 1


#===============================================================================
# processes the line with word int it
# line format:
# wordsnum wordstring (e.g. "1 bed")
#===============================================================================
def process_word(line):
    line = line.split()
    word, label = line[0], line[1].rstrip()
    create_data(label, word)


#===============================================================================
# opens the text file with the list of words
# the text file format: each word on its line 
# words1num word1string
# words2num word2string
# ....
# wordsNnum wordNstring
#===============================================================================
def create_words(filename):
    wordsfile = open(filename, 'r');
    
    for line in wordsfile:
        process_word(line)
    wordsfile.close()


#===============================================================================
# MAIN FUNCTION
#===============================================================================
def main():
    # os.system("cls")
    ifilename = "words_and_labels_small.txt"
    create_words(ifilename)


#------------------------------------------------------------------------------ 
if __name__ == "__main__": 
    main()
