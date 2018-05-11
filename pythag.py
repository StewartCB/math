print "Input -1 for unknown"
a = input("a : ")
b = input("b : ")
c = input("c : ")
print " "
if a == -1:
    print ("a = " + str(((c**2 - b**2)**0.5)))
elif b == -1:
    print ("b = " + str((c**2 - a**2)**0.5))
elif c == -1:
    print ("c = " + str((a**2 + b**2)**0.5))
