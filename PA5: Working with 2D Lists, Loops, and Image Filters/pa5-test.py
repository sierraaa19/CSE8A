from CSE8AImage import *
from pa5 import *

"""
RGB codes for common colors. You can add on to this
if you want to experiment with different colors.
"""
black   = (0,0,0)
white   = (255,255,255)
red     = (255,0,0)
green   = (0,255,0)
blue    = (0,0,255)
yellow  = (255,255,0)
magenta = (255,0,255)
gray    = (128,128,128)
purple  = (128,0,128)

def test_complement():
    
    # TEST CASE 1:
    
    # Create a 100*100 image of blue color and visualize it 
    test_img1 = create_img(100, 100, blue)
    save_img(test_img1, "blue_test_img1.jpg")
    # View the pixel values of the original image
    img_str_to_file(test_img1, "blue_test_img1.txt")
    
    # Call complement and visualize the resulting image
    result1 = complement(test_img1);
    save_img(result1, "complement_result1.jpg")
    # View the pixel values of the filtered image
    img_str_to_file(result1, "view_complement_pixels.txt")


    # TEST CASE 2:
    
    # Load the cat image given and call complement on it
    cat = load_img("images/cat.jpg")
    img = complement(cat)
    save_img(img, "complement_cat.jpg")


    # TEST CASE 3:
    # TODO: Add test case for complement function using a self created image similar to Test Case 1

    # Create a 100*100 image of green color and visualize it 
    test_img2 = create_img(100, 100, green)
    save_img(test_img2, "green_test_img2.jpg")
    # View the pixel values of the original image
    img_str_to_file(test_img2, "green_test_img2.txt")
    
    # Call complement and visualize the resulting image
    result2 = complement(test_img2);
    save_img(result2, "complement_result2.jpg")
    # View the pixel values of the filtered image
    img_str_to_file(result2, "view_complement_pixels.txt")

    
def test_negative():

    # TEST CASE 1:
    
    # Create a 100*100 image of red color and visualize it 
    test_img1 = create_img(100, 100, red)
    save_img(test_img1, "red_test_img1.jpg")
    # View the pixel values of the original image
    img_str_to_file(test_img1, "red_test_img1.txt")
    
    # Call negative and visualize the resulting image
    result1 = negative(test_img1);
    save_img(result1, "negative_result1.jpg")
    # View the pixel values of the filtered image
    img_str_to_file(result1, "view_negative_pixels.txt")


    # TEST CASE 2:
    # TODO: Add test case that loads the cat image given and calls negative filter on it

    # Load the cat image given and call complement on it
    cat = load_img("images/cat.jpg")
    img = negative(cat)
    save_img(img, "negative_cat.jpg")




    # TEST CASE 3:
    # TODO: Add test case for negative function using a self created image similar to Test Case 1

    # Create a 100*100 image of purple color and visualize it 
    test_img3 = create_img(100, 100, purple)
    save_img(test_img3, "purple_test_img3.jpg")
    # View the pixel values of the original image
    img_str_to_file(test_img3, "purple_test_img3.txt")
    
    # Call negative and visualize the resulting image
    result3 = negative(test_img3);
    save_img(result3, "negative_result3.jpg")
    # View the pixel values of the filtered image
    img_str_to_file(result3, "view_negative_pixels.txt")




"""
Calling the Test functions one after the other.
You may want to uncomment one test at a time.
OPTIONAL: You can add tests for the custom filters you have
created as part of Star points.
"""

#test_complement()
#test_negative()
