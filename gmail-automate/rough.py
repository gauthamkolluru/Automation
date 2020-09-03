

def generate_range():
    a = range(1,100)
    for i in a:
        print('generate range')
        yield i


def square_i():
    for i in generate_range():
        print("square_i")
        print(i*i)
        if i > 15:
            break

square_i()