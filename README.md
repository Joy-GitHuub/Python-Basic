1. What is Python?
ans:- Python is a interpreted, object-oriented, high-level programmin language with dynamic semantics.


2. Why is choose python
Ans:- Python has a simple syntax and hence is easy to understand and learn. Thus, making to popular pick when it comes to programmin languages. As you can see, the same code can be written using fewer lines in Python. Thus making it much simpler to use on many levels.

3. Where is Python Used?
Ans:- Python is used in everything from machine learning to building websites and software testing. Python is used across a wide variety of industries. Of course, the most common areas where python language is used are for building mobile web deskot applications. 


4. Python for Multi-purpose usage?
Ans:- a.{Webapp development} b.{Quick prototyping} c.{Scripting} d.{Data science} e.{Databse programming}

## Python Print
```py
1. print("Hello Python World");
```

## Python Comment
```py
# Python Single line Comment

""" Multiple line Comment
1. Python Easy to learn
 """
```

## Python multiple line print
```py
* Python Backslash character / Escape Sequences
print("Joy Bose \n0177777777");
print("Joy Bose \t01888888880");
print("\"Joy Bose\"")

# Formatted String
num1 = 20;
num2 = 10;
x = f"{num1} + {num2} = {num1 + num2}";
print(x);

- \' => Single Quote
- \\ => Backslash
- \n => New line
- \r => Carriage Return
- \t => Tab
- \b => Backspace
- \f => Form Feed
- \000 => Octal Value
- \xhh => Hex Value
```

## Python Variable

```py
# Python Variable
name = "X",
age = 11,
cgpa = 3.27;
print(f"Our new Student name is {name}", name);
print(name ," lives in Dhaka");
print("He is currently ", age, " Years old");
print("At the age of ", age, " He has started to learn Python");
print(name, " has scored ", cgpa, " in his final exam")
```

## Python Data Type
```py
1. Text Type: str,
2. Numeric Types: int, float, complex,
3. Sequence Types: list, tuple, range,
4. Mapping Type: dict,
5. Set Types: set, frozenset,
6. Boolean Type: bool,
7. Binary Types: bytes, bytearray, memoryview,
8. None Type: NoneType,

x = "Hello World"; # str
x = 20; # int
x = 20.5 # float,
x = 1j; #complex
x = ["apple", "banana", "cherry"]; # list
x = ("apple", "banana", "cherry"); # tuple
x = range(5); # range
x = {"name": "X", "age": 11, "isPass": False}; # dict
x = {"apple", "banana", "cherry"}; # set
x = frozenset({"apple", "banana"}); # frozenset
x = True # bool
x = b"hello"; # bytes
x = bytearray(4); # bytearray
x = memoryview(bytes(5)); # memoryview
x = None; # NoneType
```



## Numerical Operation
* Python Arithmetic Operators
```py
- Python Arithmetic Operators
first = 10;
second = 5;
total = first + second;
sub = first - second;
multi = first * second;
division = first / second;
modulus = 18 % 5; 
print(2**2); # ans= 4 [Exponentiation]

a =29;
b = 3;
print(a//b); # The floor division // rounds the result down to the nearest whole number.
```
* Python Assignment Operators
```py
- Python Assignment Operators
x = 5;
x += 3;
print(x); # ans:- 8
x -= 2
print(x); # ans:- 6
x *= 2;
print(x); # ans:- 12
x /=  2;
print(x); # ans:- 6.0
```

* Python Comparison Operators
```py
- Python Comparison Operators
x = 10;
y = 10;
print(x == y); # Equal
print(x != y); # Not Equal
print(x > y); # Greater than
print(x < y); # Less Than
print(x <= y); # Greater than or equal to
print(x>= y); # Less than or equal to
```



## Python String
```py
"""
- String are arrays
- Like many other propular programming languages, strings in Python are arrays of bytes representing unicode characters.
** Strings in python are surrounded by either single quotation marks, or double quotation marks.
** String length

"""
# String print
print("Hello")

# Assign String to a Variable
a = "Hello";
print(a)

# three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# three single quotes:
b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# String Lenght
a = "Hello, World!"
print(len(a))

#  Check String
txt = "The best things in life are free!"
print("frees" in txt)

# if state useing in a string
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# looping throught a string
string = "bangla";
for x in string:
    print(x);
```


## Python String Method
```py
# Specify the start index and the end index, separated by a colon, to return a part of the string.
string = "bangla";
slices = string[0:3];
print(slices)
slices = string[3:];
print(slices)


# String - Modify Case 

# - String Case
string = "bANgla";
stringUpperCase = string.upper();
stringLowerCase = string.lower();

# - Remove Whitespace
a = " Hello, World! ";
b = a.strip();
print(a)
print(b);

# - Replace String
#  The replace() method replaces a string with another string
a = "Joy Bose";
b = a.replace("o", "O")
print(b);

# - The split() method returns a list wwhere the text between the specified separator becomes the list items.
a = "Hello World";
b = a.split(" ");
print(b);
```

## String Format() Method
```py
""" 
** String format() method
"""
num1= 20;
num2= 30;
print(f"This is my super number num1 + num2 = {num1 + num2}");

userName = "Joy";
print(f"My name is {userName}");
```

