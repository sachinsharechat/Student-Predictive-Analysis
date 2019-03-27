import csv
def change(row,i):
    if i==10:
        if row[i]=='YES':
            row[i]=1
        else:
            row[i]=0
    elif i==9:
        
        if row[i]=='GENERAL':
            row[i]=1
        elif row[i]=='OBC':
            row[i]=2
        elif row[i]=='SC':
            row[i]=3
    

File=open('student_data_cs_4.csv',newline='') 
ofile=open('re_IT.csv','w',newline='')

reader = csv.reader(File)
writer = csv.writer(ofile)
row=next(reader)

writer.writerow(row)
reader.__next__()

for row in reader:
    change(row,9)
    change(row,10)
    writer.writerow(row)
    

File.close()
ofile.close()
    
