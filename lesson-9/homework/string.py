# 1
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:
    def __init__(self, radius: int):
        self.radius = radius
        self.area = 3.14 * radius * radius
        self.perimeter = 2 * 3.14 * radius

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter
    
d=Circle(50)

print("Yuza:", d.get_area())
print("Perimetr:", d.get_perimeter())


# 2
# Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

class Person:
    def __init__(self, name: str,country: str,date_of_birth: int):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
        self.age = 2025 - date_of_birth 

    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def get_country(self):
        return self.country
    
d=Person('ali','uzb',2006)

print(f"Salom {d.get_name()},siz {d.get_country()}da turasiz va siz {d.get_age()} yoshdasiz")



# 3
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "0 ga bo‘lish mumkin emas"
        return self.a / self.b

# Misol uchun
calc = Calculator(10, 5)
print("Yig‘indi:", calc.add())
print("Ayirma:", calc.subtract())
print("Ko‘paytma:", calc.multiply())
print("Bo‘linma:", calc.divide())



# 4
# Write a Python program to create a class that represents a shape. Include methods to calculate its area
#  and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.
class represents :
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
# 3
# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  
        self.right = None  

class BinarySearchTree:
    def __init__(self):
        self.root = None  

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)  
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)


tree = BinarySearchTree()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(8)

print(tree.search(8))   
print(tree.search(5))  


# 6
class Stack:
    def __init__(self):
        self.items = [] 

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack bo'sh!"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack bo'sh!"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack:", self.items)



s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.display()           

print("Pop:", s.pop())   
print("Peek:", s.peek()) 
s.display()


# 7
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  


class LinkedList:
    def __init__(self):
        self.head = None  

    def insert(self, data):
        new_node = Node(data)  
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node  

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev is None:
                    self.head = current.next  # Bosh tugunni o'chirish
                else:
                    prev.next = current.next  # O‘rta yoki oxirgi tugunni o‘chirish
                return
            prev = current
            current = current.next
        print(f"Element topilmadi: {data}")

    def display(self):  # <-- Bu yerda to‘g‘ri joyda turishi kerak
        current = self.head
        if not current:
            print("Ro'yxat bo‘sh.")
            return
        print("Ro'yxatdagi elementlar:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Test qilish
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()       # 10 -> 20 -> 30 -> None

ll.delete(20)
ll.display()       # 10 -> 30 -> None

ll.delete(100)     # Element topilmadi: 100




# 8

class ShoppingCart:
    def __init__(self):
        self.items = {}  
    def add_item (self,mahsulot,miqdor,suma):
        mahsulot = mahsulot.strip()
        if mahsulot in self.items:
            self.items[mahsulot][0]=+miqdor
        else :
            self.items[mahsulot] = [miqdor,suma]
    def remove_item(self,mahsulot):
        mahsulot = mahsulot.strip()
        if mahsulot in self.items[mahsulot]:
            self.items.pop(mahsulot)
        else:
            return f'{mahsulot} savatda mavjud emas'
    def get_total(self):
        total = 0
        for miqdor, suma in self.items.values():
            total += miqdor * suma
        return total

    def display_cart(self):
        if not self.items:
            print("Savat bo'sh.")
        else:
            print("Savat tarkibi:")
            for mahsulot, (miqdor, suma) in self.items.items():
                print(f"{mahsulot} - {miqdor} dona, {suma} so'm/dona")


    
cart = ShoppingCart()
cart.add_item("Olma", 3, 2000)
cart.add_item("Non", 2, 3000)
cart.display_cart()

print("Jami narx:", cart.get_total(), "so‘m")

cart.remove_item("Olma")
cart.display_cart()
print("Yangi jami narx:", cart.get_total(), "so‘m")

#9
class Stack :
    def __init__(self):
        self.items = []
    def push(self,element):
        self.items.append(element)
    def pop(self):
        if len(self.items)>0:
            del self.items[-1]
            print(f"{self.items} stackdan olib tashlandi.")
        else:
            print("Stack bo‘sh, element yo‘q.")
    def display(self):
        if self.items:
            print("Stack elementlari:", self.items)
        else:
            print("Stack hozircha bo‘sh.")


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

s.pop()
s.display()


#10
class Queue  :
    def __init__(self):
        self.items = []
    def enqueue(self,navbat):
        self.items.append(navbat)
    def dequeue(self):
        if self.items:
            removed = self.items.pop(0) 
            print(f"{removed} navbatdan chiqarildi.")
        else:
            print("Navbat bo‘sh.")
    def display(self):
        if self.items:
            print("Navbatdagi odamlar:", self.items)
        else:
            print("Navbatda hichkim yo'q.")



q = Queue()

q.enqueue("Diyorbek")
q.enqueue("Ozoda")
q.enqueue("Ali")

q.display()

q.dequeue()
q.display()

q.dequeue()
q.dequeue()
q.dequeue()  # Bo‘sh holatda chiqib ko‘rish

# 11
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance):
        if name in self.accounts:
            print(f"{name} uchun hisob allaqachon mavjud.")
        else:
            self.accounts[name] = initial_balance
            print(f"{name} uchun hisob yaratildi. Boshlang'ich balans: {initial_balance}")

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
            print(f"{name} hisobiga {amount} qo‘shildi. Yangi balans: {self.accounts[name]}")
        else:
            print(f"{name} uchun hisob topilmadi.")

    def withdraw(self, name, amount):
        if name in self.accounts:
            if self.accounts[name] >= amount:
                self.accounts[name] -= amount
                print(f"{name} hisobidan {amount} yechildi. Qolgan balans: {self.accounts[name]}")
            else:
                print(f"{name} hisobida yetarli mablag‘ yo‘q.")
        else:
            print(f"{name} uchun hisob topilmadi.")

    def get_balance(self, name):
        if name in self.accounts:
            print(f"{name} ning joriy balansi: {self.accounts[name]}")
        else:
            print(f"{name} uchun hisob topilmadi.")

    def show_accounts(self):
        if not self.accounts:
            print("Hech qanday hisob mavjud emas.")
        else:
            print("Bankdagi barcha hisoblar:")
            for name, balance in self.accounts.items():
                print(f"{name} -> {balance} so'm")



bank = Bank()

bank.create_account("Ali", 1000)
bank.create_account("Laylo", 2000)

bank.deposit("Ali", 500)
bank.withdraw("Ali", 300)

bank.get_balance("Ali")
bank.get_balance("Laylo")

bank.withdraw("Laylo", 3000)  # Yetarli mablag‘ yo‘q holatini ko‘rish

bank.show_accounts()
