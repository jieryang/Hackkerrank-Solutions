
def catAndMouse(x, y, z):
    #
    # Write your code here.
    #
    a = abs(x-z)
    b = abs(y-z)
    if a == b:
        return "Mouse C"
    elif a<b:
        return "Cat A"
    else:
        return "Cat B"
