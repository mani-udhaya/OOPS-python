# ==============>> Variable & lambda function <<==========

# Types of Variable:
#   	1. Global variable
#	    2. Local variable

# Function:
#	- Group(set) of instruction with a name.
# Module:
#	- Group(set) of function saved a file.
# Library:
#	- Group(set) module 


# Global variable:

discount = 20          # this is global discount - global variable
def purchaseTV():
    print('TV discount: ',discount)
purchaseTV()

def purchase_lap():
    discount = 30       # thia is local discount - local variable
    print('laptop discount: ',discount)
purchase_lap()
print('-----------------------------')


# global and local variable:

discount = 20
def OpeningTime():
    global discount
    discount = 35
    print('OpeningTime Discount: ',discount)
    
def purchaseTV():
    print('TV discount: ',discount)

def purchase_lap():
    discount = 30       # thia is local discount - local variable
    print('global discount:',globals)
    print('laptop discount: ',discount)
    
OpeningTime()
purchaseTV()
purchase_lap()