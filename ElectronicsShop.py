
def getMoneySpent(keyboards, drives, b):
#
# Complete the getMoneySpent function below.
#
    #
    # Write your code here.
    #
    s = 0
    l = []
    for i in keyboards:
        for j in drives:
            s = i+j
            if s <= b:
                l.append(s)
                s = 0
    if len(l)>0:
        return max(l)
    else:
        return -1
