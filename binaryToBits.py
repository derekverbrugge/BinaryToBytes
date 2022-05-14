#binaryToBits.py

#settings
inputF = 'binaryTest2.bin' #input file
outputF = 'oFile.o' #output file
bitCount = 5 #bits per byte to be read in
printFlag = 1 #0 -off | 1 - min | 2 - detailed | 3 - debug

#open binary
count = 0
L = ""

if printFlag == 3:
  print("Reading in file:")

with open(inputF) as inFile:
     
    while True:
         
        # Read from file
        c = inFile.read(bitCount)
        count += 1

        if not c:
            break
 
        # print the character
        if printFlag == 3:
            print("Line {}: {}".format(count, c))
        L = L + c + "\n"


if printFlag == 3:  
  print("\n")
if printFlag == 1:  
#prints the content of L that will be written to the output file
  print("Writing to file: \n" + L)

inFile.close() 
# Writing to file

oFile = open(outputF, 'w')
oFile.writelines(L)
oFile.close()

#printing oFile
if printFlag == 2 or printFlag == 3:
  print("Writing to file:")
  oFile = open(outputF, 'r')
  count = 0

  for line in oFile:
    count += 1
  
    a = line.strip()

  	#prints in decimal while read in
    print("Line {}: {}".format(count, a))

oFile.close()