## Python Booleans
```py
""" 
** Boolean Data Types
- In programming you often need to know if an expression is True or False.
- You can evaluate any expression in Python, and get one of two answers, True or False.

** True Values
-. True, 0, -1, 1, "Hello"

** False Values
- False, None, 0, '''', (), [], {}
"""

# True or False Return
print(10>9);
print(10 == 9);
print(10<9);


# True Values
print(bool("Hello"));
print(bool(1));
print(bool(-1));
print(bool("A"));
print(bool({"id": 1}));
print(bool([1,2]))

# False Values
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
```

## Binary Types
```py
""" 
** Binary Types
- bytes 
- bytearray
- memoryview

* bytes
=> The bytes() function returns a bytes object. It can convert objects into bytes objects, or create empty bytes object of the specified size. bytes is a inmutable.

* bytearray
=> The bytearray type is a mutable sequence of integers in the range between 0 and 255.

"""

# must me 0 to 255
mylist = [1,2,3,4,5,6,7,100, 122, 255];
b = bytes(mylist);
# print(type(b)); # Type <class 'bytes'>
# print(b[8])


# Bytearray
mylist2 = [23, 42, 54, 76, 24, 27, 22, 75, 77];
c = bytearray(mylist2);
# print(type(c)); # <class 'bytearray'>
c[0] = 11;
```

## None Type
```py
"""  
** Python None Keyword
- The none keyword is used to define a null value, or no value at all. none is not the same as 0, False, or an empty string. None is a data type of ites own (NoneType) and only None can be None.
"""
# Declear a None variable
x = None;
print(x);

# Type check
print(type(x)) #<class 'NoneType'>


if x:
    print("Do You think None is True")
elif x is False:
    print("Do You think None is False")
else:
    print("None is not True, or False, None is Just None....");
```

## Type Casting
```py

- [Integers]:-
x = int(1);
y = int(2.5);
z = int("22");
print(x); # 1
print(y); # 2
print(z); # 22

- [Floats]:-
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("22.44") # w will be 22.44
print(x);
print(y);
print(z);
print(w);

- [Strings]:-
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
w = str("33.33"); # w will be '33.33'
print(x);
print(y);
print(z);
print(w);


- Short Project-1
num1 = input("Enter first number ");
num2 = input("Enter second number ");
sum = int(num1) + int(num2);
print("The Sum is", sum);

- Short Project-2
base = int(input("Enter Base = "));
hight = int(input("Enter Hight = "));
area = 0.5 * base * hight;
print(area)
```

## Python Math
```py
""" 
Math Function
** Buil-in Math Function
** Math Module
"""

# ** Buil-in Math Function
maxnum = max(20, 10);
minnum = min(20, 10);
positivenum = abs(-7.25)
power = pow(3,3);
print(power)

# ** Math Modules Function
import math;
x = math.sqrt(64); # 8 
y = math.ceil(3.56); # 4
z = math.floor(3.56); # 3
p = math.pi # 3.141592653589793
```

## Variable Type Check
```py
# Type Function
num = 29.5;
name = "X";
isPass = False;
print(type(name));
print(type(num));
print(type(isPass));
```

## Python Operators
```py
""" 
** Python Operators
- Python Math Operators
- Python Assignment Operators
- Python Comparison Operators
- Python Logical Operators
- Python Identity Operators
- Python Membership Operators
"""

# Python Arithmetic Operators
print(10 + 20);
print(20 - 10);
print(10 * 2);
print(20 / 5);
print(20 % 3);
print(10 ** 2);
print(100 // 3);

#  Python Assignment Operators
x = 5;
x += 10;
x -= 10;
x *= 2;
x **= 2;
x /= 5;
x %= 3;
y = 3;
y &= 3;
y |= 3;
y ^= 3
y >>= 3
y <<= 3

# Python Comparison Operators
a = 5;
b = 10;
print(a == b);
print(a != b);
print(a < b);
print(a > b);
print(a >= b);
print(a <= b);

# Python Logical Operators
# and operator Returns True if both statements are true
# or operator Returns True if one of statements is true
# Not operator Returns Reverse the result,


p = 10;
q = 11;
m = 20;
n = 25;
print(p > q and m < n )
print(p > q or m < n )
print(not(p > q and m < n))
print(not(p > q or m < n));

# Python Identity Operators
i = 22;
l = 22;
print(i is l); # True
print(i is  not l); # False

# Python Membership Operators
arr = ["a", "b", "c"];
print("a" in arr); # True
print("a" not in arr) # False
print("d" not in arr) # True
```

## Python Logical Operators
```py
- and Returns True if both statements are true.
- or Returns True if one of the statements is true.
- not Reverse the result, returns False if the result is true.

- and
num1 = 20;
num2 = 10;
num3 = 30;
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2);
else:
    print(num3)


- or
# vowel => a, e, i, o, u
word = "a";
if (word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u'):
    print("This word is vowel");
else: 
    print("This word is consonant");


- not
isPass = True;
if not isPass:
    print("Bye");
else:
    print("Hi");

if not 11 % 2 == 0:
    print("not zero");
else:
    print("00");
```

## Python Swap Variable
```py
# variable Swap
a = 10;
b = 20;
print(a,b);
a,b = b,a;
print(a,b);

mylist1 = [1,2,3];
mylist2 = [4,5,6];
print(mylist1, mylist2);
mylist1,mylist2 = mylist2,mylist1 
print(mylist1, mylist2);
```

