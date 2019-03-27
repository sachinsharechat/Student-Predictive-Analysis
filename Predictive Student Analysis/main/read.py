import csv
def change(row,i):
    if row[i]=='never':
        row[i]=0
    elif row[i]=='rarely':
        row[i]=1
    elif row[i]=='sometimes':
        row[i]=2
    elif row[i]=='frequently':
        row[i]=3
    elif row[i]=='always':
        row[i]=4

File=open('moody_training_data.csv',newline='') 
ofile=open('modified.csv','w',newline='')

reader = csv.reader(File)
writer = csv.writer(ofile)
row=next(reader)

writer.writerow(row)
reader.__next__()

for row in reader:
    row[2]=ord(row[2])-64
    change(row,3)
    change(row,4)
    change(row,5)
    writer.writerow(row)

File.close()
ofile.close()
    
