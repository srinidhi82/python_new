def main():
    student_details = {"age" : 35, "city": "Dallas", "name": "Bobby"}
    studentinfo(**student_details)
   

    x = int(input("Enter an integer to perform a square: "))
    print(f"The squre of x is", square(x))
   
    greet_person()
       
def square(n):
    return n **2           

def studentinfo(**kwargs):
    
    city = kwargs.get('city')
    age = kwargs.get('age')
    name = kwargs.get('name')
    if city and age and name:
        print(f"The student's name is {name}, from {city}, and they are {age} years old")
    else:
        print("Some student details are missing")

    


def greet_person(to = 'Joey'):
    print("Hey how are you", to)


main()