## If, Else Statement
```py
** Python Conditions and If Statements
- Equals: a == b
- Not Equals: a != b
- Less than: a < b
- Less than or equal to: a <= b
- Greater than: a > b
- Greater than or equal to: a >= b

number = int(input("Enter Your Number "))
if number > 10:
    print("Number is bigger than 10");
else:
    print("This Number is smaller than 10");


mark = 40;
if mark>= 33:
    print("Pass");
else:
    print("Fail");


a = 10;
b = 10;
if a < b:
    print("B is greater than a");
elif a==b:
    print("A and B equal number");
else:
    print("A is greater than b");


if 7> 3:
    if 7> 5:
        print("Hi");
else: 
    print("Bye");


x = 10;
y = 15;
z = 12;
if x > y and x > z:
    print("X is bigger number");
elif y > z and y > z:
    print("Y is bigger number");
else:
    print("Z is bigger number");
```

## Ternary Operator
```py
- Short Hand if else
a = 10
b = 300;
print("A") if a > b else print("B");

- Short Hand multiple check 
a = 300;
b = 300;
print ("A") if a > b else print("==") if a == b else print("B"); 


a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
```

## Letter Grade Program
```py
marks = int(input("Enter Your Marks = "));
if marks >= 80 and marks <= 100:
    print("A+");
elif marks >= 70 and marks <=79:
    print("A");
elif marks >= 60 and marks <= 69:
    print("A-");
elif marks >= 50 and marks <= 59:
    print("B");
elif marks >= 40 and marks < 49:
    print("C");
elif marks >= 33 and marks < 39:
    print("D");
else:
    print("Sorry Fail....");
```

## Python Loop
- Python has two primitive loop commands:
    - while Loop
    - for loop
```py

""" 
While Loop
1. koto taka start hoba
2. condition ar moda boltahoba koto porjonto cholba
3. koto kora barba.
"""

i = 1;
while i <= 6:
    print(i)
    i = i + 1;

i = 2;
while i <= 100:
    print(i);
    i = i +2;

# Print only odd number
i = 1;
while i < 10:
    if i % 2 != 0:
        print(i)
    i +=1;

# Print only Even number
i = 1;
while i < 10:
    if i % 2 == 0:
        print(i)
    i +=1;

# number sum
sum = 0;
i = 0;
while i <= 9:
    sum = sum + i
    i +=1;
print(sum);


""" 
** Python For Loops
- A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
- This is less like the for keyword in other programming language, and works more like an iterator method as found in other object-orientated programming languages.
"""

# Loop is a string
for x in "bangladesh":
    print(x);

# Loop is a list
for x in [10, 20, 30, 40]:
    print(x); 


# Loop is a number
for x in range(0, 5):
    print(x);


# list loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x);

# range() function defaults to 0 as a starting value,
for x in range(6):
  print(x)

# range(_, _, 2) loop increment sequence with 2 (default is 1);
for x in range(0, 10,3):
    print(x);

# sum 
sum = 0;
for x in range(0, 10):
    sum = sum + x;

print(sum)

#  Nested Loops
color = ["red", "big", "tasty"];
fruits = ["apple", "banana", "cherry"]
for x in color:
    print(x)
    for y in fruits:
        print(x, y);
```


## Break and Continue in Loop
```py
# break and continue

# the break statement we cna stop the loop even if the while condition is true
i = 1;
while i <=20:
    if i == 10:
        break
    print(i)
    i= i+1

# The continue statement we can stop the current iteration, and continue with the next:
i = 0;
while i <10:
    i +=1
    if i % 2 == 0:
        continue
    print(i);
```


## Python List
```py
# Python List 
programLanguage = ["C","C++", "JAVA", "Python", "JavaScript", "Swift", "PHP", "Ruby"];
print(programLanguage);

# list length
print(len(programLanguage));

# List Items
"""
- List items oar ordered, changeable, and allow duplicate values.
- List items are indexed, the first item has index [0], the second item has index [1] ect.
- Allow Duplicates
- To determine how many items a list has, use the len() function:
- <class 'list'>
"""
list1 = ["apple", "banana", "cherry"];
list2 = [1, 5, 7, 9, 3];
list3 = [True, False, False];

# Create new List
thislist = list(("apple", "banana", "cherry"));
print(thislist)

```

## Python List All Method
```py

** Python List Methods
- append() 
- clear()
- copy()
- count()
- extend()
- index()
- insert()
- pop()
- remove()
- reverse()
- sort()
```


## Python List Oparation
```py
# Python List 

# - Python list access 
programLanguage = ["C","C++", "JAVA", "Python", "JavaScript", "Swift", "PHP", "Ruby"];
print(programLanguage[4]);
print(programLanguage[-4]);


# Range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
listslice = thislist[1:3]; #['banana', 'cherry']
listslice2 = thislist[:4]; #['apple', 'banana', 'cherry', 'orange']
listslice3 = thislist[4:]; #['kiwi', 'melon', 'mango']
print(listslice3);

# Check if Item Exists
if "Python" in programLanguage:
    print("Yes, 'Python is in the progrome list'");


# Change item value
programLanguage = ["C","C++", "JAVA", "Python", "JavaScript", "Swift", "PHP", "Ruby"];
programLanguage[1] = "C#";
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist);

# list.count() method return the number of times the value "x" appears in the list
# count() method list ar moda item ta koy bar asa tar total return kora.
points = [1, 9, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x) # result => 3
```


