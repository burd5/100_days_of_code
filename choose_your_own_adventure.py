print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Life.")
print("Your mission is to try and figure it out.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

after_highschool = input("You just graduated from high school. Do you go to an expensive Ivy League school, enter a trade school, or take a gap year? Type 'ivy', 'trade', or 'gap'.").lower()

if after_highschool == 'ivy':
    degree = input('Bold choice. Is your degree in the humanities or STEM? Type "humanities" or "STEM".')
    if degree.lower() == 'stem':
        graduation_year = input("Did you graduate before or after 2008? Enter 'B' for before and 'F' for after.")
        if graduation_year.lower() == 'b':
            print("Whew, that was a close one. You'll probably be alright.")
        else:
            print("That's some real bad luck. Sucks to be a millenial")
    else:
        print('You done messed up. GAME OVER.')

if after_highschool == 'trade':
    union = input("Did you go join a trade job that has a union? Enter 'Y' for yes and 'N' for no.")
    if union.lower() == 'y':
        print("Nice! You are probably doing pretty well by now, unless you're a coal miner")
    elif union.lower() == 'n':
        print("Damn son, wish you had that one back. GAME OVER")
    else:
        print("That wasn't an answer.....GAME OVER")


if after_highschool == 'gap':
    travel = input("Did you take a year to travel and find yourself? Enter 'Y' for yes and 'N' for no.")
    if travel.lower() == 'y':
        location = input("Did you spend time in SE Asia, Europe, or Africa? Enter 'A' for Africa, 'SE' for Southeast Asia, 'E' for Europe, or 'N' for none of the above.")
        if location.lower() == 'SE':
            print("Classic. Should've gone to Africa. GAME OVER.")
        elif location.lower() == 'A':
            print("I admire the tenacity.")
        elif location.lower() == 'E':
            print("Better than SE Asia. We'll let it slide.")
        elif location.lower() == 'N':
            print("Huh, where'd you go?! WINNER WINNER")
    else:
        print("Then what did you do?")

