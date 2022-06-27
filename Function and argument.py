#==================>> Function <<=================

# 1.) set of instruction with the name is 'Function'
# 2.) Named set of instruction is 'Function'
# Types of function:
#	-> pre defined function(build in function)
#	-> user defined function

#example function:

def function_name():
	"document string"

# function  - action
# action --> inputs with a comma seperation
# ()  --> inputs

#input --> parameter / agruments

#function:
#	1. def is mandatory
#	2. return is not mandatory
#	3. code reusability --> function

 # function programs:

#1.) 
def wish(greetings):     # formal argument
    print(greetings)
wish("Happy new year")    # actual argument

#2)
def invite(name):
    print('Hi',name,'welcome to out python course...')

name = input('Enter your name: ')
invite(name)
  
#3.) 
def square_of_number(no):
    return(no * no)
    
print(square_of_number(5))


# 4.)
def addition(no1,no2):
    return(no1+no2)
    
result = addition(50,100)
print(result)

#5.)
def odd_even(no):
    if no%2==0:
        print("Given no is even number")
    else:
        print("Given no is odd number")
        
number = int(input('enter a number: '))
odd_even(number)

# 6.)

def calculator(no1,no2):
    add = no1+no2
    sub = no1-no2
    mul = no1*no2
    div = no1//no2
    return(add,sub,mul,div)
    
result = calculator(100,20)
print(result)
print(type(result))

for x in result:
    print(x)
  
  
#TYPES OF ARGUMENTS:
#	1. keyword argument
#	2. positional arguments
#	3. default arguments
#	4. variable length arguments
#	5. Keyword length argument


# keyword argument:

def add(no1,no2):    # formal argument
    print(no1+no2)
    
add(20,40)           # actual argument
print('----------------------')

# positional argument:

def wish(name,msg):
    print('Hi',name, msg)
    
wish(name = 'arun',msg = 'welcome our python course')
wish(msg = 'welcome our python course',name = 'arun')
print('----------------------')


# default argument:

def wish( name = 'admin'):
    print('Hi',name)
    
wish('Abi')
wish()
print('----------------------')

def wish(name = 'admin',msg = 'Good morning'):
    print('Hi',name, msg)
    
wish('Arun', 'welcome our course')
wish()
wish('sanjay')
wish(name = 'Ram', msg = 'Welcome our course')
wish(name = 'Raj')
# wish(name = 'sri','welcome')     # SyntaxError: positional argument follows keyword argument
print('----------------------')

# variable length arguments:

def calculate_total(*no):         # variable length argument must - '*'

    total = 0
    for x in no:
        total = total+x
    print(total)
    
calculate_total(50)
calculate_total(20,50,80)
calculate_total(0)
print('----------------------')

# keyword length arguments:

def calculate_total(**kwargs):          # keyword length arguments must - '**'
    for sub,mark in kwargs.items():
        print(sub ,':', mark)
        
calculate_total(tamil = 90)
calculate_total(Tamil = 98, English = 89, Maths = 98, Science = 95)
print('----------------------')

	 