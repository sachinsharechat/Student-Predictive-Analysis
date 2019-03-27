import re
import sys
from robobrowser import RoboBrowser
var=1402710016
orignal=sys.stdout
for i in range(1):
    ofile=open('data/'+str(var)+'.txt','w')
    #sys.stdout=ofile
    br=RoboBrowser()
    br.open("http://10.10.156.201/login-student.php")
    form=br.get_form('password-form')
    form['username1'].value=var
    form['password'].value=str(var)
    br.submit_form(form)
    container=br.find_all('table')
    print(container)

    ofile.close()
    var+=1
