import sys
import math

print "List known values of the triangle, input -1 for unknown."
print ""
sides = [input("Input value for side A: ") * 1.0, input("Input value for side B: ") * 1.0, input("Input value for side C: ") * 1.0]			#Array of side values
angles = [input("Input value for angle A: ") * 1.0, input("Input value for angle B: ") * 1.0, input("Input value for angle C: ") * 1.0]		#Array of angle values
print ""

sideIsKnown = [sides[0] != -1, sides[1] != -1, sides[2] != -1]			#Array of booleans to see if side values are knwon
angleIsKnown = [angles[0] != -1, angles[1] != -1, angles[2] != -1]		#Array of booleans to see if angle values are known

sidesUnknown = 0	#Represents number of unknown side values
anglesUnknown = 0 	#Represenrs number of unknown angle values
for i in range (0 , 3):		#Counts number of unknowns
	if not sideIsKnown[i]:
		sidesUnkown = sidesUnknown + 1
	if not sideIsKnown[i]:
		anglesUnknown = anglesUnknown + 1

#If 2 angles are known, solves for third
if angleIsKnown[0] & angleIsKnown[1]:
	angles[2] = 180 - (angles[0] + angles[1])
elif angleIsKnown[0] & angleIsKnown[2]:
	angles[1] = 180 - (angles[0] + angles[2])
else:
	angles[0] = 180 - (angles[1] + angles[2])

if sidesUnknown == 3:																																	#sss triangle
	print "Impossible"
	sys.exit()

if anglesUnknown == 3:																																	#aaa triangle
	angles[0] = math.degrees(math.acos((sides[1]**2 + sides[2]**2 - sides[0]**2) / (2 * sides[1] * sides[2])))
	angles[1] = math.degrees(math.acos((sides[2]**2 + sides[0]**2 - sides[1]**2) / (2 * sides[2] * sides[0])))
	angles[2] = 180 - (angles [0] + angles [1])
	
elif sidesUnknown == 2:																																#aas triangle & asa triangle
	#sets value of unknown sides
	if sideIsKnown[0]:
		sides[1] = (sides[0] / math.degrees(math.sin(math.radians(angles[0])))) * math.degrees(math.sin(math.radians(angles[1])))
		sides[2] = (sides[0] / math.degrees(math.sin(math.radians(angles[0])))) * math.degrees(math.sin(math.radians(angles[2])))
	elif sideIsKnown[1]:
		sides[0] = (sides[1] / math.degrees(math.sin(math.radians(angles[1])))) * math.degrees(math.sin(math.radians(angles[0])))
		sides[2] = (sides[1] / math.degrees(math.sin(math.radians(angles[1])))) * math.degrees(math.sin(math.radians(angles[2])))
	elif sideIsKnown[2]:
		sides[0] = (sides[2] / math.degrees(math.sin(math.radians(angles[2])))) * math.degrees(math.sin(math.radians(angles[0])))
		sides[1] = (sides[2] / math.degrees(math.sin(math.radians(angles[2])))) * math.degrees(math.sin(math.radians(angles[1])))
	
elif anglesUnknown == 2:
	if not sideIsknown[0]:
		side[0] = (side[1]**2 + side[2]**2 + (2 * side[1] * side[2] * math.degrees(math.sin(math.radians(angles[a])))))**0.5
	if not sideIsknown[1]:
	
	if not sideIsknown[2]:
	


#Final output
print ("Side A = " + str(sides[0]))
print ("Side B = " + str(sides[1]))
print ("Side C = " + str(sides[2]))
print ("Angle A = " + str(angles[0]))
print ("Angle B = " + str(angles[1]))
print ("Angle C = " + str(angles[2]))
	