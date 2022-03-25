#Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.
# Use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File does not exist:', fname)
    quit()
#create dictionary
counts = dict()
#go through lines
for line in fh:
    line = line.rstrip()
    if len(line) < 1:
        continue
    if line.startswith('From '):
        linesplit = line.split()
        #isolate email
        email = linesplit[1:2]
#fill in dictionary
    for e in email :
        counts[e] = counts.get(e,0) + 1
print(counts)