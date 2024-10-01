print("Welcome to 'The Queers: N and J's Journey to Henriettas'")
print("You are N, on your way to have fun at Henriettas.")
print("You find yourself at a crowded subway station. The sign reads: 'Delays on the A/C/E line.'")
choice1 = input("Do you take the 'subway' or call a 'rideshare'? ").strip().lower()

if choice1 == "subway":
    print("You descend the stairs and enter the station.")
    print("The train is delayed, and you're standing on a crowded platform.")
    action = input("Do you 'wait' for the next train or 'switch' to another line? ").strip().lower()

    if action == "wait":
        print("You wait, and after 20 minutes, the train arrives, packed with commuters.")
        action2 = input("Do you 'squeeze in' or 'wait longer' for another train? ").strip().lower()

        if action2 == "squeeze in":
            print("You manage to squeeze into the train! It's cramped, but you're on your way.")
            print("The ride is long, but you finally reach your stop.")
            action3 = input("Do you 'exit' and take a bus to Henrietta's or 'walk' the remaining distance? ").strip().lower()

            if action3 == "exit":
                print("You get off the train and call a rideshare. You arrive just in time for Chappelle Roan playing!")
                print("You win!")
            elif action3 == "walk":
                print("You decide to walk. The fresh air revives you, but it takes longer. J is annoyed that N complains about walking")
                print("You arrive a bit late but the weather was nice for a walk. Good job!")
            else:
                print("You hesitate too long, and the train leaves you behind.")
        elif action2 == "wait longer":
            print("You wait for another train, but delays worsen. You end up being late.")
            print("Both N and J are now annoyed! Better luck next time.")
        else:
            print("You couldn't decide, and the train doors close in your face.")
            print("N is now annoyed and wants to call 'rideshare'")

    elif action == "switch":
        print("You switch to another line, but it's even more crowded!")
        print("You see two options: take the 'local' line with more stops or wait for the 'express' train.")
        action2 = input("Do you take the 'local' or 'express'? ").strip().lower()

        if action2 == "local":
            print("The local train is slow, but at least you’re moving.")
            print("You arrive at Henriettas, but the line is long.")
            print("You get to line and have to wait. Should have gone to the Bush instead!")
        elif action2 == "express":
            print("The express train flies through the stations. You make it to your stop in record time!")
            print("You get there super fast. Both N and J are happy!")
        else:
            print("You stand in confusion and don't know if you should go to Henriettas or the Bush!")

elif choice1 == "rideshare":
    print("You call a rideshare, and your driver arrives in 5 minutes.")
    action = input("Do you take the 'expressway' or 'local streets'? ").strip().lower()

    if action == "expressway":
        print("The expressway looks clear, but suddenly there’s traffic ahead!")
        action2 = input("Do you ask the driver to 'exit' and take a detour, or 'stay' on the expressway? ").strip().lower()

        if action2 == "exit":
            print("The driver exits and takes a faster route. You arrive and there's barely a line!")
            print("You win!")
        elif action2 == "stay":
            print("You stay on the expressway, but the traffic worsens. You arrive late to Hennys.")
            print("They are playing all Chappelle Roan, and you're missing out. Better luck next time!")
        else:
            print("You hesitate, and your driver gets lost in the traffic. You arrive when it is all packed.")

    elif action == "local streets":
        print("The local streets are busy, but the drive feels nice.")
        action2 = input("Do you 'play music' or 'relax' quietly? ").strip().lower()

        if action2 == "play music":
            print("You play Chappelle Roan preparing for the night. The time passes quickly!")
            print("You arrive at Henriettas and feel energized for the night. You win!")
        elif action2 == "relax":
            print("You close your eyes for a quick rest. Before you know it, you've arrived!")
            print("Refreshed, you are both ready to dance. You win!")
        else:
            print("You overthink it, and the driver takes a wrong turn. You're delayed.")

else:
    print("You stand on the sidewalk, unable to decide. Time flies, and you decide to go to the Bush.")