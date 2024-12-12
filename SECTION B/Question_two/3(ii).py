def grade_student():
    
    #Capture stdent mark
    mark = int(input("enter mark  scored:\t"))

    #testing student mark
    if mark>=90 and mark<=100:
        print("Grade is A")
    elif mark>=80 and mark<=89:
        print("Grade is B")
    elif mark>=70 and mark<=79:
        print ("Grade is C")
    elif mark>=60 and mark <=69:
        print ("Grade is D")
    else:
        print("F")

#call the function
grade_student()
## Modifying the 
def grade():
 if grade == 'A':

          print('\n...Your grade is...')
          grade = int(input("Enter your grade: "))


 if grade >= 'B':
    print(f'Execellent')
 elif grade >= 'C':
    print(F'Good')
 elif grade >= 'D':
    print('Satisfactory')
 else:
    print(f'Needs  Improvement')  
grade()      
