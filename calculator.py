


def menu():
	print('\n\t ##################################')
	print('\t Choose from below menu: ')
	print('\t 1 - Arithmetic Operation ')
	print('\t 2 - Comparison Operation ')
	print('\t 3 - Logical Operation ')
	print('\t 4 - Assignment Operation ')
	print('\t 5 - Bitwise Operation ')
	print('\t 6 - Membership Operation ')
	print('\t 7 - Identity Operation ')
	print('\t Press 0 to exit ')
	print('\t ##################################')
	opt=input('\n\tEnter required option: ')
	if opt == '0':
		print('\n\tExiting program')
		exit(0)
	return opt

#########################################################

def armenu():
	''' 
Arithmetic Operators: These are the operators which are used to perform basic Mathematic calculations.
Addition(+): Operator used for addition of two or more values.
Eg: 4+5
Subtraction(-): Operator used for subtraction of two or more number.
Eg: 5-4
Multiplication(*):Operator used for product of two numbers.
Eg: 8*6
Division(/): Operator used for division of number with other.
Eg: 4/2
Modulus(%): Same as Division but give remainder as output.
Eg: 5/2=1
Exponent(**): Operators for power of number.Eg: 5**3=125
Floor division(//): Same as division but don’t consider value after point.
Eg: 24/5=4
	'''
	def add(a,b):
		return a+b

	def sub(a,b):
		return a-b

	def mult(a,b)	:
		return a*b

	def divi(a,b):
		return a/b

	def modu(a,b):
		return a%b

	def expo(a,b):
		return a**b

	def flrdiv(a,b):
		return a//b
	print('\n\t +-*/%**// +-*/%**// +-*/%**// +-*/%**// +-*/%**//')
	
	print('\n\t Arithmetic Operation is Selected \n\t' )
	print('\t + for Addition')
	print('\t - for Subtraction')
	print('\t * for Multiplication')
	print('\t / for Division')
	print('\t % for Modulus')
	print('\t **  for Exponent')
	print('\t //  for Floor Division')
	print('\t Enter # to check help')
	print('\t Enter 9 to goto Main screen')
	
	print('\n\t +-*/%**// +-*/%**// +-*/%**// +-*/%**// +-*/%**//')
	aropt=input('\n\t Please Choose operation to perform: ')

	if aropt in ('+','-','*','/','%','**','//'):
		a=int(input('\n\tEnter 1st Variable value: '))
		b=int(input('\n\tEnter 2nd Variable value: '))
		if aropt=='+':
			print('\n\tAddition of given values is: ',add(a,b))
		if aropt=='-':
			print('\n\t Subtraction of given values is: ',sub(a,b))
		if aropt=='*':
			print('\n\t Multiplication of given values is: ',mult(a,b))
		if aropt=='/':
			print('\n\t Division of given values is: ',divi(a,b))
		if aropt=='%':
			print('\n\t Modulus of given values is: ',modu(a,b))
		if aropt=='**':
			print('\n\t Exponent of given values is: ',expo(a,b))
		if aropt=='//':
			print('\n\t Floor Division of given values is: ',flrdiv(a,b))
		armenu()
	elif aropt=='#':
		print(armenu.__doc__)
		armenu()
	elif aropt=='9':
		return '1'
	else:
		print('\n\t Invalid option given \n\t Please choose again')
		armenu()




#####################################################################################

