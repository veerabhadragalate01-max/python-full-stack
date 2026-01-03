from employee import get_all_employees ,add_Employee ,update_employee_details
from Attendence import get_all_em_attendance

def  showmenu():    
 print('''
          1.Add Employee
          2.Mark Attendance
          3.Recoard Workingh Hours
          4.view montly Attendance Report
          5.Calculas salary
          6.view All Employeess
          7.search Employee by Name or ID
          8.Update Employee Details
          9.Delete Employee Record
          10.Exit
           ''')
def main():
    while True:
        showmenu()
        choice=int(input("Enter your choice :"))
    
        if choice == 1:
            a=input("enter EM_name:")
            b=input("enter EM_id:")
            c=input("enter EM postion:")
            d=input("enter EM salary:")
            z=add_Employee(a,b,c,d)
            print(z)
            
        elif choice == 6:
            Employees = get_all_employees()
            print(Employees)
        
        elif choice== 8:
            # def main():
            #   print("Before update:")
            #   print(get_all_employees())
              emp_id = int(input("enter employee ID: "))
              position = input("enter new position: ")
              salary = int(input("enter new salary: "))
              h=(update_employee_details(emp_id, position, salary))
              print(h)
              print("\nAfter update:")
              print(get_all_employees())
                      
            
        elif choice == 2:
            a=get_all_em_attendance()
            print(a)
            em=input("enter a em_id:")
            day=input("enter a day:")
            b=a[em][day]
            print(b)                 
        elif choice == 10:
           breakpoint
        
if __name__=="__main__":
    main()
    
