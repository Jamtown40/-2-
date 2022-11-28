#Python
#Realm Night Club

#1. Input:
sName = input("(Baxter) Hello goodman, nice to meet you. Welcome to Realm! My name is Baxter, I'm the bartender here. What's your name? > ")
sDrink = input("(Baxter) Very good sir, it is an honor to meet your acquaintance. What would you like to drink? (Choose: Beer, Cocktail, Wine, Cranberry Juice) > ")
iDrink = int(input("(Baxter) Just the one drink sir? You look like the type that can drink all night! Tell me, how many do you really want? > "))
sMan = input("(Baxter) Now that's the spirit! If you haven't noticed, we're not on Earth anymore so the gravity here tends to get a bit wonky. Quick, I saw you talking to that man through the window just there in the other room... what was his name? > ")
sVictim = input("(Baxter) Jolly good sir! I shall throw one of the drinks you ordered at the man and see if he catches it with the gravity adjustment! > ")
sThrow = input("(Baxter) Should I throw the drink? (y/n) > ")
nWeight = float(input("(Baxter) And by the way, like I said before the gravity here tends to get a bit wonky so you might want to enter your weight on your stylus that you got there. I think you'll find it a handy resource, you don't want to walk into the wrong room! Enter your weight: > "))

#2. Surface gravity Factor:
BARROOM = 0.57
DININGROOM = 0.72
BATHROOM = 0.44
KITCHEN = 1.52

#3. Calculations:
f_barroom = nWeight * BARROOM
f_diningroom = nWeight * DININGROOM
f_bathroom = nWeight * BATHROOM
f_kitchen = nWeight * KITCHEN

#4. Condtionals:
if sThrow == "y":
    print("(Narrator) WHOOSH! The glass cuts the man's neck and he bleeds out on the floor.")
elif sThrow == "n":
    print("(Baxter) You're no fun.")
if sDrink == "Beer":
    print("(Baxter) Fine choice sir. Suds it is!")
elif sDrink == "Cocktail":
    print("(Baxter) You're in for a wild ride!")
elif sDrink == "Wine":
    print("(Baxter) You're a scholar and a mench goodman!")
elif sDrink == "Cranberry Juice":
    print("(Drunk Guy #1) What are you on your period?")
if iDrink <= 3:
    print("(Narrator) You chug your measley numbered drinks and feel a slight buzz.")
elif iDrink <= 8:
    print("(Narrator) You chug your manly beverage and are ready for wherever the night leads you.")
elif iDrink <= 15:
    print("(Narrator) You chug your drinks like an animal and start feeling very intoxicated.")
else:
    print("(Narrator) You chug all your drinks and fight everyone at the bar.")
    
#5. Output:
print("(Stylus)" ,sName,"here is your weight in each room in this building: ")
print(f"Your weight in Bar:           {f_barroom:5,.1f} lbs")
print(f"Your weight in Dining Room:   {f_diningroom:5,.1f} lbs")
print(f"Your weight in Bathroom:      {f_bathroom:5,.1f} lbs")
print(f"Your weight in Kitchen:       {f_kitchen:5,.1f} lbs")
print(f"Your weight in Earth:         {f_earth:5,.1f} lbs")
