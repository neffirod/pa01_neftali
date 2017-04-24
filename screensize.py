# screensize.py
# Neftali Rodriguez, 04/19/21

def height(D,W,H):
    height=((D**2 * H**2)/(W**2 + H**2))**(1/2)
    return(height)


def width(D,W,H):
    width=(W/H) * height(D,W,H)
    return(width)




# solution must be above this comment

# do not change any part of the code below
def main():
    D, W, H = eval( input("enter D, W, H (separated by commas): ") )
    h = height(D, W, H)
    w = width(W, H, h)
    print("width = {0:.1f}, height = {1:.1f}".format(w, h))

main()
