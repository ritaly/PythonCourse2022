def upper_case(param):
    def upper_nested():
        result = param()
        return result.upper()

    return upper_nested

@upper_case
def get_text():
    return 'python is great!'

def main():
    my_text = get_text()
    print(my_text)


if __name__ == '__main__':
    main()