## Python List Add
```py
# Append Items
# just single one append one time.
# append method add kora last index a
thislist = ["apple", "banana", "cherry", "orange"];
thislist.append("kiwi");
print(thislist);

# Multiple Items Add in a List
fruits = ["apple","charry","orange"]
fruits.extend(("banana","guava","rasbarrry"))
print(fruits)


# Insert Items with out any replace element.
# insert expected 2 arguments, 1-index no, 2-item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"];
thislist.insert(len(thislist), "watermelon");
thislist.insert(len(thislist), "potato");
print(thislist);

# To append elements from another list to the current list, use the extend() method.
name = ["a", "b", "c", "d"];
name2 = ["e", 'f', "g", "h"];
name.extend(name2);
print(name)
```

## Python Remove List
```py

""" 
** Remove Specified Item
- remove() method not return remove item;
- remove() method not found item this time give a error.
"""
programLanguage = ["C","C++", "JAVA", "Python", "JavaScript", "Swift", "PHP", "Ruby"];
print(programLanguage);
programLanguage.remove("Python");
# programLanguage.remove("swift"); # Error.
print(programLanguage);



""" 
** Remove Specified Index
- the pop() method removes the specified index.
- pop() method give remove item
- pop() mehtod need a remove index
- pop() method give error jodi index list ar moda na taka.
- pop() method with out any index number this time remove last index in the list
"""
programLanguage = ["C","C++", "JAVA", "Python", "JavaScript", "Swift", "PHP", "Ruby"];
x = programLanguage.pop(0);
y = programLanguage.pop();
print(programLanguage)


""" 
** The del keyword also removes the specified index
- del the first item { del thislist[0] }
- the del keyword can also delete the list completely.
- list is not exists.
"""
programLanguage = ["C","C++", "JAVA", "Python", "JavaScript", "Swift", "PHP", "Ruby"];
del programLanguage[0];
del programLanguage[1];
del programLanguage
print(programLanguage)


""" 
** The clear() method empties the list.
- The list still remains, but it has no content.
- all items remove
"""
programLanguage = ["C","C++", "JAVA", "Python", "JavaScript", "Swift", "PHP", "Ruby"];
programLanguage.clear();
print(programLanguage)
```


## Python List-Loops
```py
# Python List Loops
programLanguage = ["C","C++", "JAVA", "Python", "JavaScript", "Swift", "PHP", "Ruby"];

# While Loop 
i = 0;
while i < len(programLanguage):
    print(programLanguage[i])
    i+=1;

# For Loop
programLanguage = ["C","C++", "JAVA", "Python", "JavaScript", "Swift", "PHP", "Ruby"];
for x in programLanguage:
    print(x)

# Print all items by referring to their index number
# Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
```

## List More Method
```py
"""
** List Sort Method 
** List reverse Order
** Copy a list
** Index item in a list
"""
# Sort the list numerically:
points = [1, 4, 2, 9, 10, 11, 7, 8, 9, 3, 1]
points.sort();
print(points);

# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list descending order
points = [1, 4, 2, 9, 10, 11, 7, 8, 9, 3, 1]
points.sort(reverse=True);
print(points)

#  Case-insensitive sort of the list
thislist = ['a', "B", 'c', 'd', "E", "G"]
thislist.sort(key=str.lower);
print(thislist)

# The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist);

# Make a copy of a list with the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Make a copy of a list with the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Add two List
# Join two Lists useing the + operator. 
list1 = [1,2,3,4];
list2 = [5,6,7,8];
list3 = list1 + list2
print(list3)

#  use extend() method to add list2 at the end of list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# use extend() method multiple items add in a List
fruits = ["apple","charry","orange"]
fruits.extend(("banana","guava","rasbarrry"))
print(fruits); 

# Another wat to join two lists is by appending all the items from list2 into list1 one by one.
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#  Mulple list join
list1 = [1,2];
list2 = [3,4];
list3 = [5,6];
list4 = [7,8];
list1 = [*list1, *list2, *list3, *list4]
print(list1)


# List index() method
# The index() method return the position at the first find item of the specified value. 
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
fruits = [4, 55, 64, 32, 16, 32]
y = fruits.index(16)
print(x);
print(y);

```


## Python Range Function
```py
""" 
** Python range() function
- Create a sequence of number from 0 to 5, range(6)
- The range() function returns a sequence of number, starting from 0 by default, and increments by 1 (by default), and steps before a specified number.

* Parameter values
- start => Optional. An integer number specifying at which position to start. Default is 0
- stop => Required. An integer number specifying at which position to stop (not included).
- step => Optional. An integer number specifying the incrementation. Default is 1
"""
x = list(range(3, 20,  2))
num = list(range(10, 100, 10))

# range() function use for loop using a create a list
num = range(0, 20, 5);
for x in num:
    print(x); 
```

## Python Problem Slove
```py
""" 
** Math Series Using Python
=> 1+2+3+4+...+n
"""
n = int(input("Enter the last number : "));
sum = 0;
for x in range(1, n+1, 1):
    sum+=x;
print(sum);


# Guess Number Game.
from random import randint;
count = 0;
randomNumber = randint(1,5);
for x in range(1, 6):
    guessNumber = int(input("Enter your guess between 1 to 5 : "));
    count += 1;
    if(guessNumber == randomNumber):
        print(f"You have won try number {count}")
        break
    elif (count == 5):
        print("Sorry you loss")
    elif (guessNumber > randomNumber):
        print("Sorry random number is small")
    elif (guessNumber < randomNumber):
        print("Sorry random number is big")
```

