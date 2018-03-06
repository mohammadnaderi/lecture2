####################################
# following variables are the same #
####################################
 str1=" salam!chitori? "
 str2='salam!chitori?'

######################
## concat two string #
######################
 name='mohammad'
 family= 'naderi'
 greeting= str1+name+family
 print(greeting)
#
 greeting2=str1+" "+name+" "+family
 print(greeting2)
#
 print(("\'"+greeting2+" \'") * 30)
######################################
## some useful operations on strings #
######################################
 print(greeting2.capitalize())
 print(greeting2.upper())
 print(greeting2.rsplit(' ')) # splitting the string by blank
 print(greeting2.strip(' ')) # remove the blanks before and after the string

###########################################
### another sample of printing a varibale #
###########################################
a = 152364
print(a)
str_pi = str(a)
print("a number is : ", a)  # print each part of input separately
print("a number is : " + str(a))  # concat two string
