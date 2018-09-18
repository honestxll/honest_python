# coding=UTF-8
class Calculator:
    result = ''

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print('我的名字是：%s，%d 块钱' % (self.name, self.price))

    def add(self, num1, num2):
        self.result = num1 + num2
        return self

    def minus(self, num1, num2):
        self.result = num1 - num2
        return self

    def output(self):
        print(self.result)

calcul = Calculator('Good Calculator', 18)
calcul.info()
calcul.add(1, 2).output()
