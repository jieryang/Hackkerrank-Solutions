def countingValleys(steps, path):
    # Write your code here
    count = 0
    sea = 0
    for _ in path:
        if _ == "D":
            sea -= 1
        else:
            sea += 1
            if sea == 0:
                count += 1
    return count
