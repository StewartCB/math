arr = []
l = input("Input number of items: ")
for i in range(0, l):
    arr.append(1.0 * input("Item " + str(i) + " = "))
    i = i + 1
print " "
arr.sort()
sum = 0.0

#Average / Mean

for o in range(0, len(arr)):
    sum = sum + arr[o]
print ("Sum = " + str(sum))
print ("Average = " + str(sum/(len(arr) )))

#Median

if len(arr) % 2 == 0:
    print ("Median = " + str((arr[len(arr)/2] + arr[len(arr)/2 - 1])/2))
else:
    print ("Median = " + str(arr[len(arr)/2]))

#mode

most = 0
numMode = 0
poses = []
for x in range (0, len(arr)):
    count = 0
    check = 0
    for y in range(len(arr)):
        if arr[y] == arr[x]:
            count = count + 1
    if count > most:
        most = count
        pos = x
        numMode = 1
        poses.append(pos)
    elif count == most:
        for b in range(0, len(poses)):
            if arr[poses[b]] == arr[x]:
                check = check + 1
        if check == 0:
            poses.append(x)
        numMode = numMode + 1
if most == 1:
    print ("No mode")
elif numMode == 1:
    print ("Mode = " + str(arr[pos]))
else:
    finText = "Mode = "
    for p in range(0, len(poses)):
        if p == len(poses) - 1:
            finText = finText + str(arr[poses[p]])
        else:
            finText = finText + str(arr[poses[p]]) + " & "
    print finText
