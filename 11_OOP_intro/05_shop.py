class Product:
    def __init__(self, name, size, price, color):
        self.name = name
        self.size = size
        self.price = price
        self.color = color

    def product_show(self):
        print(self.name.title(), self.size, self.color.title(), self.price)

    def product_buy(self, money):
        return "Sold" if money >= self.price else "Its too expensive"


class Shop:
    def __init__(self, products=[]):
        self.products = products

    def show_all(self):
        for index, item in enumerate(self.products):
            print(index, end=' - ')
            Product.product_show(item)

    def buy(self, index, wallet):
        selected = self.products[index]
        print(Product.product_buy(selected, wallet)) # selected.product_buy()


def main():
    tshirt = Product('tshirt', 'S', 30, 'red')
    dress = Product('dress', 'M', 40, 'green')
    shoes = Product('shoes', '39', 120, 'black')

    store = [tshirt, dress, shoes]
    my_shop = Shop(store)
    my_shop.show_all()
    my_shop.buy(1, 10)





if __name__ == '__main__':
    main()
