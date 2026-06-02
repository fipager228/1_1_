import random

class Bank:
    def __init__(self, name, balance):
        self.name = str(name)
        self.balance = balance
        self.number = [[2,2,0,6]]

        for i in range(3):
            numb_4 = []
            for l in range (4):
                a = random.randint(0 , 9)
                numb_4.append(a)
            self.number.append(numb_4)

    def perevod(self, num_2, summa):
        if summa <= self.balance :
            num_2.balance  = num_2.balance + summa
            self.balance -=summa
            print(f"Перевод в размере {summa} на счет {num_2.name} выполнен")
        else:
            print("Недостаточно средств")





chel_1 = Bank('Вася', 100)
print(chel_1.name,chel_1.number)

chel_2 = Bank('Коля',5)
print(chel_2.name, chel_2.balance)

chel_1.perevod(chel_2,-50)
print(chel_2.balance)
print(chel_1.balance)
