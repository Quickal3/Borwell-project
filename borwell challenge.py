print("welcome to this program to use for a paint calculator")#welcoming you to the program and telling you whats the program used for
height = int(input("what is the height of the room?"))#asking the person what is the height of the room to use it for later calculations
length = int(input("what is the length of the room?"))#asking the person for the length of the room to use for later calculations
width = int(input("what is the width of the room?"))#asking the person for the width of the room to use later calculations
surface_area = width*height*2 + length*width*2 + height*length*2#the calculation for the surface area
Areaofthefloor = length*width#the calculation for the area of the floor
amountofpaint = height*length*2 + height*width*2#the calculation to find the amount of paint needed
volume = length*width*height#the calculation to find the volume
