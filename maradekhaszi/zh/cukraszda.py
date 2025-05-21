class Cake:
    def __init__(self,name,price):
        self.name=name
        self.is_sold=False
        self.price=price

    def sell(self):
        self.is_sold=True
        return self.price


class Baker:
    def __init__(self,name):
        self.money=0
        self.name=name

    def bake(self,cake_name,cake_price):
        return Cake(cake_name,cake_price)
    
    def sell(self,cake):
        if not cake.is_sold:
            self.money += cake.sell()
        return cake.price


def main():
    bejgli = Cake("diós bejgli", 100)
    print(bejgli.is_sold) # False
    price_of_bejgli = bejgli.sell()
    print(bejgli.is_sold) # True
    print(price_of_bejgli) # 100
    #.--------------------------------------------------------------------------
    peti = Baker("Peti")
    print(peti.money) # 0
    bejgli = peti.bake("diós bejgli", 100)
    print(bejgli.is_sold) # False
    peti.sell(bejgli)
    print(bejgli.is_sold) # True
    print(peti.money) # 100

main()
