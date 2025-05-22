
talabalar = {
    "Ali": 85,
    "Vali": 92,
    "Sardor": 78,
    "Dilshod": 90
}

sorted_asc = dict(sorted(talabalar.items(), key=lambda item: item[1]))
print("O'sish tartibi:", sorted_asc)

sorted_desc = dict(sorted(talabalar.items(), key=lambda item: item[1], reverse=True))
print("Kamayish tartibi:", sorted_desc)


my_dict={0: 10, 1: 20}
my_dict[2]=30
print(my_dict)




dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4={}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)

print(dic4)




n = 5  # You can change this value

squares_dict = {x: x * x for x in range(1, n + 1)}

print(squares_dict)



n = 15  # You can change this value

squares_dict = {x: x * x for x in range(1, n + 1)}

print(squares_dict)



num={1,2,3,4,5}
type(num)
print(num)


num={1,2,3,4,5}

# Iterate over the set
print("Numbers in the set:")
for item in num:
    print(item)



toplam={'ali','Aziz','Akbar'}
toplam.update(['Olim',"umit"])
toplam.add('gilos')
print(toplam)


toplam.remove('ali')
toplam.discard('gilos')
print(toplam)





my_set = {"apple", "banana", "cherry"}

item_to_remove = "banana"

my_set.discard(item_to_remove)

print("Updated set:", my_set)
