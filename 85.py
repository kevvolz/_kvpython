#1 parse the From line using split() and print out the second word in the line
#  the entire address of who sent the message
#2 print out each item in list and the count at the end

name = raw_input("Enter file:")	#prompt for user to input file name
if len(name) < 1 : name = "mbox-short.txt"	#if no input entered will default to...
handle = open(name)	#handle assigned to input
lst = list()	#create list
emails = dict()	#create dictionary

for line in handle:	#for lines of text in file
	if not line.startswith("From ") : continue	#if it doesn't start with 'From ', keep going
	cut = line.split()	#add lines that do start with 'From ' to cut (list), split by spaces
	lst.append(cut[1])	#append the 2nd block of text to lst (list)
	
for addresses in lst:	#for 2nd block of text in list...
	emails[addresses] = emails.get(addresses, 0) + 1	#grab email, add (if not there) and count in dictionary

bigcount = None	#define variable for value
bigword = None	#define variable for key
for k, v in emails.items():	#for key, value in dictionary
	if bigcount is None or v > bigcount:	#if bigger or not there, replace
		bigword = k
		bigcount = v
print bigword, bigcount	#print email with highest count, and what the count is





