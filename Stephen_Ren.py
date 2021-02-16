print("welcome to fortinet")
print("    /|")
print("   /_|")
print("  /__|")
print(" /___|")
print("/____|")

Character_name = "John"
Character_age = 41
print("My name is "+ Character_name + ",today is my birthday and I am an old man")
print("I am ",Character_age, " years old")
Character_name = "Stephen"
print("I really like my name " + Character_name)
print("but I don't like being",Character_age)

print("stephen_\sen")

name = "STEPHEN_REN"
print(name.replace("REN","SAA"))

q=3.13
print(4*(5+1))

print(10 % 3)

print(str(4) + " is my favariate number")

num = -5
print(abs(num))

print(pow(25,2))

print(round(3.14))

help(min)

from math import *
print(sqrt(36))


#aa = input("who are you?:")
#bb = input("how old are you?:")
#print("welcome,"+aa+"!you are "+bb)


#xx = input("number1:")
#yy = input("number2:")

#result = float(xx) + float(yy)
#print(result)


#color = input("Input the color:")
#noun = input("input the noun:")
#celebrity = input("input the celebrity:")

#print("Roses are " + color)
#print(noun + " are blue")
#print("I love " + celebrity)
name = [1,2,3]
friends = ["alex","stephen","john","c2","c3"]
aa = friends.copy()
print(aa)

name = (1,2)
print("---------------------------------")
print(name[0])

aa = [(1,2),(3,4),(5,6)]
print(aa[1])

def say_hi(name):
    print("Hello to you !" + name)

say_hi("stephen")
say_hi("Alex")

def hello(name,age):
    print("hello " + name + ",you are " + age)
    return 33

hello("stephen","41")
hello("rene","39")


def sum(sum):
    print (sum * sum * sum)

sum(3)

is_male = True
is_tall = False

if is_male and is_tall:
    print("you are a male")
elif is_male and not is_tall:
    print("I am tall")
else:
    print("you are not a male")


def max_num(num1,num2,num3):
    if num1 != num2 and num1 == num3:
        return num2
    elif num2 >=num1 and num2 >=num3:
        return num2
    else:
        return num3
print (max_num("a","b","a"))

#aa = float(input("your first number is: "))
#mark = input("your algorithm is: ")
#bb = float(input("your 2nd number is: "))

#def cal(aa,mark,bb):
 #   if mark == "+":

   #   print("your result is: ", aa+bb)

  #  elif mark == "-":
   #    print("your result is: ", aa - bb)
  #  elif mark == "*":

     # print("your result is: ", aa*bb)
  #  elif mark == "/":
   #   print("your result is: ", aa/bb)
  #  else:
   #   print("invalid things")

#cal(aa,mark,bb)

cal = {10:"January",
       "Feb":"February",
      "Mar":"March"}

#print(cal.[10])

i = 1
while(i <= 10):
    print(i)
    i += 1
print("The end")

for letter in "I love you":
    print(letter)

aa = ["a","b","ccccc"]
for a in aa:
    print (a)


    bb = "I love him"
for i in bb:
    print(i)

for count in range(11):
    print(count)

aa = ["a","b","c"]
for count in range (len(aa)):
    print(aa[count])

for i in range(5):
   if i == 0:
    print("lala")

secret_word = "I love you,Rene"
guess = ""
guess_count = 0
guess_limit = 3
guess_out = False
#while (guess != secret_word  and not guess_out):
 #   if guess_count < guess_limit:
  #    guess = input("please say something from your heart: ")
   #   guess_count += 1
    #else:
     #   guess_out = True

#if guess_out:
 # print("you are out")
#else:
 #  print("Kiss you,Mr Ren")

print(2**3)
print("--------------------------------------------")
def func(base_num,power_num):
    result = 1
    for i in range(power_num):
      result = result * base_num
    return result

print(func(3,4))

num_list = [[1,2,3],[4,5,6],[7,8,9]]

for x in range(3):
    for y in range(3):
          print(num_list[x][y])

print("-------------------------------------------")
#for row in num_list:
    #for column in row:
 #       print(row)


"""
def translate(words):
    name = ""
    for i in words:
            if i.lower() in "aeiou":
                if i.isupper() :
                  name = name + "G"
                else:
                   name = name + "g"
            else:
                name = name + i
    return(name)

print(translate(input("Please input your words: ")))

"""
"""

try:
   name =10/0
   num = int(input("please enter your number: "))
   print(num)

except ZeroDivisionError as error01:
   print(error01)
except ValueError as err:
  print(err)

"""
data = open("aa.html","w")
data.write("<p>I am html</p>")

data.close()
print("))))))")
class Student:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height






