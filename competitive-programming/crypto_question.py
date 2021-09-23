#question.py
# msg = input("enter your secret message: ")
msg = "sikander is doing good"
x = 'abcdefghijklmnopqrstuvwxyz'
y = x[::-1]
print(x)
print(y)
tran = msg.maketrans(x, y)
print(msg.translate(tran))