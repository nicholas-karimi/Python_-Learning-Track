"""Implemeting the ljust(), rjust() and center() string methods."""

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v). rjust(rightWidth))


picnicItems = {'sandwiches':4, 'apples': 12, 'cups':4, 'cookies': 400}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
