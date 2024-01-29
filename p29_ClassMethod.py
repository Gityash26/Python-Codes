'''
=======================================================================================
____________________________________@ Class Method____________________________________
=======================================================================================
Normally when we call a method of a class with the help of its object then by default the class instance(Object) comes as first parameter and any change in the class attribute are only reflect for object reference.

But if we wants to reflect changes in attribute from class reference

ex :  class employee:
         name="Default_name"

      s=employee()

      -> s.name="Harry"
      -> employee.name="Google_Employee"

In the above example the (s.name) only reflect changes in the referene of that object not for other objects
But (employee.name) reflect change for other objects also
   
Therefore @classmethod helps to considered first parameter as class name instead of object name
'''



class employee():
    company="Apple"

    def display(self):
        print(f"\nThe Employee Name : {self.name} and Company is : {self.company}")        

    @classmethod
    def ChangeCompany(self,newCompany):
        self.company=newCompany

a=employee()
a.name="Yash"

a.display()      # The Employee Name : Yash and Company is : Apple        

a.ChangeCompany("Google")

a.display()      # The Employee Name : Yash and Company is : Google        

print(employee.company)    #Apple -> Google