import random




print("computer : ohh trainer you have been challenged by All for one")
print("computer : which of these heroes do you want to be ??")
print("a)deku\nb)todoroki\nc)bakugo")
choice = input("")
choice1 = 'a'
choice2 = 'b'
choice3 = 'c'
if choice == choice1 :
    loop = True

    while loop :
        print("All for One : Ha! Ha! Ha! you must have inherited the powers of my nemesis but you are still no where near as capable as me")
        print("choice :\na)first time playing\nb)i'm already a pro")
        play = input()
        deku_attacks_common = "moves : \n1)Delaware smash\n2)Detroit Smash"
        deku_attacks_special = "moves : \n1)Delaware smash\n2)Detroit Smash\n3)Manchester Smash"
        deku_attacks_ultimate = "moves : \n1)Delaware smash\n2)Detroit Smash\n3)Manchester Smash\n4)1,000,000% Delaware Detroit Smash"
        if play == 'a':
            all_might_text = ['\n\n\n\n\n\n\n||||All might : Hi deku !',"\n\n\n\n\n\n\n||||All might : I think you lost your memory from your previous battle" ,"\n\n\n\n\n\n\n||||All might : That's okay I'll refresh you'r memory", "\n\n\n\n\n\n\n||||All might : we currently live in a world where 99% of human beings have superpowers or as we call it now 'quirks'", "\n\n\n\n\n\n\n||||All might : you were one of the 1% who didn't have a quirk", "\n\n\n\n\n\n\n||||All might : seeing your bravery I 'All Might' gave you my quirk", "\n\n\n\n\n\n\n||||All might : now it's your turn to protect this world !", "\n\n\n\n\n\n\n||||computer : before we start I would Like to take you through how to fight", "\n\n\n\n\n\n\n\n\n\n\n\n\n\n||||this is your battle interface", "||||the first two attacks are common and can be used by you at any time","||||the 3rd one is you'r special move and can be performed by you only if you have got 5 attack points", "||||the 4th and last one is your ultimate and can only be performed if you have got 10 attack points" ]
            for i in all_might_text :
                continue_game = input("press sapce and enter to continue")
                if continue_game == ' ':
                    print(i)
                    if i == "\n\n\n\n\n\n\n\n\n\n\n\n\n\n||||this is your battle interface":
                        print("\nsuccesful hits: 0")
                        print("attack points: 0")
                        print("All for One health : 0\n\n\n\n")
                        print(deku_attacks_ultimate+"\n\n\n")
                    elif i == "||||the 4th and last one is your ultimate and can only be performed if you have got 10 attack points":
                        go_back = input("press sapce and enter to start fighting")
                        if go_back == ' ':
                            pass








        elif play == 'b':
            succesful_hits = 0
            attack_points = 0
            points = 0
            All_for_one_health = 20
            deku_health = 20
            turns = 0
            print("All for One : okay let's begin the battle !!")
            playing = True



            while playing:


                if turns % 2 == 0:
                    if All_for_one_health <= 0:
                        playing = False
                        loop = False




                    else:
                        if attack_points >= 10:
                            attack = input(deku_attacks_ultimate)
                            turns += 1


                        elif attack_points >= 5:
                            attack = input(deku_attacks_special)
                            dodge = random.randint(0, 3)
                            turns += 1
                            if dodge == 2:
                                print("\n\n\n\n||||All for One dodged it\n\n\n\n")
                                if attack == '3':
                                    attack_points -= 3
                                else :
                                    attack_points -= 1

                                print("succesfull attacks : " + str(succesful_hits))
                                print("attack points : " + str(attack_points))
                                print("All for One health : " + str(All_for_one_health))
                                print("Your Health : " + str(deku_health)+ "\n\n\n")
                            else :
                                if attack == '3':
                                    print("\n\n\n\n||||you hit him\n\n\n\n")
                                    succesful_hits += 1
                                    attack_points -= 3
                                    All_for_one_health -= 3
                                    print("succesfull attacks : " + str(succesful_hits))
                                    print("attack points : " + str(attack_points))
                                    print("All for One health : " + str(All_for_one_health))
                                    print("Your Health : " + str(deku_health)+ "\n\n\n")
                                else :
                                    print("\n\n\n\n||||you hit him\n\n\n\n")
                                    succesful_hits += 1
                                    attack_points += 1
                                    All_for_one_health -= 1
                                    print("succesfull attacks : " + str(succesful_hits))
                                    print("attack points : " + str(attack_points))
                                    print("All for One health : " + str(All_for_one_health))
                                    print("Your Health : " + str(deku_health)+ "\n\n\n")

                        else:
                            attack = input(deku_attacks_common)
                            dodge = random.randint(0, 3)
                            turns += 1
                            if dodge == 2:
                                print("\n\n\n\n||||All for One dodged it\n\n\n\n")
                                attack_points -= 1
                                print("succesfull attacks : " + str(succesful_hits))
                                print("attack points : " + str(attack_points))
                                print("All for One Health : " + '*  ' * All_for_one_health + '|' + str(All_for_one_health))
                                print("Your Health : " + '*  ' * deku_health + '|' + str(deku_health) + "\n\n\n")
                            else:
                                print("\n\n\n\n||||you hit him\n\n\n\n")
                                succesful_hits += 1
                                attack_points += 1
                                All_for_one_health -= 1
                                print("succesfull attacks : " + str(succesful_hits))
                                print("attack points : " + str(attack_points))
                                print("All for One Health : " + '*  ' * All_for_one_health + '|' + str(All_for_one_health))
                                print("Your Health : " + '*  ' * deku_health + '|' + str(deku_health) + "\n\n\n")
                        gogo = input("press space and enter to continue")
                        if gogo == ' ':
                            pass
                else:
                    if deku_health <= 0:
                        playing = False
                        loop = False
                    else:
                        All_for_one_moves = ['Air canon', 'spring like arms', 'impact recoil', 'enhanced air canon']
                        chance = random.randint(0, 6)
                        if chance > 4:
                            turns += 1
                            i = random.randint(0,1)
                            miss = random.randint(0,4)
                            print('\n\nAll for One used ' + All_for_one_moves[i]+"\n\n")
                            if miss == 3:
                                print('but you dodged it attack\n\n')
                                print("succesfull attacks : " + str(succesful_hits))
                                print("attack points : " + str(attack_points))
                                print("All for One Health : " + '*  ' * All_for_one_health + '|' + str(All_for_one_health))
                                print("Your Health : " + '*  ' * deku_health + '|' + str(deku_health) + "\n\n\n")

                            else :
                                print('ahhhh!! It hit you\n\n')
                                deku_health -= 1
                                print("succesfull attacks : " + str(succesful_hits))
                                print("attack points : " + str(attack_points))
                                print("All for One Health : " + '*  ' * All_for_one_health + '|' + str(All_for_one_health))
                                print("Your Health : " + '*  ' * deku_health + '|' + str(deku_health) + "\n\n\n")

                        elif chance == 4 or chance == 5:
                            turns += 1
                            i = 2
                            miss = random.randint(0, 4)
                            print('\n\nAll for One used ' + All_for_one_moves[i])
                            if miss == 3:
                                print('but you dodged it attack\n\n')
                                print("succesfull attacks : " + str(succesful_hits))
                                print("attack points : " + str(attack_points))
                                print("All for One Health : " + '*  ' * All_for_one_health + '|' + str(All_for_one_health))
                                print("Your Health : " + '*  ' * deku_health + '|' + str(deku_health) + "\n\n\n")


                            else:
                                print('ahhhh!! It hit you\n\n')
                                deku_health -= 3
                                print("succesfull attacks : " + str(succesful_hits))
                                print("attack points : " + str(attack_points))
                                print("All for One Health : " + '*  ' * All_for_one_health + '|' + str(All_for_one_health))
                                print("Your Health : " + '*  ' * deku_health + '|' + str(deku_health) + "\n\n\n")


                        else :
                            i = 3
                            miss = random.randint(0, 4)
                            turns += 1
                            print('\n\nAll for One used ' + All_for_one_moves[i])
                            if miss == 3:
                                print('but you dodged it attack\n\n')
                                print("succesfull attacks : " + str(succesful_hits))
                                print("attack points : " + str(attack_points))
                                print("All for One Health : " + '*  ' * All_for_one_health + '|' + str(All_for_one_health))
                                print("Your Health : " + '*  ' * deku_health + '|' + str(deku_health) + "\n\n\n")

                            else:
                                print('ahhhh!! It hit you\n\n')
                                deku_health -= 5
                                print("succesfull attacks : " + str(succesful_hits))
                                print("attack points : " + str(attack_points))
                                print("All for One Health : " + '*  ' * All_for_one_health + '|' + str(All_for_one_health))
                                print("Your Health : " + '*  ' * deku_health + '|' + str(deku_health) +"\n\n\n")




    print("Game Over!!!")

















elif choice == choice2 :
    print("hello todoroki")
elif choice == choice3 :
    print("hello bakugo")
else :
    print("please enter a valid response")