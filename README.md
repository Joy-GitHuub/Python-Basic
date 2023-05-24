

1. What is Python?
ans:- Python is a interpreted, object-oriented, high-level programmin language with dynamic semantics.


2. Why is choose python
Ans:- Python has a simple syntax and hence is easy to understand and learn. Thus, making to popular pick when it comes to programmin languages. As you can see, the same code can be written using fewer lines in Python. Thus making it much simpler to use on many levels.

3. Where is Python Used?
Ans:- Python is used in everything from machine learning to building websites and software testing. Python is used across a wide variety of industries. Of course, the most common areas where python language is used are for building mobile web deskot applications. 


4. Python for Multi-purpose usage?
Ans:- a.{Webapp development} b.{Quick prototyping} c.{Scripting} d.{Data science} e.{Databse programming}

### Python Print
```py
1. print("Hello Python World");
```

### Python Comment
```py
# Python Single line Comment

""" Multiple line Comment
1. Python Easy to learn
 """
```

### Python multiple line print
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

### Python Variable

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

### Python Data Type
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



### Numerical Operation
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



### Python String
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


### Python String Method
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

### String Format() Method
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

### Python Booleans
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

### Binary Types
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

### None Type
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

### Type Casting
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

### Python Math
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

### Variable Type Check
```py
# Type Function
num = 29.5;
name = "X";
isPass = False;
print(type(name));
print(type(num));
print(type(isPass));
```

### Python Operators
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

### Python Logical Operators
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

### Python Swap Variable
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

### If, Else Statement
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

### Ternary Operator
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

### Letter Grade Program
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

### Python Loop
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


### Break and Continue in Loop
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


### Python List
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

### Python List All Method
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


### Python List Oparation
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


### Python List Add
```py
# Append Items
# just single one append one time.
# append method add kora last index a
thislist = ["apple", "banana", "cherry", "orange"];
thislist.append("kiwi");
print(thislist);


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

### Python Remove List
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


### Python List-Loops
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

### List More Method
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


### Python Range Function
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

### Python Problem Slove
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

### Python Dictionaries
```py
""" 
** Python Dictionaris
- Dictionaries are used to store data values in key:value pair
- A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
- duplicates Not Allowed
- Dictionaries cannot have two items with the same key
"""
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
```


### Python Dictionary Access Method
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


### Python Dictionary add change remove Method
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

### Python Dictionary Loop
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


### Python Dictionary Other Method
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

### Python Tuple
```py
# Tuple Declear
""" 
** Tuple Declear
- Tuples are used to store multiple items in a single variable.
- A tuple is a collection which is ordered and unchangeable.
- Tuple items are ordered, unchangebale, and allow duplicate values.

"""

# Create Tuple
name = (
    "Joy", "Anisul", "Rabeya", "Nishat", "Sumit", "Nahim",
);

# Allow duplicates values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")

# Tuple Length
length = len(thistuple);

# Create Tuple with one Item
oneitem = ("apple");
print(type (oneitem)) # Type not a typle this type is str

#  Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False);

# Mixed Typle
tuple1 = ("abc", 34, True, 40, "male")

# Create Tuple() constructor
thistuple = tuple(("apple", "banana", "cherry"))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# Access Typle Items
firstitem = thistuple[0];

# Range of Indexes
mytuple = thistuple[3:];
mytuple = thistuple[:3];
mytuple = thistuple[2:5];

# Check if item Exists
if 'banana' in thistuple:
    print("Yes, 'banana' is in the fruits tuple");


# Update Tuples
x = ("Apple", "Banana", "Cherry");
y = list(x);
y.append("Kiwi");
x = tuple(y);

# Add Items in Tuples
x = ("Apple", "Banana", "Cherry");
y = list(x);
y.append("Kiwi");
x = tuple(y);

# Add tuple to a tuple
a = ("apple", "banana", "cherry")
b = ("orange",);
a+=b;
print(a,b)


# Remove Items in a Tuple
t = ("apple", "banana", "cherry");
l = list(t);
l.remove("apple");
t = tuple(l);

# Delete Full Tuples
thistuple = ("apple", "banana", "cherry")
del thistuple

# Using Asterisk* in Tuple
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(a,b,*c,) =  fruits;
(a,*b,c,) =  fruits;

# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
tuple1 = ("a", "b" , "c")
tuple2 = tuple1 * 2
print(tuple2)

# Tuples Count() method
thistuple = (1, 3, 5, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

# Tuple index() method
# TH eindex() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
```

### Python Set
```py
""" 
** Python Sets
- Sets are used to store multiple items in a single variable.
- Set items are unchangeable, and do not allow duplicate values.
- Once a set is created, you cannot change its items, but you can add new items.
"""
# Create a Set
thisset = {"X", "Y", "Z"};

# Set Type
typeset = type(thisset); #<class 'set'>

# Duplicates Not Allowed
# True and 1 is considered the same value:
duplicateset = {"apple", "banana", "cherry", "apple"}
thisset = {"apple", "banana", "cherry", True, 1, 2}

# Get the lenght of a Set
length = len(thisset);

# Create set() Constructor
cre = set(("A", "C", "B", "D"));

# Loop through the  set
for x in cre:
    print(x);

# If statement in set
if "B" in cre:
    print("Yes");

# Add new Items
cre.add("J");

# Remove Items
# If the item to remove does not exist, remove() will raise an error.
cre.remove("C");

# discard() method
# If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")

# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry", "kiwi"}
x = thisset.pop()

# The clear() method empties the set:
thisset.clear();

# The del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset

# Update() method use for two set Join
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

# update() method use for set and list join
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist);
```

### Stack And Queue
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

### Python Function
```py
""" 
** Python Function
- In Python a function is defined useing the def keyword
- To call a function, use the function name
- Information can be passed into functions as arguments.
- The terms parameter and argument can be used for the same thing: information that are passed into a function.
- If we call the function wtihout argument, it uses the default value.
"""

# Create a Function
def sum(a,b) :
    return a + b;

a = sum(10, 20);
b = sum(20, 5);
print(a,b);

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
```

### 