#---------------->> Lambda Function  <<------------------------

# Lambda function  - Anonymous function: 
#	functional program concepts
#	one time used for any activity

#1.) square of number:

squareofnumber = lambda n: n*n

print("square of number: ",squareofnumber(5))
print('-----------------------------')

#2.) sum of two number:

sumoftwo =lambda no1,no2: no1+no2

print("sum of two number: ",sumoftwo(10,20))
print('-----------------------------')

#3.) bigest of two number:

bigoftwo = lambda a,b: a if a>b else b

print("bigest of two number: ",bigoftwo(30,50))
print('-----------------------------')


#4.) nested function:

def outer():
    print(" i am standing outer function")
    def inner():
        print(" i am standing inside inner function")
    print("outer inner function")
    inner()
outer()