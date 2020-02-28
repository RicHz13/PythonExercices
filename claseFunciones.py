import turtle
def main():
    window = turtle.Screen()
    ricardo = turtle.Turtle()

    make_square(ricardo)
    turtle.mainloop()

def make_square(ricardo):
    length = int(input('Tamaño de cuadrado: '))

    for i in range(4):
        make_line_and_turn(ricardo, length)

def make_line_and_turn(ricardo, length):
    ricardo.forward(length)
    ricardo.left(90)



if __name__ == '__main__':
    main()