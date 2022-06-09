import os


def open_file(filename):
    if not os.path.exists(filename):
        print("Chosen file does not exist")
    elif os.stat(filename).st_size == 0:
        print("Chosen file is empty")

    else:
        with open(filename) as f:
            file = f.read()
        return file


def write_file(filename, content):
    if os.path.exists(filename) and os.stat(filename).st_size > 0:
        print("File exist and it's not empty")
    else:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'File {filename} is saved!')
