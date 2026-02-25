#01
print("The sum of 1 to 5 is :", 1+2+3+4+5 )

#02-01
N = -1
S = 0

#02-02
n%2 == 0

#03
n = int(input("enter the number:"))
print("*"*2*n)
print("#"*n)

#04
name = "David Doe"
address= "1600 Wilshire Blvd #205, Los Angeles CA 90017"
print(f"NAME:{name}\nADDRESS:{address}")

#05
0
1
0
1

#06
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number" ))
print("Numbers from smallest to largest are:")
if num1==num2:
    print("Please enter two different numbers!")
elif num1<num2:
    print(f"[{num1},{num2}]")
else: 
    print(f"[{num2},{num1}]")

#07
adult = int(input("Are you an adult? (1 if you are an adult, 0 if you are minor): "))
if adult == 1:
    married = int(input("Are you married? (1 if you are married, 0 if you are single): "))
    if married == 1:
        print("You are an adult who is marrried.")
    else:
        print("You are a single who is adult")
else:
    print("You are a minor!")

#08
for num in range(2, 13):
    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(f"{num} : Prime number")
    else:
        print(f"{num} : Composite number")

#09
print("Three digit armstrong numbers are:", end=" ")
for num in range(100, 1000):
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    if total == num:
        print(num, end=" ")

#10
l1 = ['i like','i love']
l2 = ['pancake','kiwi juice','espresso']
for i in l1:
    for j in l2:
        print(i, j)

#11
person = {'name':'david doe','age':26,'weight':82,'job':'data scientist'}
person.update({'father':'john doe'})
print(person)

#12
lst = [5,6,9,2,12,3,8,7]
max_index = 0
for i in range(len(lst)):
    if lst[i] > lst[max_index]:
        max_index = i
lst[0], lst[max_index] = lst[max_index], lst[0]
print("Largest number is:", lst[0])
print("Updated list:", lst)

#13
a = [[1,2],[3,4],[5,6]]
new_list = []

for sublist in a:
    for item in sublist:
        new_list.append(item)

print(new_list)

#14
maria = {
    'korean': 95,
    'english': 88,
    'math': 92,
    'science': 82
}
total = sum(maria.values())
count = len(maria)
average = total / count
print(average)

#15
import copy
school = {
    'kim': {'age': 16, 'hei': 170, 'grade': 3},
    'lee': {'age': 15, 'hei': 168, 'grade': 2},
    'choi': {'age': 14, 'hei': 173, 'grade': 1}
}
school2 = copy.deepcopy(school)
print("school1 is school2 ?", school is school2)

#16
scores = (
    ('Hyun', 88, 95, 90),
    ('Kang', 85, 90, 95),
    ('Park', 70, 90, 80),
    ('Hong', 90, 90, 95)
)
names, english, math, science = zip(*scores)
print("Math Scores:", math)
average_math = sum(math) / len(math)
print("Average Math Score:", average_math)
