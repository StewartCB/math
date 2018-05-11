import math
shape = raw_input('What shape? (or list shapes)')
if shape == "list shapes":
	print ("square, rectangle, triangle, circle, parallelogram, ellipse, cube, rectangular prism, sphere, circular cone, general cone")
	shape = raw_input('What shape? ')
if shape == "square":
	l = input("Length? ") * 1.0
	print ("Area = " + str(l**2))
	print ("Perimeter = " + str(l * 4))
elif shape == "rectangle":
	l = input("Length? ") * 1.0
	w = input("Width? ") * 1.0
	print ("Area = " + str(l * w))
	print ("Perimeter = " + str(2*l + 2*w))
elif shape == "triangle":
	b = input("Base? ") * 1.0
	h = input("Height? ") * 1.0
	print ("Area = " + str(0.5 * b * h))
elif shape == "circle":
	r = input("Radius? ") * 1.0
	print ("Area = " + str(math.pi * r**2))
	print ("Circumference = " + str(2 * math.pi * r))
elif shape == "parallelogram":
	l = input("Length? ") * 1.0
	h = input("Height? ") * 1.0
	print ("Area = " +	str(l * h))
elif shape == "ellipse":
	a = input("Longer Radius? ") * 1.0
	b = input("Shorter Radius? ") * 1.0
	print ("Area = " + str(math.pi * a * b))
	print ("Circumference = " + str(math.pi * (3 * (a + b) - ((a + 3*b) * (b + 3*a))**0.5)))
elif shape == "cube":
	l = input("Length? ") * 1.0
	print ("Volume = " + str(l**3))
	print ("Surface Area = " + str(6 * l**2))
elif shape == "rectangular prism":
	l = input("Length? ") * 1.0
	w = input("Width? ") * 1.0
	h = input("Height? ") * 1.0
	print ("Volume = " + str(l * w * h))
	print ("Surface Area = " + str(2*l*w + 2*l*h + 2*h*w))
elif shape == "sphere":
	r = input("Radius? ") * 1.0
	print ("Volume = " + str((4.0/3.0) * math.pi * r**3))
	print ("Surface Area = " + str(4 * math.pi * r**2))
elif shape == "circular cone":
	r = input("Radius? ") * 1.0
	h = input("Height? ") * 1.0
	print ("Volume = " + str((1.0/3.0) * math.pi * r**2 * h))
	print ("Surface Area = " + str(math.pi * r * (r**2 + h**2)**0.5 + math.pi * r**2))
elif shape == "general cone":
	ba = input("Base Area? ") * 1.0
	h = input("Height? ") * 1.0
	print("Volume = " + str((1.0/3.0) * a * h))
else:
	print "No such shape"
