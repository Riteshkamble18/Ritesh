students = []

def add_student():
    Name = input("Enter Student Name :- ")
    Roll = int(input("Enter Student Roll Number :- "))
    Marks = float(input("Enter Student Marks :- "))
    Address = input("Enter Student Address :- ")
    stud = {"Name" :Name , "Roll" : Roll , "Marks" : Marks , "Address" :Address}
    students.append(stud)
    print(f"{stud} ADDED SUCCESSFULLY..!") 

def view_student():
    
      if students:
       print("All Students\n")
       for s in students:
           print(f"Name:- {s["Name"]} , Roll:- {s["Roll"]} , Marks:- {s["Marks"]}, Address:- {s["Address"]}")
      else:
        print("NO Student Found..!")
   
    
def search_student():
    def search_student():
    roll = int(input("Enter Student Roll Number :- "))
    found = False
    for s in students:
        if s["Roll"] == roll:
            print(f"Student Found: Name: {s['Name']}, Marks: {s['Marks']}, Address: {s['Address']}")
            found = True
            break
    if not found:
        print("Student Not Found..!")

def update_student():
   roll = int(input("Enter Student Roll Number :- "))
   for s in students:
      if s["Roll"] == roll:
         s["Name"] = input("Enter New Student Name :- ")
         s["Marks"] = float(input("Enter New Student Marks :- "))
         s["Address"] = input("Enter New Student Address :- ")
         print(f"Student Updated Successfully..! {s}")
         return
      else:
         print("Student Not Found..!")
         

def delete_student():
    try:
       roll = int(input("Enter Student Roll Number :- "))
       for s in students:
         if s["Roll"] == roll:
            students.remove(s)
            print("Student Deleted Successfully..!")
            return
       print("Student Not Found\n")
    except ValueError:
       print("Inavid Roll Number.! Please Check You Entered is Not integer value..! ")
       

while True:
    print("***..STUDENT MANAGEMENT SYSTEM..***")
    print("1.Add Student")
    print("2.View Student")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.EXIT")

    choice = input("ENTER A NUMBER (1-5) :- ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        search_student()
    elif choice == '4':
       update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print(" YOU ARE EXITING STUDENT MANAGEMENT SYSTEM..!")
        break
    else:
        print("invalid Choice Number please Try Again..!")
