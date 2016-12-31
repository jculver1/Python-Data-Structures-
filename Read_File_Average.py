# Python-Data-Structures-
# This program counts the lines and extracts the floating point values from each lines and computes the average. 

fname = raw_input("Enter file name: ")

try:
	fh = open(fname)

except: 
    print "File cannot be opened: ", fname
    exit()
    
count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    number = line[-7:-1]
    now_float = float(number)
    total += now_float
    count = count + 1
average = total / count
     
print "Average spam confidence:",average
