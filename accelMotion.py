print("Input -1 for wanted & -2 for unwanted")
vo = input("Initial velocity : ") * 1.0
v = input("Velocity : ") * 1.0
a = input("Acceleration : ") * 1.0
t = input("Time : ") * 1.0
d = input("Distance : ") * 1.0
print " "
if vo == -2:
	print "Impossible"
if v == -1:
	if a == -2:
		print ("Velocity = " + str(((d * 2) / t) - vo))
	elif t == -2:
		print ("Velocity = " + str((vo**2 + (2 * d * a))**0.5))
	elif d == -2:
		print ("Velocity = " + str(vo + a * t))
elif vo == -1:
	if v == -2:
		print "Impossible"
	elif a == -2:
		print ("Initial Velocity = " + str(((d * 2) / t ) - v))
	elif t == -2:
		print ("Initial Velocity = " + str(v**2 - (2 * a * d)))
	elif d == -2:
		print ("Initial Velocity = " + str(v - a * t))
elif a == -1:
	if v == -2:
		print ("Acceleration = " + str ((d - vo * t) / (2 * t**2)))
	elif t == -2:
		print ("Acceleration = " + str((v**2 - vo**2) / (2 * d)))
	elif d == -2:
		print ("Acceleration = " + str ((v - vo) / t))
elif t == -1:
	if v == -2:
		print ("That's some trig stuff do it yourself you lazy piece of trash <3")
	elif a == -2:
		print ("Time = " + str(d * 2 / (vo + v)))
	elif d == -2:
		print ("Time = " + str ((v - vo) / a))
elif d == -1:
	if v == -2:
		print ("Distance = " + str ((vo * t) + 0.5 * a * t**2))
	elif a == -2:
		print ("Distance = " + str(0.5 * (vo + v) * t))
	elif t == -2:
		print ("Distance = " + str((v**2 - vo**2) / 2 * a))
