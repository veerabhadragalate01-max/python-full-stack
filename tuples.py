# tuples 
# tuples are ordered collections  of items
#duplicates are allowed and mixed data types
# create tuples
# a=()
# b=tuple()
# c= (1,2,3, True,"hello")
# d= 2,3,4
# e=(2,)

# # Access items from tuples
# names=("alice","bob","charlie")
# # print(nmaes[0])
# #print(names[-2:-1])
#add and update /NA in tuple
# a.remove not avalable in tuple
# numbers=[34, 35, 84, 23, 19]
# numbers.sort(reverse=True)
# print(numbers)
# numbers.remove(84)
# print(numbers)
# fruits = [1,3, 56, 89]
# fruits.sort() 
# print(fruits)
# list1=["wake up", "Exercise", "work"]
# del list1[1]
# print(list1)
# delete the second task using pop
# delete the first task using remove
##print the list

# user=[33,45,108,44,100,81]
# user.sort(reverse=True)
# print(user)

# userdeatails={}
# adhar=input("enter you adhar deatails")
# pandeatails=input("enter your pan deatils")
# a=adhar.split(",")
# b=pandeatails.split(",")
# userdeatails.update
# {
    
    
# }
# print(a)    
# print(b)




details = {

    "flights": ['001', '002', '003'],

    "locations": (123223.22, 123212.22),

    "airports": {

        "HYD": "hyderabad",

        "BLR": 'bangalore'

    },

    "dishes": {'apple', 'fruit juice'}

}
 
a = {
   "user": {
       "id": 101,
       "profile": {
           "name": "John Doe",
           "contacts": {
               "email": "john@example.com",
               "phone": "+1-234-567-890",
               "location": "Hyderabad"
           },
           "settings": {
               "theme": "dark",
               "language": "English"
           }
       }
   }
}
b = {
   "company": {
       "name": "TechNova",
       "departments": {
           "engineering": {
               "teams": {
                   "backend": ["Python", "Node"],
                   "frontend": ["React", "Vue"],
                   "devops": ["AWS", "Docker"]
               },
               "head_count": 120
           },
           "sales": {
               "regions": ["APAC", "EMEA", "US"],
               "head_count": 45
           }
       }
   }
}
c = {
   "university": {
       "name": "Global Institute of Science",
       "courses": {
           "computer_science": {
               "subjects": {
                   "core": ["Data Structures", "Algorithms", "Operating Systems"],
                   "electives": ["AI", "Cybersecurity"]
               },
               "credits_required": 120
           },
           "mechanical": {
               "subjects": {
                   "core": ["Thermodynamics", "Fluid Mechanics"],
                   "electives": ["Robotics"]
               },
               "credits_required": 118
           }
       }
   }
} 

#print("user")("id")
#In b dictionary:
 
 #Print All core subjects
# Print sum of computer science credits and mechanical credits
# Change univerisity name to Global Science University
# Add 'Data Science' to computer science electives
 
 
# In dictionary a:
 
# Print 'Hyderabad'
# Print 'Doe'
# # # Print ['+1', '234', '567', '890']
 
# # # In dictioanry c:
# # # Print ['Operating Systems', 'Algorithms', 'Data structures']
# # # Print sum of credits_required in courses
print(('details')('locations')[1])