## Python Dictionaries
```py
""" 
** Python Dictionaris
- Dictionaries are used to store data values in key:value pairs.
- A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
- Dictionaries are written with curly brackets, and have keys and values.
- the items have a defined order, and that order will not change.
- Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
- Dictionaries cannot have two items with the same key.
- The update() method will update the dictionary with the items from the given argument.The argument must be a dictionary, or an iterable object with key:value pairs.
"""
** Python Dictionary Method
- clear()
- copy()
- get()
- items()
- keys()
- pop()
- popitem()
- update()
- values()

#  Declear a Dictionarie
thisdict = {
    "brand" : "Ford",
    "year" : 1967,
    "model" : "Mustage",
    "colors": ["red", "white", "blue"]
};
print(thisdict);

# Access a Dictionarie value
brand = thisdict["brand"];
print(brand);

# Dictionaries Length Check
length = len(thisdict);
print(length)

#  Dictionaries Type Check
print(type (thisdict)); # <class 'dict'>

# Create a dict
person = dict(name = "Joy", age = 20, country = "bangladesh");
print(person);

# Duplicate Not Allow
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
```

## Python Dictionary Access Method
```py
thisdict = {
    "brand" : "Ford",
    "year" : 1967,
    "model" : "Mustage",
    "colors": ["red", "white", "blue"]
};

#  Access Dictionary
year = thisdict["year"];
colors = thisdict.get("colors");

# The keys() method will return a list of all the keys in the dictionary.
keys = thisdict.keys();

# The values() method will return a list of all the values in the dictionary.
values = thisdict.values();

# The items() method will return each item in a dictionary, as tuples in a list.
allproperty = thisdict.items();
print(allproperty)

# Check If keys Exists
if "year" in thisdict:
    print("Yes, 'year' is one of the keys in the dictionary");
```


## Python Dictionary add change remove Method
```py
thisdict = {
    "brand" : "Ford",
    "year" : 1967,
    "model" : "Mustage",
    "colors": ["red", "white", "blue"]
};

# the copy() method copy full dictionary.
copydict = thisdict.copy();
mydict = dict(thisdict);

# Change Values
thisdict["year"] = 2002;

# Adding Items
thisdict["instock"] = True;

# Update Dictionary and add new propertys.
thisdict.update({"brand": "Tata", "model": "Tata Altroz", "sell": 3500});


#  Remove Dictionary Items
thisdict.pop("model"); # modle item remove
# The popitem() method removes the last inserted item
thisdict.popitem(); # last item remove.


# del keyword removes the item with the specified key name
del thisdict["colors"]; # colors property delete

#  The clear() method empties the dictionary
thisdict.clear();
print(thisdict)

# The del keyword can also delete the dictionary completely:
del thisdict;
# print(thisdict) #NameError: name 'thisdict' is not defined   
```

## Python Dictionary Loop
```py
thisdict = {
    "brand" : "Ford",
    "year" : 1967,
    "model" : "Mustage",
    "colors": ["red", "white", "blue"]
};

# Loop through a dictionary
for x in thisdict:
    print(f"{x} : {thisdict[x]}");

# key() method to return the keys of a dictionary
for x in thisdict.keys():
  print(x)

# values() method to return the values of a dictionary
for x in thisdict.values():
  print(x)

# both keys and values, by using the items() method:
for x, y in thisdict.items():
   print(x,y)
```


## Python Dictionary Other Method
```py
# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
};

# Other Way
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily2 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Access Nested dictionaries
name= myfamily["child2"]["name"];
print(name)

``` 

## Python Tuple
```py
"""
** Python Tuples
- Tuples are used to store multiple items in a single variable.
- Tuple items are ordered, unchangeable, and allow duplicate values.
-Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
"""

# Create a Tuple
mytuple = ("apple", "banana", "cherry");

# Create a tuple() Constructor
mytuple2 = tuple(("apple", "banana", "cherry"))

# Tuple Length
lenght = len(mytuple);

# Create Tuple With One Item
oneitem = ("apple",)
nottuple = ("apple") # not tuple

# Tuple Type
typetuple = type(mytuple);

# Access Tuple
thistuple = mytuple[0];
thistuple2 = mytuple[-2]; #banana

# Range of Index
mytuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
x = mytuple3[4:];
y = mytuple3[:4];
z = mytuple3[2:4];

#  Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False);

# Mixed Typle
tuple1 = ("abc", 34, True, 40, "male");

# Allow duplicates values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")


# Check if Item Exists
if "kiwi" in mytuple3:
    print("Yes");
else:
    print("No")

# del keyword can delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


# Change Tuple Values
# Tuples are unchangeable, or immutable as it also is called.
a = ("apple", "banana", "cherry")
b = list(a);
b[1] = 'kiwi';
b.append('orange');
a = tuple(b);

# Remove Tuple
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Tuples Unpack
# we normally assign values to it. This is called "packing" a tuple
fruits = ("apple", "banana", "cherry");
(a,b,c) = fruits;

fruits2 = ("apple", "banana", "cherry", "orange", "kiwi");
# * tuple convert a list and access all tuples items.
(*a, b, c) = fruits2;

# Loop Through a Tuple
for i in range(len(fruits2)):
    print(i, fruits2[i]);

# Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2;

# Multiply Tuples
fruits = ("apple", "banana", "cherry", "apple")
mytuple = fruits * 2

# Tuple Methods
- count()
- index()

# count() methods
c = fruits.count("apple");
print(c)
# index() methods
i = fruits.index("apple");
print(i)
```

