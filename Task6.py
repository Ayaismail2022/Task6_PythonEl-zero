"""
Task 6
"""
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(dict.fromkeys(my_list))

print(unique_list)
print(type(unique_list))
print(unique_list[:-1])
print("--------------------------------------------------")
# قم بالدمج بثلاث طرق مختلفة 
nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums.union(letters))
print(nums | letters)
print(list(nums)+list(letters)) # TypeError: unsupported operand type(s) for +: 'set' and 'set'

print("--------------------------------------------------")

my_set = {1, 2, 3}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)
my_set.discard("C")
print("--------------------------------------------------")

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
print("---------------------------------------------------")

my_Dictionary = {
    "Python":"90%",
    "Html":"85%",
    "CSS":"80%",
    "JS":"60%",

}

print("Python progress is ", my_Dictionary["Python"])
print("Html progress is ", my_Dictionary["Html"])
print("CSS progress is ", my_Dictionary["CSS"])
print("JS progress is ", my_Dictionary["JS"])
#قم بإضافة مهارة جديدة لل Dictionary مع النسبة المئوية الخاصة بها ثم قم بطباعتها في السطر الخامس
my_Dictionary["Java"] = "85%"
print("Java progress is", my_Dictionary["Java"])