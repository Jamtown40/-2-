# Python
# Movie Theater
# Two people walk into a movie theater to watch a movie.

#1. Input:
print("> Welcome to Rave Intergalactic Cinemas! \n> Please fill out the following information on our NextGen Fire Stylus 6.0!")
print("---------------------------------------------------------------------------")
print("Movie Menu: ")
print("1. Avatar\n2. Oppenheimer\n3. Bladerunner\n4. Sneakers\n5. Pineapple Express ")
print("---------------------------------------------------------------------------")
print("Information: ")

sPerson1 = input("Customer 1) Name: ")
fPerson1 = float( input("Customer 1) Age: "))
sPerson1Status = input("Customer 1) Status: Child, Teen, Adult: ")
sPerson2 = input("Customer 2) Name: ")
fPerson2 = float( input("Customer 2) Age: "))
sPerson2Status = input("Customer 2) Status: Child, Teen, Adult: ")

print("---------------------------------------------------------------------------")
print("> Thank you for choosing Rave Intergalactic Cinemas! ")
print("---------------------------------------------------------------------------")

#2 Age Constants:
ACCEPTABLE_RATED_R_ADMISSION = 18.0
CHILD_ADMISSION = 4.0
TEEN_ADMISSION = 8.0
ADULT_ADMISSION = 12.0
CREATOR_ADMISSION = 0.0
INSPECTOR_ADMISSION = 0.0

#3. Calculations:
fLowestAgeAcceptableInTheater = (ACCEPTABLE_RATED_R_ADMISSION / 2)

#4. Conditionals:
if fPerson1 < fLowestAgeAcceptableInTheater or fPerson2 < fLowestAgeAcceptableInTheater :
    print("One or both of you are less than", fLowestAgeAcceptableInTheater)
    print("You are unable to watch the movie.")
    raise SystemExit

if fPerson1 >= ACCEPTABLE_RATED_R_ADMISSION or fPerson2 >= ACCEPTABLE_RATED_R_ADMISSION:
    print("> Good news! You both meet the age requirement. ")

if fPerson1 > fPerson2:
    fOlder = fPerson1
    fYounger = fPerson2
else:
    fOlder = fPerson2
    fYounger = fPerson1
    
if sPerson1 == "Tim":
    print(">", sPerson1, "everything here is free for you too, you're the inspector. ")

if fPerson1 == fPerson2:
    print("> You both are the same age! ")

if sPerson1 == "Ray" and sPerson1Status == "Adult":
    print(">", sPerson1, "everything is free to it's creator. ")
    
if sPerson1 == "Ray" and sPerson1Status == "Adult":
    print(">", sPerson1, "You owe:",CREATOR_ADMISSION)

if sPerson1 == "Tim" and sPerson1Status == "Adult":
    print(">", sPerson1, "You owe:",INSPECTOR_ADMISSION)

elif sPerson1Status == "Child":
    print(">", sPerson1, "You owe: $",CHILD_ADMISSION)

elif sPerson1Status == "Teen":
    print(">", sPerson1, "You owe: $",TEEN_ADMISSION)
    
elif sPerson1Status == "Adult": 
    print(">", sPerson1, "You owe: $",ADULT_ADMISSION)
    
if sPerson2Status == "Child":
    print(">", sPerson2, "You owe:",CHILD_ADMISSION)

elif sPerson2Status == "Teen":
    print(">", sPerson2, "You owe:",TEEN_ADMISSION)
    
elif sPerson2Status == "Adult": 
    print(">", sPerson2, "You owe:",ADULT_ADMISSION)    
    
#5. Logical Compare:
if  fYounger < fLowestAgeAcceptableInTheater:
     sMessage = "I'm sorry but you are too young and cannot be trusted to stay quiet in the theater. "
else:
    sMessage = "You both can be trusted to use your inside voices. "
    
#6. Output:
print(">", sPerson1, "and" ,sPerson2,":")
print("> The older age is:", format(fOlder,".1f"))
print("> The younger age is:", format(fYounger,".1f"))
print("> The absolute lowest age required to be in the movie theater is:",fLowestAgeAcceptableInTheater, "years old. ")
print(">", sMessage)
print("> Enjoy the movie! ")
