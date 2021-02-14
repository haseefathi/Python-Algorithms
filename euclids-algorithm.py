# Program to output the gcd of two integers

def gcd(a,b):
    if b == 0:
        return a
    r = a%b
    return gcd(b,r)

print('Enter two integers to calculate their greatest common divisor (GCD): ')

a = int(input('First number:'))
b = int(input('Second number:'))

outputSring = "The GCD of {num1} and {num2} is {ans}"
print(outputSring.format(num1 = a, num2 = b, ans = gcd(a,b)))