## Python Set
```py
"""
** Python Sets
- Sets are used to store multiple items in a single variable.
- Set items are unchangeable, and do not allow duplicate values.
- Once a set is created, you cannot change its items, but you can add new items.
- Set are unordered,
- Unordered means that the items in a set do not have a defined order.
- Sets are written with curly brackets.
- Sets are unordered, so you cannot be sure in which order the items will appear.
- To add one item to a set use the add() method.
- To add items from another set into the current set, use the update() method
- To remove an item in a set, use the remove(), or the discard() method.
- Remove a random item by using the pop() method
- The union() method returns a new set with all items from both sets
"""

# Create a Set
myset = {"A", "C", "B"}; #{'A', 'B', 'C'}

# Create set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets

# Duplicates Not Allowed
dup = {"a", "c", "d", "a", "a", "b", "f", "k", "g", }; # duplicate a allow just 1 time.

# Set Length Check
length = len(dup);

# The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2, 0, False, "",}

# Set Data Types
set1 = {"apple", "banana", "cherry"};
set2 = {1, 5, 7, 9, 3};
set3 = {True, False, False};

# copy() method
thisset = {"apple", "banana", "cherry"};
my = thisset.copy();

# Loop Through in a Set
for x in set1:
    print(x);

# If Statement Check
thisset = {"apple", "banana", "cherry"};
if "banana" in thisset:
    print("Yes")

# Add Item in a Set
# add() method recived 1 argument.
thisset =  {"apple", "banana", "cherry"};
thisset.add("orange",);

# Update Method use add Set in a Set 
firstset = {"apple", "banana", "cherry"};
secondset = {"pineapple", "mango", "papaya"};
firstset.update(secondset);

# Add Any Iterable
a =  {"apple", "banana", "cherry"};
b = ("kiwi", "orange");
c = ['potato'];
a.update(b, c);

# Remove Set Items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") # If the item to remove does not exist, remove() will raise an error.

# remove item using discard
thisset = {"apple", "banana", "cherry"}
thisset.discard("bananaa") # If the item to remove does not exist, discard() will NOT raise an error.

# random item pop
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()

# Clear Method empty the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()

# del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset

# random item changing tricky
thisset = {"apple", "banana", "cherry"}
x = list(thisset);
x[0] = "kiwi";
thisset = set(x);

# Join Sets
# union() method retrun value.
set1 = {"a", "b" , "c",};
set2 = {1, 2, 3};
set3 = set1.union(set2);

# Keep only the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple", "cherry"}
x.intersection_update(y)
print(x);

** Set All Method
- add()
- clear()
- copy()
- difference()
- difference_update()
- discard()
- intersection()
- intersection_update()
- isdisjoint()
- issubset()
- pop()
- remove()
- union()
- update()
```

## Stack And Queue
```py
""" 
Stack And Queue

** Stack 
- last in first out
    - push
    - pop

** Queue
- first in first out

"""
books = [];
books.append("C");
books.append("C++");
books.append("C#");
books.append("JAVA");
books.append("PHP");
books.append("JavaScript");
books.append("Python");
print(books)
books.pop();
books.pop();
print(books);

from collections import deque;
bank = deque(["A", "B", "C", "D", "E"]);
print(bank)
bank.popleft();
bank.popleft();
print(bank)
```

## Python Function
```py
""" 
** Python Functions
- A function is a block of code which only runs when it is called.
- You can pass data, known as parameters, into a function
- A function can retun data as a result.

* parameters or Arguments?
- The terms parameter and argument can be used for the same thing.
"""

# Create a Function
def my_function():
    print("Hello from a function");
# Call a Function
my_function();

# Arguments pass
def my_name(name):
    print(name);
# call function with argumetns
my_name("Joy");

# This function expects 2 arguments, and gets 2 arguments:
def my_info(fname, lname):
  print(fname + " " + lname)
my_info("Emil", "Refsnes")

# sum two number using a function
def math_sum(num1,num2):
   print(num1 + num2);
math_sum(10, 5);


```

## Python Function More Concepts
```py
""" 
** Arbitrary Arguments, *args
- If you do not know how many arguments that will be passed into your function, add a * before the paramenter name in the function definition.
- This way the function will recive a tuple of arguments, can access the items accordingly.

** Keyword Arguments
- You can also send arguments with the key = value syntax.
- This way the order of the arguments does not matter.

** Default Parameter Value
- If we call the function without argument, it uses the default value.

** Return values
- To let a function return value, use the return statement.

** The pass Statement
- function definitions cannot be empyt, but if you for some reson have a function definition with no content, put in the pass statement to avoid, getting an error.
"""

# Arbitrary Arguments, *args
def my_fun(*kids):
    print(kids[1]);

my_fun("emil", "anis", "sumit");


def my_function(child1, child2, child3):
    print(child1, child2, child3);
my_function(child1="X", child2="Y", child3="Z");


# Default Parameter Value
# If we call the function without argument, it uses the default value.
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Passing a List as an Argument
def my_sum(numbers):
   sum = 0
   for x in numbers:
      sum += x;
   print(sum);
my_sum([10, 20, 30]);

# Return values
# - To let a function return value, use the return statement.
def multiply(num):
   return num * 2;
x = multiply(5);
y = multiply(4);
z = multiply(6);

# The pass Statement
# - function definitions cannot be empyt, but if you for some reson have a function definition with no content, put in the pass statement to avoid, getting an error.
def pass_fun():
   pass;


# Zip Function
# Join Two Tuples together
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
x = zip(a,b);

list1 = ["Joy", "Sumit", "Anis"];
list2 = ["programmer", "CEO", "Teacher"];
y = list(zip(list1, list2));


rolls = [1,2,3,4,5,6,7,8,9,10];
names = ['A', "B", "C", "D", "E", "F", "G", "H", "I", "J"];
x = list(zip(rolls, names, "ABABABABAB"));
print(x);
```

