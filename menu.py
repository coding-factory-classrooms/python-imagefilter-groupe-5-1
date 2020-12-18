import sys

from function_dilated import function_dilated
from function_black_white import function_black_and_white
from function_blurry import blurry


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

