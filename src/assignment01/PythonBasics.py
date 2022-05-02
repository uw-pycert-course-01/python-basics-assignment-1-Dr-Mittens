my_string = 'The power of words and symbols'
my_integer = 12345
my_float = 1.01
x = 4
y = 73
z = x+y
#z should be equal to 77
print(z)

a = 8.2
b = 3.14
c = a+b
#c should be equal to 11.34
print(c)

text1 = 'We can also add'
text2 ='oh fiddlesticks'
text3 = text1+text2
#text3 should result in We can also addoh fiddlesticks
#yes the missing space was totally intentional and not an easy oopsy that retroactively makes the fiddlesticks funnier
print(text3)

floatingint = my_float+z
#floatingint should be a float with value 78.01
print(floatingint)
print(type(floatingint))

#consumingstr = x+text2
#consumingstr should be an error since we did not convert the int to a string first
#consumingstr = str(x)+text2
#yep, now properly doing str(int) then adding, and the result will be a string
#print(consumingstr)
print(type(my_string))
print(type(my_integer))
print(type(my_float))
symbol = '10'
print(type(symbol))
restored = int(symbol)
print(type(restored))
print(round(5*7.654321,3))
my_name = input('Please enter your name: ')
print('Your name has been registered as: '+my_name)
favorite_number = input('Please enter your favorite number: ')
print(type(favorite_number))
#inputs default as strings because str won't crash from unexpected user inputs
#and if we expect/need an integer value it's simple enough to test then convert
var1 = input('Please enter an integer:')
var2 = input('Please enter one more integer:')
var3 = var1+var2
print(var3)
#var3 will be a string sum of the above to *numbers* stored as strings, so 1+3 will result in '13' instead of 4
confirmed = 'false'
while confirmed == 'false':
    try:
        var1=int(var1)
        var2=int(var2)
        confirmed = 'true'
    except:
        print('Inputs not recognized as integers, please try again')
        var1 = input('Please enter an integer:')
        var2 = input('Please enter one more integer:')
var4 = var1+var2
print(var4)