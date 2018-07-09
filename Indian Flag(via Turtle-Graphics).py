import turtle

ob=turtle.Turtle()

ob.speed(5)

ob.color("white")
ob.goto(-350,300)
ob.color("black")

for i in range(2):
    ob.forward(150)
    ob.right(90)
    ob.forward(90)
    ob.right(90)

ob.forward(150)
ob.right(90)
ob.forward(30)
ob.right(90)

ob.color("orange")
for i in range(15):
    ob.forward(150)
    ob.right(90)
    ob.forward(1)
    ob.right(90)
    ob.forward(150)
    ob.left(90)
    ob.forward(1)
    ob.left(90)


ob.forward(150)
ob.goto(-350,270)
ob.color("white")
ob.goto(-350,240)


ob.color("green")
ob.left(180)
for i in range(15):
    ob.forward(150)
    ob.right(90)
    ob.forward(1)
    ob.right(90)
    ob.forward(150)
    ob.left(90)
    ob.forward(1)
    ob.left(90)

ob.forward(150)
ob.goto(-200,240)
ob.color("white")
ob.goto(-200,270)

ob.color("orange")
ob.left(180)
ob.forward(75)

ob.color("blue")
for i in range(360):
    ob.forward(0.25)
    ob.left(1)

ob.left(90)
ob.forward(30)
ob.goto(-275,255)
ob.left(90)
ob.forward(15)
ob.back(30)
ob.goto(-275,255)
ob.left(45)
ob.forward(15)
ob.back(30)
ob.goto(-275,255)
ob.right(90)
ob.forward(15)
ob.back(30)

ob.goto(-275,255)
ob.right(22)
ob.forward(15)
ob.back(30)

ob.goto(-275,255)
ob.left(134)
ob.forward(15)
ob.back(30)

ob.goto(-275,255)
ob.right(45)
ob.forward(15)
ob.back(30)

ob.goto(-275,255)
ob.right(45)
ob.forward(15)
ob.back(30)





    


