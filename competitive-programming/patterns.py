def pyramid(rows = 6):
    for i in range(1, rows+1):
        print(end="  "*(rows-i))
        print("* "*(i*2-1), end="")
        print()

def pyramid_down(rows = 6):
    for i in range(rows, 0, -1):
        print(end="  "*(rows-i))
        print("* "*(i*2-1), end="")
        print()

def right_angle_traingle_down(rows = 6):
    for i in range(rows+1, 0, -1):
        print("* "*i)

def right_angle_traingle(rows = 6):
    for i in range(1,rows+1):
        print("* "*i)

right_angle_traingle()
# right_angle_traingle_down()
# pyramid()
# pyramid_down()