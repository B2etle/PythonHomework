a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"  # source string
        # global a  # task 4.2.1
        # nonlocal a  # task 4.2.2
        print(a)

    return inner_function  # task 4.1


if __name__ == '__main__':
    print(enclosing_funcion()())
