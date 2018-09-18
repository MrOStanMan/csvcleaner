
import csv
from ast import literal_eval

def fileIntReader(readmodecsv):
    inputlist =list()
    for row in readmodecsv:
        inputlist.append((row[0]))
       
    return inputlist

def fileIntWriter(writemodecsv,fileIntReadProcess):
    newlist = list(set(fileIntReadProcess))
    for word in newlist:
        writemodecsv.writerow([word, ''])
    
def fileStringtReader(readmodecsv):
    inputlist =list()
    for row in readmodecsv:
        inputlist.append(row[0])
        
    return inputlist

def fileStringWriter(writemodecsv,fileStringReadProcess):
    newlist  = list(set(fileStringReadProcess))
    for word in newlist:
        writemodecsv.writerow(['\''+ word + '\'',''])
       
def main():

    print("\n ---------------Duplicate Removal.---------------")
    filename = input("Remove Duplicates by entering the .csv file name in the directory this program lives (Note: Results will be unordered) \n")
    contents = input(("Does the file contain(Select '1' or '2'): \n 1. Integers \n 2. Strings \n"))
    output = input ("Name file where you would like the output. (Note: Naming a non existant file will create a new one) \n")
    
    if contents == '1':

        readmodecsv=csv.reader(open(filename, newline=''))
        writemodecsv = csv.writer(open(output, 'w+', newline=''))
        fileIntWriter(writemodecsv,fileIntReader(readmodecsv))

        print("\nDuplicates Removed and output to:"  + str(output) + " Remember to remove last comma!")

    elif contents == '2':

        readmodecsv=csv.reader(open(filename))
        writemodecsv = csv.writer(open(output, 'w+', newline=''),  quoting=csv.QUOTE_NONE, escapechar=' ')
        fileStringWriter(writemodecsv, fileStringtReader(readmodecsv))

        print("\nDuplicates Removed and output to: " + str(output) + " Remember to remove last comma!")

    else:
        print("Invalid Selection")
    
    input("Press any key to end.")

if __name__== "__main__":
  try:
        main()
  except SystemExit as e:
        print('Error!', e)
        print('Press enter to exit (and fix the problem)')
        input()