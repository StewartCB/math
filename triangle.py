import sys
import math

degOrRad = raw_input("Degrees or Radians? ")
print "List known values of the triangle, input -1 for unknown."
print ""
sides = [input("Input value for side A: ") * 1.0, input("Input value for side B: ") * 1.0, input("Input value for side C: ") * 1.0]			#Array of side values
angles = [input("Input value for angle A: ") * 1.0, input("Input value for angle B: ") * 1.0, input("Input value for angle C: ") * 1.0]		#Array of angle values
print ""

sideIsKnown = [sides[0] != -1, sides[1] != -1, sides[2] != -1]			#Array of booleans to see if side values are knwon
angleIsKnown = [angles[0] != -1, angles[1] != -1, angles[2] != -1]		#Array of booleans to see if angle values are known

sidesUnknown = 3	#Represents number of unknown side values
anglesUnknown = 3 	#Represenrs number of unknown angle values
for i in range (0 , 3):		#Counts number of unknowns
	if (angleIsKnown[i]):
		anglesUnknown = anglesUnknown - 1
	if (sideIsKnown[i]):
		sidesUnknown = sidesUnknown - 1
	
#If degrees are wanted / inputed, puts into radians
if ((degOrRad is "Degrees") | (degOrRad is "degrees") | (degOrRad is "d")):
	for i in range(0, 3):
		if angles[i] != -1:
			angles[i] = math.radians(angles[i])
	
#If 2 angles are known, solves for third
if angleIsKnown[0] & angleIsKnown[1]:
	angles[2] = math.pi - (angles[0] + angles[1])
elif angleIsKnown[0] & angleIsKnown[2]:
	angles[1] = math.pi - (angles[0] + angles[2])
elif angleIsKnown[1] & angleIsKnown[2]:
	angles[0] = math.pi - (angles[1] + angles[2])

if sidesUnknown == 3:																																	#aaa triangles
	print "Impossible"
	sys.exit()

if anglesUnknown == 3:																																	#sss triangles
	angles[0] = math.acos((sides[1]**2 + sides[2]**2 - sides[0]**2) / (2 * sides[1] * sides[2]))
	angles[1] = math.acos((sides[2]**2 + sides[0]**2 - sides[1]**2) / (2 * sides[2] * sides[0]))
	angles[2] = math.pi - (angles [0] + angles [1])
	
elif sidesUnknown == 2:																																	#aas triangles & asa triangles
	#sets value of unknown sides
	if sideIsKnown[0]:
		sides[1] = (sides[0] / math.sin(angles[0])) * math.sin(angles[1])
		sides[2] = (sides[0] / math.sin(angles[0])) * math.sin(angles[2])
	elif sideIsKnown[1]:
		sides[0] = (sides[1] / math.sin(angles[1])) * math.sin(angles[0])
		sides[2] = (sides[1] / math.sin(angles[1])) * math.sin(angles[2])
	elif sideIsKnown[2]:
		sides[0] = (sides[2] / math.sin(angles[2])) * math.sin(angles[0])
		sides[1] = (sides[2] / math.sin(angles[2])) * math.sin(angles[1])

if anglesUnknown == 2:																																	
	if ((angleIsKnown[0] & (not sideIsKnown[0])) | (angleIsKnown[1] & (not sideIsKnown[1])) | (angleIsKnown[2] & (not sideIsKnown[2]))):				#sas triangles
		if not sideIsKnown[0]:
			sides[0] = (sides[1]**2 + sides[2]**2 - (2 * sides[1] * sides[2] * math.cos(angles[0])))**0.5
		elif not sideIsKnown[1]:
			sides[1] = (sides[0]**2 + sides[2]**2 - (2 * sides[0] * sides[2] * math.cos(angles[1])))**0.5
		elif not sideIsKnown[2]:
			sides[2] = (sides[0]**2 + sides[1]**2 - (2 * sides[0] * sides[1] * math.cos(angles[2])))**0.5
		#Finds angles
		angles[0] = math.acos((sides[1]**2 + sides[2]**2 - sides[0]**2) / (2 * sides[1] * sides[2]))
		angles[1] = math.acos((sides[2]**2 + sides[0]**2 - sides[1]**2) / (2 * sides[2] * sides[0]))
		angles[2] = math.pi - (angles [0] + angles [1])
	
	else:																																				#ssa triangles
		#Finds side of the known angle
		if (sideIsKnown[0] & angleIsKnown[0]):
			if sideIsKnown[1]:
				angles[1] = math.asin(math.sin(angles[0]) / sides[0] * sides[1])
				angleIsKnown[1] = not angleIsKnown[1]
			elif sideIsKnown[2]:
				angles[2] = math.asin(math.sin(angles[0]) / sides[0] * sides[2])
				angleIsKnown[2] = not angleIsKnown[2]
		elif (sideIsKnown[1] & angleIsKnown[1]):
			if sideIsKnown[0]:
				angles[0] = math.asin(math.sin(angles[1]) / sides[1] * sides[0])
				angleIsKnown[0] = not angleIsKnown[0]
			elif sideIsKnown[2]:
				angles[2] = math.asin(math.sin(angles[1]) / sides[1] * sides[2])
				angleIsKnown[2] = not angleIsKnown[2]
		elif (sideIsKnown[2] & angleIsKnown[2]):
			if sideIsKnown[0]:
				angles[0] = math.asin(math.sin(angles[2]) / sides[2] * sides[0])
				angleIsKnown[0] = not angleIsKnown[0]
			elif sideIsKnown[1]:
				angles[1] = math.asin(math.sin(angles[2]) / sides[2] * sides[1])
				angleIsKnown[1] = not angleIsKnown[1]
		#Solves for third angle
		if angleIsKnown[0] & angleIsKnown[1]:
			angles[2] = math.pi - (angles[0] + angles[1])
		elif angleIsKnown[0] & angleIsKnown[2]:
			angles[1] = math.pi - (angles[0] + angles[2])
		elif angleIsKnown[1] & angleIsKnown[2]:
			angles[0] = math.pi - (angles[1] + angles[2])
		#Solves for final side
		if not sideIsKnown[0]:
			sides[0] = (sides[1]**2 + sides[2]**2 - (2 * sides[1] * sides[2] * math.cos(angles[0])))**0.5
		elif not sideIsKnown[1]:
			sides[1] = (sides[0]**2 + sides[2]**2 - (2 * sides[0] * sides[2] * math.cos(angles[1])))**0.5
		elif not sideIsKnown[2]:
			sides[2] = (sides[0]**2 + sides[1]**2 - (2 * sides[0] * sides[1] * math.cos(angles[2])))**0.5

#If degrees is wanted / inputed converts to degrees	
if ((degOrRad is "Degrees") | (degOrRad is "degrees") | (degOrRad is "d")):
	for i in range(0, 3):
		if angles[i] != -1:
			angles[i] = math.degrees(angles[i])
		
#Final output
print ("Side A = " + str(sides[0]))
print ("Side B = " + str(sides[1]))
print ("Side C = " + str(sides[2]))
print ("Angle A = " + str(angles[0]))
print ("Angle B = " + str(angles[1]))
print ("Angle C = " + str(angles[2]))
	