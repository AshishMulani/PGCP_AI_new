import pickle

from Day6.EmployeePortal import (SalariedEmployee,Manager,ContractEmployee)



se=SalariedEmployee(101,'ashish',80000,'hdbh89hd')
me=Manager(102,'Pranita',80000,15500,'acdr89hd')
ce=ContractEmployee(103,'Dhriti',20,15500,'kmujm89hd')

employees=[se,me,ce]

employee_data=[]

with open('Employee.pkl','wb') as fw:
    try:
        for employee in employees:
            pickle.dump(employee,fw)
            print('data written')

    except IOError as e:
        print(e)

with open('Employee.pkl','rb') as fr:
    while True:
        try:
            data=pickle.load(fr)
            employee_data.append(data)

        except EOFError as e:
            print('EOF')
            break

for emp in employee_data:
    print(emp)