def compare():
	'''
Comparison Operators: This perform comparison between the values and return output in the form of Boolean (True/False).These are also called as Relational Operators.
(==):If both values are same then it will return True other wise False.
Eg: a=5 b=2 (a==b)=False
(!=):If both values are different it return True and viceversa.
Eg: a=5 b=2 (a==b)=True
(>):Check the number is greater or not and return True is Yes and Viceversa.
Eg: a>b=True
(<):Check the number is smaller or not and return True if Yes and vicecersa.
Eg: a<b=False
(>=):Checks greaterthan or equal to condition with numbers and return True or false.
Eg: a>=b=True
(<=):Checks smallerthan or equal to condition with numbers and return True or false.
Eg: a<=b=False 
	'''		
	print('\n\t == != > < >= <= == != > < >= <= == != > < >= <=  ')
	
	print('\n\t Comparison Operation is Selected \n\t' )
	print('\t == for Equal')
	print('\t != for Not Equal')
	print('\t > for Greater')
	print('\t < for smaller')
	print('\t >= for Greaterthan or Equal')
	print('\t <= for smallerthan or Equal')
	print('\t Enter # to check help')
	print('\t Enter 9 to goto Main screen')
	
	print('\n\t == != > < >= <= == != > < >= <= == != > < >= <=  ')
	cpmopt=input('\n\t Please Choose operation: ')

	if cpmopt in ('==','!=','>','<','>=','<='):
		a=int(input('\n\tEnter 1st Variable value: '))
		b=int(input('\n\tEnter 2nd Variable value: '))
		if cpmopt=='==':
			print('\n\tIs given values equal: ',(a==b))
		if cpmopt=='!=':
			print('\n\tIs given values not equal: ',(a!=b))
		if cpmopt=='>':
			print('\n\tIs 1st Value is greater than 2nd Value: ',(a>b))
		if cpmopt=='<':
			print('\n\tIs 1st Value is less than 2nd Value: ',(a<b))
		if cpmopt=='>=':
			print('\n\tIs 1st Value is greater than or equal 2nd Value: ',(a>=b))
		if cpmopt=='<=':
			print('\n\tIs 1st Value is less than or equal 2nd Value: ',(a<=b))
		compare()
	elif cpmopt=='#':
		print(compare.__doc__)
		compare()
	elif cpmopt=='9':
		return '1'
	else:
		print('\n\t Invalid option given \n\t Please choose again')
		compare()

#####################################################################################	

def logic():
	'''
Logical Operators: Operators that are used to perform logical operation such as AND ,OR and NOT are called logical operators and give output as Boolean.
Logical AND(and): This will give true only if both the conditions are true otherwise false.
Eg: a=8<6 and 6>5 = False (F) (T)
Logical OR(or):This will give True if one condition is true otherwise false.
Eg: a=8<6 or 6>5 = True (F) (T)
Logical NOT(not):This will convert True into False and viceversa.
Eg: a=not(5<6) = False
	'''

	print('\n\t AND OR NOT AND OR NOT AND OR NOT AND OR NOT  ')
	
	print('\n\t Logical Operation is Selected \n\t' )
	print('\t AND for And Operation')
	print('\t OR for Or Operation')
	print('\t NOT for Not Operation')
	
	print('\t Enter # to check help')
	print('\t Enter 9 to goto Main screen')
	
	print('\n\t AND OR NOT AND OR NOT AND OR NOT AND OR NOT  ')
	logopt=input('\n\t Please Choose operation: ')

	if logopt in ('AND','OR','NOT'):

		a=(input('\n\tEnter X Variable value in True or False format: '))
		b=(input('\n\tEnter Y Variable value in True or False format: '))
		if logopt == 'AND':
			print('\n\tAND Operation on ',a,' and ',b,' is: ', a and b)
		if logopt == 'OR':
			print('\n\tOR Operation on ',a,' and ',b,' is: ', a or b)
		if logopt == 'NOT':
			print('\n\t NOT  Operation on ',a,' is: ', not a )
			print('\n\t NOT  Operation on ',b,' is: ', not b )
			logic()
	elif logopt=='#':
		print(logic.__doc__)
		logic()
	elif logopt=='9':
		return '1'
	else:
		print('\n\t Invalid value given \n\t Please choose again')
		logic()


#####################################################################################	

