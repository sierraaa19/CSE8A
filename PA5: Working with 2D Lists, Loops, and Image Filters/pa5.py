from CSE8AImage import *

# PART 1.1

def make_menu(fruits, toppings):
    menu = []
    for fruit in fruits:
        for topping in toppings:
            menu.append(str(fruit) + " ice cream with " + str(topping))
    return menu

# PART 1.2
# TODO: Write the function as given in PA specifications

def multiplication_table(num, table):
    new = []
    for x in range(1, num+1):
        lst = []
        new.append(lst)
        for number in range(len(table[0])):
                number += 1
                lst.append(x*number)
    return new

# PART 1.3

def complement(img):
    for r in range(len(img)):
        for c in range(len(img[r])):
            pix = img[r][c]
            img[r][c] = (pix[0], pix[2], pix[1])            
    return img

cat = load_img("images/cat.jpg")
cat_mod = complement(cat)
save_img(cat_mod, "cat_modified.jpg")


def negative(img):
    for r in range(len(img)):
        for c in range(len(img[r])):
            pix = img[r][c]
            img[r][c] = (255-pix[0], 255-pix[1], 255-pix[2])            
    return img

cat = load_img("images/cat.jpg")
cat_neg2 = negative(cat)
save_img(cat_neg2, "cat_neg2.jpg")
















