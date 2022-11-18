
def catAndMouse(x, y, z):
    #
    # Write your code here.
    #
    if z>x and z>y:
        a = z-x
        b = z-y
        if a == b:
            return "Mouse C"
        elif a < b:
            return "Cat A"
        else:
            return "Cat B"
    elif x<=z<=y or y<=z<=x:
        a = z-x
        b = z-y
        if a<0:
            a = x-z
        if b<0:
            b = y-z
        if a==b:
            return "Mouse C"
        elif a<b:
            return "Cat A"
        else:
            return "Cat B"
    else:
        a = x-z
        b = y-z
        if a==b:
            return "Mouse C"
        elif a<b:
            return "Cat A"
        else:
            return "Cat B"
