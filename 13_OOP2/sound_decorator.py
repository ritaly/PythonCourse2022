def sound_decorator(params_func):
    def nested():
        print('~~~~~~~~~~~~~~')
        params_func()
        print('~~~~~~~~~~~~~~')

    return nested

@sound_decorator
def dog_sound():
    print('Hau hau')

@sound_decorator
def cat_sound():
    print('Miau miau')

def main():
    # dog = sound_decorator(dog_sound)
    # dog()
    dog_sound()

    cat_sound()

if __name__ == '__main__':
    main()