## Python xargs & xxargs
```py
# xargs
def student (*info):
    print(info[0], info[1], info[2])
student(101, "Joy", True);

def sum(*numbers):
    sum = 0
    for x in numbers:
        sum += x;
    print(sum);
sum(10, 20, 30, 40, 50);
sum(10, 50);

# xxargs
def person(**info):
    print(info); #{'name': 'X', 'role': 'user', 'id': 101}
person(name="X", role="user", id=101);
```

## Python Lambda and Recursion Function
```py
# Python Lambda Function
""" 
- A lambda function is a small anonymous function
- A lambda function can take any number of arguments, can can only have one expression.

Why Use Lambda Functions?
- The power of lambda is better shown when you use them as an anonymous function inside another function.
- Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
"""
# anonymous function
p = lambda x, b : x + b;
q = p(10, 20);
print(q);

# function return another lambda fuction
def myfunc(n):
  return lambda a = 2 : a * n;
x = myfunc(5);
print(x())
print(x(10))

sum = lambda num1, num2 : num1 + num2;
print(sum(10, 10));

# myfunc recived cb as a function
def myfunc(n, cb):
    print(n, cb)
    x = cb(n)
    print(x)
myfunc(50, lambda x : x *2);


# Recursion
def recursion(num):
    if (num > 0):
        result = num + recursion(num - 1)
        print(result);
    else:
        result = 0;
    return result;
x = recursion(6)
```

## Python Map & Filter Function
```py
- Python map() function
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

# Syntax
# map(function, iterables)

mylist = [1,2,3,4,5];
def square(x):
    return x * x;

result = list(map(square, mylist));
print(result)

def myfunc(n):
  return len(n)
x = tuple(map(myfunc, ('apple', 'banana', 'cherry')));
print(x)


- Python filter() Function
ages = [5, 12, 17, 18, 24, 32];

def myFunc (x):
    if (x < 18):
        return False;
    else:
        return True;

result = list(filter(myFunc, ages));
print(result);
```

## Python Class And Objects
```py
""" 
** Python  Class And Objects
- python is an object oriented programming language.
- Almost everthing in Python is an object, with its properties and methods.
- A class is like an object constructor, or a "Blueprint" for creating object.

* Create a class
- To create a class, use the keyword "class"
- The __init__() function is called automatically every time the class is being used to create a new object.
"""

# Create a Class
class Myclass:
    x = 5;

# Create object 
p1 = Myclass();


# The __init__() function is called automatically every time the class is being used to create a new object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

x = Person("John", 40);

class Car:
    def __init__(self, name, year, model):
        self.name = name
        self.year = year
        self.model = model
    def myfun(self):
        print(f"{self.name} {self.year} {self.model} ")    
car1 = Car("Frod", 2020, "Anything");
car1.myfun()


# Modify Object Properties
car1.year = 2023;
car1.myfun()

# Delete Object Properties
del car1.name;
car1.myfun()

# Delete Objects
del car1

# Pass Statement
class Person:
  pass
```

## Class Inheritance
```py
"""  
** Python Inheritance
- Inheritance allows us to define a class that inherits all the methods and properties from another class.
- Parent class is the class being inherited from, also called base class.
- Child class is the class that inherits from another class, also called derived class.
"""

# Create a Parent Class
class Person:
    def __init__(self, id, name, age):
        self.id = id;
        self.name = name;
        self.age = age;
    def printMe(self, other):
        print(other, self.id, self.name, self.age);

x = Person(101, "X", 25);


# Create a Child Class
class Student(Person):
    role = "Student";

s1 = Student(1005, "Anis", 17);
s1.printMe("Hi");

# Create another Child Class
class Teacher(Person):
    # Same Work
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self.role= "Teacher"

t1 = Teacher(5022,'Sumit', 36);
t1.printMe("Hi Sir")
```

## Python Iterators
```py
""" 
** Python Iterators
- An iterator is an object that contains a countable number of values.
- An iterator is a object that can be iterated upen, meaning that your can traverse through all the values.

# Iterator vs Iterable
    - Iterator => পুনরাবৃত্তিকারী
    - Iterable => পুনরাবৃত্তিযোগ্য
"""

mylist = ["A", "B", "C", "D", "E", "F"];
x = iter(mylist);
print(next(x));
print(next(x));
print(next(x));

mylist2 = [1,2,3,4,5,6,7];
it = iter(mylist2);
a = it.__next__();
b = it.__next__();
c = it.__next__();
d = it.__next__();
print(a+b+c+d);

# String Interable
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
```

## Python Scope
```py
""" 
** Python Scope
- A variable is only available from inside the region it is created. This is called scope.

* Local Scope
- A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

* Function inside Function
- As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function

* Global Scope
- A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.

* Global Keyword
- use the global keyword if you want to make a change to a global variable inside a function.
"""

# Local Scope
def myfunc():
  x = 300
  #This x acces only hare
  print(x)

# print(x); # "x" is not defined hare. 
myfunc()


# Function inside Function
# - As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc() 

# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
x = 300

def myfunc():
  print(x)

myfunc()
print(x)


# Global Keyword
# use the global keyword if you want to make a change to a global variable inside a function.
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)
```

