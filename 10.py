# Write a Python program that accepts an integer (n) and 
# computes the value of n+nn+nnn.

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

c = int(input("Input an integer : "))
b1 = int(f"{c}")
b2 = int( f"{c}{c}" )
b3 = int( f"{c}{c}{c}" )
print (b1+b2+b3)

n=input("Sample value of n is:")
sum=int(n)+int(n+n)+int(n+n+n)
print("Expected result:",sum)
