BCD1 =[[ 0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],[1,0,0,0],[1,0,0,1],[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],[1,0,0,0]]

BCD2 =[[ 0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]

inputbit = [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,1,1],[0,0,1,0,0],[0,0,1,0,1],[0,0,1,1,0],[0,0,1,1,1],[0,1,0,0,0],[0,1,0,0,1],[0,1,0,1,0],[0,1,0,1,1],[0,1,1,0,0],[0,1,1,0,1],[0,1,1,1,0],[0,1,1,1,1],[1,0,0,0,0],[1,0,0,0,1],[1,0,0,1,0]]

OutputString = []
inputString = "INPUT"
outputString1 = "BCD1"
outputString2 = "BCD2"

for x in range(0, 4):
	AddString = "BCD1("  + str(3-x) +") <= "
	for y in range(0, len(BCD1)):
		if(BCD1[y][x] == 1):
			AddString += "("
			for i in range(5):
				if inputbit[y][i]:
					AddString += inputString + "("+str(4-i) + ")"
				else:
					AddString += "(NOT " + inputString + "("+str(4-i) + "))"
				if i!= 4:
					AddString += " AND "
					
			AddString += ") OR "
	AddString = AddString[:-3]
	AddString += ";"
	print(AddString)


print("")
print("")
	
for x in range(0, 4):
	AddString = "BCD2("  + str(3-x) +") <= "
	for y in range(0, len(BCD2)):
		if(BCD2[y][x] == 1):
			AddString += "("
			for i in range(5):
				if inputbit[y][i]:
					AddString += inputString + "("+str(4-i) + ")"
				else:
					AddString += "(NOT " + inputString + "("+str(4-i) + "))"
				if i!= 4:
					AddString += " AND "
					
			AddString += ") OR "
	AddString = AddString[:-3]
	AddString += ";"
	print(AddString)	
	
