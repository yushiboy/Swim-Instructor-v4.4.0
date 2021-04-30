
#NEW CUSTOMER FORM
  #STUDENT NAME "student"
  #STUDENT BIRTHDAY 
  #STUDNET AGE 
  #NAME OF PARENT 
  #CONTACT PHONE NUMBER ABILITY TO ADD LESSONS CHECK IF THEY HAVE PAID
#NUMBER OF LESSONS
#ABILITY TO SUBTRACT LESSONS FROM THE REMAINING
#NOTES ABOUT THE LESSONS

####################READY SET GO!#####################

#Sign up menu


def add_student():
        print("First off I would like to thank you for selecting me as your instructor")
        input("Student name: " , name)
        input("student birthday: " , birthday)
        input("Age of student: " , age)
        input("name of parent: ", parent)
        input("Contract number", cont_number)
        print("student: " + name)
        print("birthday: " + birthday)
        print("age: " + age)
        print("parent: " + parent)


#lesson menu

menu = {}

menu = ["1"] = "Find student"
menu = ["2"] = "Add student"
menu = ["3"] = "Archive student"
menu = ["4"] = "exit"

while True:
        options = menu.keys()
        options.sort()
        for entry in options:
                        print(entry, menu[entry])
                        selection = raw_input("Please select an option: ")
                        if selection == '1':
                                input("Student" , student)
                                find_student(student)
                        elif selection == '2':
                                print("Add student")
                                add_student()
                        elif selection == '3':
                                print("Archive student")
                                input("Student: " , student)
                                archive_student(student)
                        elif selection == '4':
                                      print("EXIT")
                        else:
                                      print("Unknown selection")
