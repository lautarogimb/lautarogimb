x = 0
while x < 30:
    x = x + 1
    if x == 15:
        print(f"The execution of the loop was broken when x was {x}")
        break
    if x != 4 and x != 6 and x!= 10:
        print(f"The value of the loop is: {x}")
    else:
        print(f"The value {x} was skipped")