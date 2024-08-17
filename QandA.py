#1. How can we store a s1ngle quote (‘) as a str1ng 1n a var1able?
#1.The first line of the program uses the print() function to print the string “‘WithQuotes'” enclosed within single quotes. The inner single quotes are escaped using a backslash to prevent them from ending the string prematurely.
#2.The second line of the program uses the print() function to print the string “Hello ‘Python'” which contains a single quote within double quotes. The single quote is not escaped since it is inside a string enclosed within double quotes.
#3.The third line of the program uses the print() function to print the string “”WithQuotes”” enclosed within double quotes. The inner double quotes are escaped using HTML entity codes to prevent them from ending the string prematurely.
#4.The fourth line of the program uses the print() function to print the string “Hello “Python”” which contains double quotes within single quotes. The double quotes are also escaped using HTML entity codes since they are inside a string enclosed within single quotes.

# Q Refer the below var1able:
# x = ‘a'
# Here, is x a character type or str1ng type variable? Support your answer w1th an explanat1on.
# x is a string typed variable whenever anything stored in the variable with single or double or triple quotes then it is considered as a string 


# 3.Q Apply the follow1ng funct1ons on th1s variable: ‘Welcome to Python foun at1on course'
# 1. find()
# 2. count()
# 3. len()
# 4. Concatenation()
# Note: You can use your cho1ce of parametersQ But make sure 1t 1s correct.
s="welcome to Python Foundation course"
print(s.find("welcome"))#output  -1
print(s.count("a"))#output 1
print(len(s))#35
print(s+" "+"pwskills")#welcome to  the python foundation course pwskills


# Q4Q For the var1able: wor = ‘PanaJi@12256"
# Calculate the following:
# (a) Total number of alphabets in lowercase
# (b) Total number of alphabets in uppercase
# (c) Total number of numerical in string

wor="PanaJi@12256"
lower_count=0
upper_count=0
numerical_count=0
for i in wor:
    if(i>='A' and i<='Z'):
        upper_count=upper_count+1
    elif (i>='a' and i<='z'):
        lower_count+=1
    elif(i>='0' and i<='9'):
        numerical_count+=1
print(upper_count)
print(lower_count)
print(numerical_count)

# Q5 Write a code to store a numer1cal value inside a variable then convert it into string

n=int(input("enter the number "))
m=str(n)
print(type(m))
print(m)

