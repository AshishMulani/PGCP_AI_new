from EmployeePortal import (Employee,SalariedEmployee,ContractEmployee,Manager)

class Payroll:

    @staticmethod
    def display_gross(employee:Employee):
        print(employee.calculate_gross())

    @staticmethod
    def display_net(employee: SalariedEmployee):
        print(employee.calculate_net())

se=SalariedEmployee(101,'ashish',80000,'hdbh89hd')
me=Manager(101,'Pranita',80000,15500,'acdr89hd')
ce=ContractEmployee(101,'Dhriti',20,15500,'kmujm89hd')

print(se)
Payroll.display_gross(se)
Payroll.display_net(se)
print('==================================')

print(me)
Payroll.display_gross(me)
Payroll.display_net(me)
print('--------------------------------')

print(ce)
Payroll.display_gross(ce)
print('--------------------------------')

# for i in se,me,ce:
#     print(payroll.display_gross(i))
#     if isinstance(i,SalariedEmployee):
#         print(payroll.display_net(i))
