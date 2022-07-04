def wrapper():
    txt = 'closure'

    def nested():
        return '--> Jestem w środku', txt * num

    return nested




def main():
    returned_func = wrapper()

    print(returned_func(6))

if __name__ == '__main__':
    main()