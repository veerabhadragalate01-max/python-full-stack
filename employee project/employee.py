Employees=[
    
    {
       'EM_name':'surendar',
       'EM_ID ':101,
       'position':'HR',
       'base_salary':35000
    },
    {
        
       'EM_name':'surya',
       'EM_ID ':103,
       'position':'devloper',
       'base_salary':30000
    },
    {
        
       'EM_name':'jenny',
       'EM_ID ':104,
       'position':'tester',
       'base_salary':37000
       }   
    
]

def get_all_employees():
    return Employees
 
def add_Employee(EM_name,EM_ID ,position,base_salary):
   Employees.append(
      {
      
      'EM_name':EM_name,
      'EM_ID ':EM_ID,
      'position':position,
      'base_salary':base_salary
   }
      )
   
   return "employee add susscesfully"

def update_employee_details(emp_id, new_position, new_salary):
    for emp in Employees:
        if emp['EM_ID '] == emp_id:
            emp['position'] = new_position
            emp['base_salary'] = new_salary
            return "Employee updated successfully"

    return "Employee not found"
   