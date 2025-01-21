health_potion = 0
gold_coins = 5
is_alive = True
line = "---------------------------------------------------------------------------------------------------------------"

hero_name = input("Hello young hero. What is your name? ")
print(f"Nice to meet you {hero_name}")
print(line)
chose_1 = input("Before we start, which hand dou you want? The 'left' or the 'right'? ")

if chose_1 == "left":
    print("The old man pulls out a knife and stabs you into your chest")
    is_alive = False
else:
    print(f"The old man gives you a health potion, smiles at you and say 'The luck is on your side, go now {hero_name}'!")
    health_potion += 1
    print(line)

if is_alive:
    print("You take the health potion and follow the old path.")
    chose_2 = input("You find an old lady, sitting right next to the path. Maybe some coins would help."
                    "Will you give her some coins 'c' or walk further 'w'? ")
    print(line)

    if chose_2 == "c":
        gold_coins -= 3
        print("You give the old lady some coins. She looks at you an give you a book but she don't say anything.")
        print(f"Now you have {gold_coins} gold coins left.")
        print(line)
    else:
        print("The old lady transform her into a dragon and kills you")
        is_alive = False

