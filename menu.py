from function_dilated import function_dilated
from function_black_white import function_black_and_white
from function_blurry import blurry
print("\n\n\n\n")
print("FUNCTION DILATED WITH PICTURES\n")
function_dilated()
print("FUNCTION BLACK AND WHITE WITH PICTURES\n")
function_black_and_white()
print("FUNCTION BLURRY WITH PICTURES\n")
blurry()

def dictionary(blurry, dilated, gray,):
    """
    She is used for the CLI in order to make the parameter for the application
    :param blurry: name of the blurry filter
    :param dilated: name of the dilated filter
    :param gray: name of the gray filter
    """

    filters = {
        '1': blurry,
        '2': dilated,
        '3': gray,
        '4': blurry + dilated,
        '5': blurry + gray,
        '6': gray + dilated,
        '7': blurry + gray + dilated
    }