def assign():
	'''
Assignment Operator: Operator that assign a value to a variable is called assignment operators.
If a=1
(=): Assign value from right side to the Left side variable.
Eg: c=9+4
(+=):Adds right side operand to left and assign result to left operand.
Eg: a+6
a=1+6 a=7
(-=):Subtract right side operand to left and assign result to left operand.Eg: a -=6
a=7-6 a=1
(*=):Multiply right side operand with left and assign result to left operand.
Eg: a*=7
a=1*7 a=7
(/=):Divide right side operand with left and assign result to left operand.
Eg: a/=7
a=7/7
a=1
(%=):Divide right side operand with left operand and assign reminder as result to left
operand.
Eg: a%=5
a=1%5 a=4
(**=): perform power of right side operand with left operand and assign result to left
operand.
Eg: a**=3 a=4**3 a=64
(//=):Perform floor division and assign value to the left operand.
Eg: a//=9 a=64//9 a=7
	'''		
	print('\n\t = += -= *= /= %= **= //= = += -= *= /= %= **= //= ')

	print('\n\t Assignment Operation is Selected \n\t' )
	print('\t = for Assignment')
	print('\t += Adds right side operand to left and assign result to left operand')
	print('\t -= Subtract right side operand to left and assign result to left operand')
	print('\t *= Multiply right side operand to left and assign result to left operand')
	print('\t /= Divide right side operand to left and assign result to left operand')
	print('\t %= Divide right side operand with left operand and assign reminder as result to left operand')
	print('\t **= perform power of right side operand with left operand and assign result to left operand')
	print('\t //= Perform floor division and assign value to the left operand')
	print('\t Enter # to check help')
	print('\t Enter 9 to goto Main screen')

	print('\n\t = += -= *= /= %= **= //= = += -= *= /= %= **= //= ')
	assopt=input('\n\t Please Choose operation: ')

	if assopt in ('=','+=','-=','*=','/=','%=','**=','//='):
		a=int(input('\n\tEnter Variable value: '))
		if assopt == '=':
			print('\n\t Entered value is assigned to A ', a)
		if assopt == '+=':
			b=int(input('\n\t Enter the value to be added to A and assigned '))
			a+=b
			print('\n\t Given value ',b,' is added to A and new value of A is ',a)
		if assopt == '-=':
			b=int(input('\n\t Enter the value to be Subtracted to A and assigned '))
			a-=b
			print('\n\t Given value ',b,' is subtracted from A and new value of A is ',a)
		if assopt == '*=':
			b=int(input('\n\t Enter the value to be multiplied to A and assigned '))
			a*=b
			print('\n\t Given value ',b,' is multiplied to A and new value of A is ',a)
		if assopt == '/=':
			b=int(input('\n\t Enter the value to be divided to A and assigned '))
			a/=b
			print('\n\t Given value ',b,' is added to A and new value of A is ',a)
		if assopt == '**=':
			b=int(input('\n\t Enter the value to be powered to A and assigned '))
			a**=b
			print('\n\t Given value ',b,' is powered to A and new value of A is ',a)
		if assopt == '//=':
			b=int(input('\n\t Enter the value to be floor divided to A and assigned '))
			a//=b
			print('\n\t Given value ',b,' is added to A and new value of A is ',a)
		assign()
	elif assopt=='#':
		print(assign.__doc__)
		assign()
	elif assopt=='9':
		return '1'
	else:
		print('\n\t Invalid option given \n\t Please choose again')
		assign()






#####################################################################################	