## Python Date
```py
""" 
** Python Date Time
- A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
"""

# import datetime now.
import datetime;
x = datetime.datetime.now();
print(x) # date date time now.
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%B"))


** A referance of all the legal format codes
- %a Weekday, short version 
- %A Weekday, full version
- %w Weekday as a number 0-6, 0 is Sunday
- %d	Day of month 01-31
- %b	Month name, short version
- %B	Month name, full version
- %m	Month as a number 01-12
- %y	Year, short version, without century
- %Y	Year, full version
- %H	Hour 00-23		
- %I	Hour 00-12		
- %p	AM/PM	
- %M	Minute 00-59		
- %S	Second 00-59	
- %f	Microsecond 000000-999999
- %z	UTC offset	
- %Z	Timezone	
- %j	Day number of year 001-366
- %U	Week number of year, Sunday as the first day of week, 00-53	
- %W	Week number of year, Monday as the first day of week, 00-53	
- %c	Local version of date and time
- %C	Century	
- %x	Local version of date	
- %X	Local version of time

```

## Python RegEx
```py
""" 
** Python RegEx
- A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
- RegEx can be used to check if a string contains the specified search pattern.

** RegEx Module
- Python has a built-in package called re, which can be used to work with Regular Expressions.
- Import the re module
"""

# Import the re module
import re;

** All RegEx Function
- findall
- search
- split
- sub


- findall [a-m]
text = "my name is joy.";
pattern = "[a-m]";
f = re.findall(pattern, text);
print(f); #['m', 'a', 'm', 'e', 'i', 'j']

- findall digit characters 
txt = "That will be 59 dollars and 5k Tk"
pattern = "\d"
#Find all digit characters:
x = re.findall(pattern, txt);
print(x) #['5', '9', '5']

- first characters find
text = "my name is joy.";
pattern = "^my";
x = re.findall(pattern, text);
print(x); #['my']

- last characters find
text = "Hello World";
pattern = "World$";
x = re.findall(pattern, text);
print(x); #['World']

- Either or
txt = "The rain in Bangladesh falls mainly in the plain! Japan";
pattern = "Spain|Japan|Bangladesh";
x = re.findall(pattern, txt);
print(x);
```

## Python Try Except
```py
** Python Try Except
- The "try" block lets you test a block of code for errors.
- The "except" block lets you handle the error.
- The "else" block lets you execute code when there is no error.
- The 'finally' block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling
try:
    print(x); # x is not defined
except:
    print("An exeption occurred");

# Many Exceptions
try:
  print(x)
except NameError:
  print("Variable is not defined")
except:
  print("Something else went wrong")

# Else keyword
try:
  print("Hello")
  print(a)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

- The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print("H")
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
```

## Python Debugging
- Debugging means the complete control over the program execution. Developers use debugging to overcome program from any bad issues. So debugging is a healthier process for the program and keeps the diseases bugs far away. Python also allows developers to debug the programs using pdb module that comes with standard Python by default. We just need to import pdb module in the Python script.

## Python File handling
```py
** Python File Open
- File handling is an important part of any web application.
- Python has several functions for creating, reading, updating, and deleting files.

** File Handling
- The key function for working with files in Python is the open() function.
- The open() function takes two parameters; filename, and mode.
- There are four different methods (modes) for opening a file

** Four methods
    - "r" Read
    - "a" Append
    - "w" Write
    - "x" Create

    - In addition you can specify if the file should be handled as binary or text mode
        - "t" Text
        - "b" Binary

** Syntax
f = open("demo.txt");
f = open("demo.txt", "rt"); #Because "r" for read, and "t" for text are the default values, you do not need to specify them.
```

## Python File Read
```py
- To open the file, use the built-in open() function.
- The open() function returns a file object, which has a read() method for reading the content of the file

- read() method
f = open("demo.txt", "r");
print(f.read());
print(f.read(5));

- readline() method
f = open("demo.txt", "r")
# Read one line of the file
# By calling readline() two times, you can read the two first lines
print(f.readline());
print(f.readline());

# Print all line.
f = open("demo.txt", "r")
for x in f:
  print(x)

- It is a good practice to always close the file when you are done with it.
f.close()
```

## Python File Write 
```py
** Python File Write
- Write to an Existing File
- To write to an existing file, you must add a parameter to the open() function
    - "a" - Append  - will append to the end of the file
    - "w" - Write - will overwrite any existing content

- Create a New File
    - "x" - Create - will create a file, returns an error if the file exist

    - "a" - Append - will create a file if the specified file does not exist

    - "w" - Write - will create a file if the specified file does not exist

f = open("myfile.txt", "x")
f = open("myfile.txt", "a")
f = open("myfile.txt", "w")

# create new file and write
f = open("demo2.txt", "w");
f.write("Create a new File and add this content.");
print(f.writable()) # check readable check
f.close();

# append new text
f = open("demo2.txt", "a");
f.write(" Now the file add new content!");
print(f.writable()) # check readable check
f.close();

f = open("demo2.txt", "r");
print(f.readable()) # check readable check
content = f.read();
print(content);
```

## Python File Delete
```py

** Python Delete File

- Delete a File
    - To delete a file, you must import the OS module, and run its os.remove() function

# import os
import os
# remove file
os.remove("myfile.txt")

# Check if file Exist
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")

# Delete Folder
os.rmdir("folder")
```