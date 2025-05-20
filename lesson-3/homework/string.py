
meva=['olma','banan','olcha',"o'rik",'gilos']
print(meva[2])



list1=[1,2,3]
list2=[1,5,6]
print(list1+list2)



sonla=[1,2,3,4,5,6,7,8,9]
bir=sonla[0]
ikki=sonla[len(sonla)//2]
uch=sonla[-1]
print(bir,ikki,uch)


favorite_movies = ["Inception", "Interstellar", "The Matrix", "The Dark Knight", "Forrest Gump"]

print(tuple(favorite_movies))


cities = ["London", "New York", "Tokyo", "Paris", "Berlin"]

if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")


numbers = [1, 2, 3, 4, 5]

print(numbers + numbers)




numbers = [1, 2, 3, 4, 5]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)


numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
n1=numbers[2:7:1]
print(n1)


numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
n1=numbers[3:8]
print(n1)


colors = ["red", "blue", "green", "yellow", "blue", "blue", "orange"]
blue_count = colors.count("blue")
print("The color 'blue' appears", blue_count, "times in the list.")


animals = ["ot", "lion", "zebra", "qurbaqa", "baqa", "kalamush", "niynachi"]
print("The color 'blue' appears",animals.count("lion"), "times in the list.")



tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)


my_list = [10, 20, 30, 40, 50]
my_tuple = (1, 2, 3)

print("Length of the list:", len(my_list))
print("Length of the tuple:", len(my_tuple))


my_tuple = (10, 20, 30, 40, 50)

my_list = list(my_tuple)

print("Original tuple:", my_tuple)
print("Converted list:", my_list)



numbers = (15, 3, 27, 8, 42, 1)

max_value = max(numbers)
min_value = min(numbers)

print("Maximum value:", max_value)
print("Minimum value:", min_value)


words = ("apple", "banana", "cherry", "date", "elderberry")

reversed_words = words[::-1]

print("Original tuple:", words)
print("Reversed tuple:", reversed_words)

