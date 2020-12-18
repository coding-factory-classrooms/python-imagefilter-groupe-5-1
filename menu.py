import sys

from function_dilated import function_dilated
from function_black_white import function_black_and_white
from function_blurry import blurry
from function_blurry_dilated import function_blurry_dilated
from function_black_and_white_blurry import function_black_and_white_blurry
from function_black_and_white_dilated import function_black_and_white_dilated
from function_all_filters import function_all


print("\n\n\n\n")

"""
   She is used for the CLI in order to make the parameter for the application
   :param blurry: name of the blurry filter
   :param dilated: name of the dilated filter
   :param gray: name of the gray filter
   """
args = sys.argv
for arg in args:
    if arg == '-dilated':
        print("FUNCTION DILATED WITH PICTURES\n")
        function_dilated()
    elif arg == '-blackandwhite':
        print("FUNCTION BLACK AND WHITE WITH PICTURES\n")
        function_black_and_white()
    elif arg =='-blurry':
        print("FUNCTION BLURRY WITH PICTURES\n")
        blurry()
    elif arg == '-blurry_dilated':
        print("FUNCTION BLURRY AND DILATED\n")
        function_blurry_dilated()
    elif arg =='-black_and_white_blurry':
        print("FUNCTION BLURRY AND BLACK AND WHITE\n")
        function_black_and_white_blurry()
        print("Your image is now in black and white and blurry")
    elif arg =='-function_black_and_white_dilated':
        print("FUNCTION DILATED AND BLACK AND WHITE")
        function_black_and_white_dilated()
        print("Your image is now in blurry and black and white\n")
    elif arg =='-function_all':
        print("ALL FILTERS")
        function_all()

