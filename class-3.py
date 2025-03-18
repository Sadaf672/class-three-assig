# list
fruits :list [str] = ["mango","banana", "orange", "graphs", "kivi"]
fruits.pop()
fruits.append("peach")  
fruits.remove("mango")
print(fruits)

# tuple.......

fruits_tuple = ('apple', 'banana', 'orange', 'mango', 'grape')
print(fruits_tuple)
print(fruits_tuple[0])  # Output: apple

# set........
fruits = {'apple', 'banana', 'mango', 'apple'}  # Duplicate 'apple' will be ignored
fruits.add("peach")
fruits.remove("apple")
print(fruits)  # Output: {'mango', 'banana', 'peach'}

# Dictionary.........
person :dict = {
    'username':"sadaf",
    "age":25,
    "city":"karachi"
}
print(person["username"])
print(person["age"])
print(person["city"])

# updating a key value in our dictionary
person["username"] = "iqra"
print(person["username"])

# Adding a key value in our  dictionary
person["country"] ="pakistan"
print(person)

#  Loops......
# For Loop...
numbers = [1,2,3,4,5,6]
for num in numbers :
    # print(num)
    print(num *2)


# While Loop.....
countdown = 10
while countdown >=1:
    print(f"{countdown}")
    countdown -=1