def bitwis():
	'''
Bitwise Operators: Operators which convert the values into binary format and perform Bitwise operations and give result in binary format.
Binary AND(&):Convert values to binary and perform AND which is if both the boththe binary values are 1 the output will be 1 otherwise 0 in all cases.
Eg: x=34,y=23 x= 0010 0010
y=0001 0111
x&y=0000 0010 = 2
Binary OR(|):Convert values to binary and perform OR which is if any the binary values are 1 the output will be 1 otherwise 0 in all cases.
Eg: x=34,y=23 x= 0010 0010
y=0001 0111
x|y=0011 0111 = 55
Binary XOR(^):Convert values to binary and perform XOR which is if both the values of binary format are same then result is 0 and 1 in othercase.Eg: x=34,y=23 x= 0010 0010
y=0001 0111
x^y=0011 0101 = 53
Binary Ones complement(~):Convert values to binary and perform Ones complement which is converting 1’s to 0’s and 0’s into 1’s.
Eg: x=34,y=23 x= 0010 0010
~x=1101 1101 = -34
Binary Leftshift(<<):Left side operand value will be moved towards left taking the condition in right operand.
Eg: x=34
x= 0010 0010
x<<2=1000 1000 = 136
Binary RightShift(>>):Left side operand value will be moved towards right taking the condition in right operand.
Eg: x=34
x= 0010 0010
x>>1= 0100 0100 = 68
	'''

	print('\n\t & | ^ ~ << >> & | ^ ~ << >> & | ')
	
	print('\n\t Bitwise Operation is Selected \n\t' )
	print('\t & for Binary And Operation')
	print('\t | for Binary Or Operation')
	print('\t ^ for Binary XOR Operation')
	print('\t ~ for complement Operation')
	print('\t << for Left Shift Operation')
	print('\t >> for Right Shift Operation')
	print('\t Enter # to check help')
	print('\t Enter 9 to goto Main screen')
	
	print('\n\t & | ^ ~ << >> & | ^ ~ << >> & | ')
	bitopt=input('\n\t Please Choose operation: ')

	if bitopt in ('&','|','^'):
		a=int((input('\n\tEnter X Variable value : ')))
		b=int((input('\n\tEnter Y Variable value : ')))
		print('\n\tGiven values in Binary format are as',a,' - ',bin(a),b,' - ',bin(b))
		if bitopt == '&':
			print('\n\tBinary AND Operation on ',a,' and ',b,' is: ', a & b)
		if bitopt == '|':
			print('\n\tBinary OR Operation on ',a,' and ',b,' is: ', a | b)		
		if bitopt == '^':
			print('\n\tBinary XOR Operation on ',a,' and ',b,' is: ', a ^ b)
		bitwis()		
	if bitopt in ('~','<<','>>'):
		a=int((input('\n\tEnter X Variable value : ')))
		print('\n\tGiven value in Binary format is ',a,' - ',bin(a))
		if bitopt == '~':
			print('\n\tComplement operation on ',a, ' is ', ~ a)
		if bitopt == '<<':
			step=int(input('\n\t Enter Shift step size: '))
			print('\n\tLeftshift operation on ',a, ' is ',(a<<step))
		if bitopt == '>>':
			step=int(input('\n\t Enter Shift step size: '))
			print('\n\tRightShift operation on ',a, ' is ',(a>>step))
		bitwis()
	elif bitopt=='#':
		print(bitwis.__doc__)
		bitwis()
	elif bitopt=='9':
		return '1'
	else:
		print('\n\t Invalid value given \n\t Please choose again')
		bitwis()


#####################################################################################		

def member():
	'''
Membership Operators: Membership operators are used to test whether the condition is True or False in a Sequence.
In: This operator evaluates True only if the specified variable is found in specified sequence and give false otherwise.
Eg: a= python
list=[ datascience , game , python ]
if (a in list):
print ( python )
else:
= Python
print ( datascience )
notin: This operator evaluates True only if the specified variable is found in specified sequence and give false otherwise.
Eg: a= python
list=[ datascience , game , python ]
if (a notin list):
print ( python )
else:
= datascience
print ( datascience )
	'''		
	print('\n\t *********************************** ')
	
	print('\n\t Membership Operation is Selected \n\t' )
	print('\t in for In Operation')
	print('\t notin for Notin Operation')
	print('\t Enter # to check help')
	print('\t Enter 9 to goto Main screen')
	
	print('\n\t *********************************** ')
	memopt=input('\n\t Please Choose operation: ')
	if memopt in ('in','notin'):
		mainstr=input('\n\t Enter a full main string: ')	
		substr=input('\n\t Enter a string to check: ')
		if memopt == 'in':
			print('\n\t Is check string part of main string:', substr in mainstr)
			member()
		if memopt == 'notin':
			print('\n\t Is check string part of main string:', substr not in mainstr)
			member()
	elif memopt=='#':
		print(member.__doc__)
		member()
	elif memopt=='9':
		return '1'
	else:
		print('\n\t Invalid option given \n\t Please choose again')
		member()

#####################################################################################	

start=menu()
while  start != '0':
	if start == '1':
		start=armenu()
		start=menu()
	elif start == '2':
		start=compare()
		start=menu()
	elif start == '3':
		start =logic()
		start=menu()
	elif start == '4':
		start=assign()
		start=menu()
	elif start == '5':
		start=bitwis()
		start=menu()
	elif start == '6':
		start=member()
		start=menu()
	elif start == '7':
		print('7th operation yet to built')
		start=menu()
	else:
		print('\n\t Invalid Option Selected\n\t Please try again')
		start=menu()