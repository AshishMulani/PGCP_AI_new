from abc import ABC,abstractmethod
from TaxPortal import TaxPayer

class Employee(ABC):
    def __init__(self,empid,name):
        self._empid=empid
        self._name=name

    @abstractmethod
    def calculate_gross(self):
        pass

    def __str__(self):
        return f'ID:{self._empid}, Name:{self._name}'
#---------------------------------------------------------------

'''single inheritance'''

# class SalariedEmployee(Employee):
#     def __init__(self,empid,name,basic):
#         # self._empid = empid
#         # self._name = name
#         super().__init__(empid,name)
#         self._basic=basic
#
#     def calculate_gross(self):
#         hra=self._basic*0.4
#         da=self._basic*0.12
#         return self._basic+hra+da
#
#     def calculate_net(self):
#         gross=self.calculate_gross()
#         pf=gross*0.12
#         return gross-pf

'''multiple inheritance'''
class SalariedEmployee(Employee,TaxPayer):
    def __init__(self,empid,name,basic,pan):
        # self._empid = empid   valid method
        # self._name = name
        Employee.__init__(self,empid,name)   #appropriate
        TaxPayer.__init__(self,pan)
        self._basic=basic

    def calculate_gross(self):
        hra=self._basic*0.4
        da=self._basic*0.12
        return self._basic+hra+da

    def calculate_net(self):
        gross=self.calculate_gross()
        pf=gross*0.12
        return gross-pf

    def calculate_tax(self):
        pass
#---------------------------------------------------------------
'''single inheritance'''
# class ContractEmployee(Employee):
#     def __init__(self, empid, name,day,rate):
#         super().__init__(empid, name)
#         self._day=day
#         self._rate=rate
#
#     def calculate_gross(self):
#         return self._day*self._rate

'''multiple inheritance'''

class ContractEmployee(Employee,TaxPayer):
    def __init__(self, empid, name,day,rate,pan):
        Employee.__init__(self,empid, name)
        TaxPayer.__init__(self, pan)
        self._day=day
        self._rate=rate

    def calculate_gross(self):
        return self._day*self._rate

    def calculate_tax(self):
        pass
#---------------------------------------------------------------
'''single inheritance'''
# class Manager(SalariedEmployee):
#     def __init__(self, empid, name, basic,allowance):
#         super().__init__(empid, name,basic)
#         self._allowance=allowance
#
#     def calculate_gross(self):
#         gross1=super().calculate_gross()+self._allowance
#         return gross1
#
#     def calculate_net(self):
#         gross=self.calculate_gross()
#         pf=gross*0.12
#         return gross-pf

'''multiple inheritance'''
class Manager(SalariedEmployee):
    def __init__(self, empid, name, basic,allowance,pan):
        super().__init__(empid, name,basic,pan)
        self._allowance=allowance

    def calculate_gross(self):
        gross1=super().calculate_gross()+self._allowance
        return gross1

    def calculate_net(self):
        gross=self.calculate_gross()
        pf=gross*0.12
        return gross-pf

    def calculate_tax(self):
        pass
#---------------------------------------------------------------

# emp1=SalariedEmployee(101,'Ashish',80000)
# print(f'{emp1}, Gross Salary:{emp1.calculate_gross()}, Net Salary:{emp1.calculate_net()}')
# display
#
# emp2=ContractEmployee(102,'Pranita',350,350)
# print(f'{emp2}, Gross Salary:{emp2.calculate_gross()}')
#
# emp3=Manager(103,'DD',90000,25000)
# print(f'{emp3}, Gross Salary:{emp3.calculate_gross()}, Net Salary:{emp3.calculate_net()}')

#-------------------------------------------------------------------------

