
x = 10

def cube():

    x = int(input('enter the num'))

    def inner():
        return x**3

    return inner()
print(cube())

