import turtle

def tree(plist, l, a, f):
    """
    plist is list of pens
    l is length of branch
    a is half of the angle between 2 branches
    f is a factor by which branch is shortened from level to level.
    """
    if l > 3:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)

        tree(lst,l*f,a,f)

def maketree():
    p = turtle.Turtle()
    p.hideturtle()
    p.speed(1)
    p.left(90)
    p.penup()
    p.forward(-210)
    p.pendown()
    tree([p],200,65,0.64)


def main():
    maketree()

if __name__ == "__main__":
    main()
    turtle.mainloop()
