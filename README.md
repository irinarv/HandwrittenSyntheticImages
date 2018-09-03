# HandwrittenSyntheticImages
This directory contain the software for creation the synthetic images of Hebrew handwritten text

FILE: getSortedUniqueListOfWords.py 
		 
		 read the contents of the input text file, strips all punctuation marks and special characters from the words
		 creates an output text file 'words_and_labels.txt' with a sorted list of unique words from the input file
		 with the following format
		 0 word0
		 1 word1
		 ...
		 N wordN
		 
		 The output directory with the images is 'pics'

FILE    words_and_labels.txt
        creates synthetic images of the words from the file words_and_labels.txt, for each words examples with different fonts,
        font sizes, image sizes and various transformations, such a rotation, blur, filtering, resizing
         
FILE 	image_functions.py
		file with various function for image transformations
		
DIRECTORY hebrew_fonts
		the directory with different hebrew_font in TTF format