from areas import count_circle_area, count_square_area, count_rectangle_area

def main():
    rooms = {
        "square": [4, 5, 2],
        "circle": [3, 4, 5],
        "rectangle": [[1, 2], [3, 4]]
    }

    total = 0
    for shape, rooms in rooms.items():
        if shape == 'square':
            for room in rooms:
                total += count_square_area(room)
        elif shape == 'circle':
            for radius in rooms:
                total += count_circle_area(radius)
        elif shape == 'rectangle':
            for room in rooms:
                a, b = room
                total += count_rectangle_area(a, b)
        else:
            print("Nie znam takiego kształ")

    print("Powierzchnia całkowita wynosi", total)

if __name__ == '__main__':
    main()