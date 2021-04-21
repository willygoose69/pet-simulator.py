# pet simulator
#user config
cheats='false'
money100='false'
health100='false'
love100='false'
clean100='false'
hunger100='false'
autowin='false'

#default variables
health=50
clean=50
hunger=50
love=50
turn=0
work=0
workturn=-1
bal=0
salary=0
points=0
inventory=[]
#salaries
mod=126
mom=243
#more soon maybe



#setup
#import
import random
#type
type=0
print("what pet would you like?")
while(type==0):
    type=input("dog, cat: ")
    if(type=="dog"): continue
    elif(type=="cat"): continue
    else: type=0

#name
name=input("what would you like to name your new pet " + type + "? ")
print("say hello to your new " + type + ", " + name + "!")

#levels
hungerlevel=0.96 #adds by 0.004 until it is 1
cleanlevel=0.99 #adds by 0.001 until it is 1
healthlevel=0.98 #adds by 0.002 until it is 1
lovelevel=0.97 #adds by 0.003 until it is 1

#setup complete
#game
while(not type==0):
    print("") # skip line after previous command

#variables
    temp = health
    health=(temp*healthlevel)
    temp = hunger
    hunger=(temp*hungerlevel)
    temp = love
    love=(temp*lovelevel)
    temp = clean
    clean=(temp*cleanlevel)
    temp = turn
    turn = temp+1
    temp = random.randrange(0,20)
    if(temp==20):
        temp=points+1
        points=temp

#op
    if(money100=='true'):
        bal=99999
    if(love100=='true'):
        love=99999
    if(clean100=='true'):
        clean=99999
    if(health100=='true'):
        health=99999
    if(hunger100=='true'):
        hunger=99999

#win check
    if (hungerlevel==1 and healthlevel==1 and lovelevel==1 and cleanlevel==1):
        print("you beat the game lol")
        temp=input("would you like to enable cheats? (y/n): ")
        if temp=="y":
            cheats='true'
            print("to use cheats: cheats help")
        print("")
        print("would you like to enable auto regen?")
        print("combine letters into input:")
        print("h - hunger")
        print("f - food")
        print("c - clean")
        print("l - love")
        temp=input("example - hf - for infinate health and food: ")
        if "h" in temp:
            health100='true'
            print("added health")
        if 'f' in temp:
            hunger100='true' 
            print("added hunger")
        if "c" in temp:
            clean100='true'
            print("added clean-ness")
        if 'l' in temp:
            love100='true' 
            print("added love")
        print()
        print("to return to this menu, use command: wincheck")



#warnings
    if(health<=30):
        print("pet health is at " + str(health) + ", please seek medical attention.")
        if(int(health)<=20):
            temp = healthlevel
            healthlevel=(0.8/health)
            temp2 = healthlevel
            healthlevel=(temp2*temp)
            temp2 = healthlevel
            healthlevel=(temp-temp2)
            print("your pet's sickness has decreased the health level from " + str(temp) + " to " + str(healthlevel) + ". please heal your pet before health is lower than 5.")
        if(int(health)<=5):
            exit("your pet has died due to low health. rip")
        else:
            print("health level will fall when it is under 20.")
    if(hunger<=15):
        print("pet is hungry, please feed it.")
        if(hunger<=10):
            temp=health
            health=temp-10
            print("due to your pet being hungry, it has taken 10 damage from "+str(temp)+" to "+str(health)+".")
    if(clean<=25):
        print("pet is dirty, please clean it before it feels unloved.")
        if(clean<=10):
            temp=love
            love=temp-10
            print("due to your pet being unclean, it has your pet feels 10 points less loved, from "+str(temp)+" to "+str(love)+".")
    if(love<=25):
        print("pet feels unloved, please play with it or buy it something.")
        if(love<=15):
            temp = healthlevel
            healthlevel=(0.4/love)
            temp2 = healthlevel
            healthlevel=(temp2*temp)
            temp2 = healthlevel
            healthlevel=(temp-temp2)
            print("the lack of love has decreased the health level from " + str(temp) + " to " + str(healthlevel) + ".")
        else:
            print("love is at "+str(love)+". health level will fall when it is under 15.")
            if(love<=15):
                temp=love
                health=temp-10
                print("health level fell by 10 due to low love levels. please play with pet.")

#help, start
    print("")
    command=input("enter command, or 'help': ")
    print("")

    if command==("help"):
        print("commands available:")
        print("help - shows this screen") #done
        print("pat - pats the pet") #done
        print("play - plays with your pet") #done
        print("shop - displays available items to buy") #done
        print("buy - use to buy things") #done
        print("use - to use a thing") #done
        print("balance - shows all avaliable coins") #done
        print("work - askes you to do stuff for coins") #done
        print("home - ur mom shows up")
        print("stats - shows pet statistics") #done
        print("doctor - use the doctor to heal pet") #done
        print("chef - use the chef to feed your pet") #done
        print("upgrade - upgrades resilience for any of the prompted categories") #done
        print("inventory - to show your inventory") #done

#wincheck menu
    elif (command=="wincheck" and hungerlevel==1 and healthlevel==1 and lovelevel==1 and cleanlevel==1):
        print("you beat the game lol")
        temp=input("would you like to enable cheats? (y/n): ")
        if temp=="y":
            cheats='true'
            print("to use cheats: cheats help")
        print("")
        print("would you like to enable auto regen?")
        print("combine letters into input:")
        print("h - hunger")
        print("f - food")
        print("c - clean")
        print("l - love")
        temp=input("example - hf - for infinate health and food: ")
        if "h" in temp:
            health100='true'
            print("added health")
        if 'f' in temp:
            hunger100='true' 
            print("added hunger")
        if "c" in temp:
            clean100='true'
            print("added clean-ness")
        if 'l' in temp:
            love100='true' 
            print("added love")
        print()
        print("to return to this menu, use command: wincheck")
#play
    elif(command==("pat")):
        print("you pat "+name+".")
        temp=love
        love=(temp+15)
    elif(command=="play"):
        temp=random.randrange(0,20)
        temp2=random.randrange(0,2)
        if(temp2==1):
            temp2=int(input("enter number below "+str(temp)+": "))
            if(temp2<temp):
                print("you played with "+name+". ")
                temp=love
                love=(temp+25)
            else:
                print("no, idiot. i said a number under "+str(temp)+". are you stupid?")
        else:
            temp2=int(input("enter number above "+str(temp)+": "))
            if(temp2>temp):
                print("you played with "+name+". ")
                temp=love
                love=(temp+25)
            else:
                print("no, idiot. i said a number over "+str(temp)+". are you stupid?")
   
#work
    elif(command=="work list"):
        print("list of currently available jobs:")
        print("discord mod - "+str(mod)+" coins")
        print("mom - "+str(mom)+" coins")

    elif(command=="work quit"):
        print("you have quit your job. please wait 5 turns before getting another.")
        workturn=work+5

    #job picker
    elif(command=="work discord mod" or command=="work mod"):
        if(work==0):
            if(workturn<turn):
                print("congrats on the new job, your salary is now",str(mod),"coins!")
                salary=mod
                work=("discord mod")
            else:
                print("you only just quit your job, wait "+str(workturn-turn)+" turns to get a new one.")
        else:
            print("you already have a job, fucking nitwit. ")

    elif(command=="work mom"):
        if(work==0):
            if(workturn<turn):
                print("congrats on the new job, your salary is now",str(mom),"coins!")
                salary=mom
                work=("mom")
            else:
                print("you only just quit your job, wait "+str(workturn-turn)+" turns to get a new one.")
        else:
            print("you already have a job, fucking nitwit. ")


    elif(command=="work"):
        if(work==0):
            if(turn>=workturn):
                print("you do not have a job. use 'work list' to find one.")
            else:
                print("ur mom is a job, wait "+str(workturn-turn)+" turns.")
        else:
            print("job for "+work+": ")
            if(turn>=workturn):
                #mod
                if(work=="discord mod"): 
                    temp=random.randrange(1,13)
                    if(temp==1):
                        answer=input("spongebob posted nsfw in genral! ban/kick/mute: ")
                        correct=("ban")
                    elif(temp==2):
                        answer=input("johnny stole 500,000 coins from @urmomgae69#4206! ban/kick/rob: ")
                        correct=("rob")
                    elif(temp==3):
                        answer=input("ashton typed '0' in chat, followed by a 'j'! ban/kick/mute: ")
                        correct=("mute")
                    elif(temp==4):
                        answer=input("urmom#6969 put 'ur mom gay' in chat! ban/warn/mute: ")
                        correct=("warn")
                    elif(temp==5):
                        answer=input("little ronny uploaded a dick pick to nsfw. it's somehow smaller than yours. bully/delete/warn: ")
                        correct=("bully")
                    elif(temp==6):
                        answer=input("anthony entered 'kys' into general and made dad bot mad. warn/ignore/kick ")
                        correct=("ban")
                    elif(temp==7):
                        answer=input("fill in the blank: i haven't slept in 3 ____. ")
                        correct=("days")
                    elif(temp==8):
                        answer=input("fill in the blank: i hold the _____. ")
                        correct=("power")
                    elif(temp==9):
                        answer=input("fill in the blank: respect me or i will ____ you. ")
                        correct=("mute")
                    elif(temp==10):
                        answer=input("True or False: 'i am a useful member of society' ")
                        correct=("true")
                    elif(temp==11):
                        answer=input("True or False: 'i haven't left home in 5 weeks' ")
                        correct=("true")
                    elif(temp==12):
                        answer=input("True or False: 'i have no life' ")
                        correct=("false")
                    elif(temp==13):
                        answer=input("True or False: 'everyone respects me' ")
                        correct=("true")
                    workturn=turn+5

                    #answer checker. (answer is user input, and correct is the accurate answer) checker can be copied elsewhere.
                    if(answer==correct):
                        temp2=salary*2
                        print("great! you get "+str(temp2)+" coins for your turn of work")
                        print("your salary was increased by 5%")
                        temp=bal
                        bal=temp+temp2
                        temp=salary
                        salary=temp*1.05
                    else:
                        print("you are bad. the answer was '"+correct+"'.")
                        print("you get "+str(salary)+" coins for your turn of work")
                        print("your salary was decreased by 10%")
                        temp=bal
                        bal=temp+salary
                        temp=salary
                        salary=temp*0.9
                    workturn=turn+5


                #mom
                elif(work=="mom"):
                    temp=random.randrange(1,13)
                    if(temp==1):
                        answer=input("little timmy killed your husband. kill/calm: ")
                        correct=("kill")
                    elif(temp==2):
                        answer=input("little timmy stole 500,000 coins from your wallet. kill/calm: ")
                        correct=("kill")
                    elif(temp==3):
                        answer=input("little timmy says he is gay. kill/calm: ")
                        correct=("calm")
                    elif(temp==4):
                        answer=input("little timmy died. cry/ignore: ")
                        correct=("ignore")
                    elif(temp==5):
                        answer=input("you see little timmy's dick pic on pornhub. kill/ignore: ")
                        correct=("ignore")
                    elif(temp==6):
                        answer=input("fill in the blank: 'tim, _____ your game of fortnite and come down here!' ")
                        correct=("pause")
                    elif(temp==7):
                        answer=input("fill in the blank: 'how do i turn off my ____ again?' ")
                        correct=("ipad")
                    elif(temp==8):
                        answer=input("fill in the blank: 'i love playing _____ crush.' ")
                        correct=("candy")
                    elif(temp==9):
                        answer=input("fill in the blank: 'can i speak to your _______!' ")
                        correct=("manager")
                    elif(temp==10):
                        answer=input("True or False: 'i am a true feminist.' ")
                        correct=("false")
                    elif(temp==11):
                        answer=input("True or False: 'i have been home cleaning all year.' ")
                        correct=("true")
                    elif(temp==12):
                        answer=input("True or False: 'i have no life' ")
                        correct=("true")
                    elif(temp==13):
                        answer=input("True or False: 'everyone respects me' ")
                        correct=("false")

                    #answer checker. (answer is user input, and correct is the accurate answer) checker can be copied elsewhere.
                    if(answer==correct):
                        temp2=salary*2
                        print("great! you get "+str(temp2)+" coins for your turn of work")
                        print("your salary was increased by 5%")
                        temp=bal
                        bal=temp+temp2
                        temp=salary
                        salary=temp*1.05
                    else:
                        print("you are bad. the answer was '"+correct+"'.")
                        print("you get "+str(salary)+" coins for your turn of work")
                        print("your salary was decreased by 10%")
                        temp=bal
                        bal=temp+salary
                        temp=salary
                        salary=temp*0.9
                    workturn=turn+5
            else:
                print("ur mom is a job, wait "+str(workturn-turn)+" turns.")

#use
    elif(command=="use"):
        print("you need to use command: (use [itemname]).")
        print("make sure you have that item in your inventory. command: (inventory)")
        print("if not, buy the item. command: (buy [itemname]).")
        print("to see all items for sale, use command: (shop)")
    elif(command=="use dog toy"):
        if "dog toy" in inventory:
            if(type=="dog"):
                temp=random.randrange(1,3)
                if temp==1:
                    print("your dog happily played with the dog toy.")
                    love=love+30
                    health=health+30
                    print("health:",health)
                    print("love:",love)
                else:
                    print("your dog played with the dog toy and broke it.")
                    love=love+25
                    health=health+35
                    print("health:",health)
                    print("love:",love)
                    inventory.remove("dog toy")
            else: print("your",type,"hates the toy. why the fuck would you buy it a dog toy?")
        else: print("its not even in your inventory noob.")
    elif(command=="use string"):
        if "string" in inventory:
            if(type=="cat"):
                temp=random.randrange(1,3)
                if temp==1:
                    print("your cat happily played with the string.")
                    love=love+30
                    health=health+30
                    print("health:",health)
                    print("love:",love)
                else:
                    print("your cat played with the string and snapped it.")
                    love=love+25
                    health=health+35
                    print("health:",health)
                    print("love:",love)
                    inventory.remove("string")
            else: print("your",type,"hates the toy. why the fuck would you buy it a string")
        else: print("its not even in your inventory noob.")
    elif command=="use mouse":
        if "mouse" in inventory:
            if(type=="cat"):
                temp=random.randrange(1,5)
                if temp==1:
                    print("your cat happily ate the mouse then got sick")
                    love=love+20
                    health=health-30
                    print("health:",health)
                    print("love:",love)
                else:
                    print("your cat played with the mouse until it died then ate it.")
                    love=love+45
                    hunger=health+55
                    print("hunger:",health)
                    print("love:",love)
            else: print("your",type,"ignores the mouse and it runs away. why the fuck would you buy it that")
            inventory.remove("mouse")
        else: print("its not even in your inventory noob.")
    elif command=="use cat food":
        if "cat food" in inventory:
            if type=="cat":
                hunger=hunger+45
                inventory.remove("cat food")
                print("your cat happily ate the cat food. hunger:",hunger)
            else:
                print("your dog decided to throw the cat food in the trash as it is not for dogs.")
                inventory.remove("cat food")
        else: print("its not even in your inventory noob.")
    elif command=="use dog food":
        if "dog food" in inventory:
            if type=="dog":
                hunger=hunger+45
                inventory.remove("dog food")
                print("your dog happily ate the dog food. hunger:",hunger)
            else:
                print("your cat is sad because you tried to feed it dog food.")
                inventory.remove("dog food")
        else: print("its not even in your inventory noob.")
    elif command=="use medical kit":
        if "medical kit" in inventory:
            if health<100:
                health=100
                print("you healed your pet to 100 health")
            else: print("your health is already",str(health),". why the fuck would you use this medical kit?")
        else: print("its not even in your inventory noob.")
    elif command=="use instant food and health" or command=="use instant food" or command=="use instant health":
        if "instant food and health" in inventory:
            hunger=hunger+100
            health=health+100
            print("hunger:",hunger)
            print("health:",health)
        else: print("its not even in your inventory noob.")
    elif command=="use magic soap":
        if "magic soap" in inventory:
            if clean<100:
                clean=clean+100
                print("clean-ness:",clean)
            else: print("your clean-ness is already",str(clean),". why the fuck would you use this magic soap?")
        else: print("its not even in your inventory noob.")

#stats commands
    elif(command==("stats")):
        print("==STATS==")
        print("name: "+name)
        print("species: "+type)
        print("turn: "+str(turn))
        print()
        print("==HEALTH==")
        print("health: "+str(health))
        print("level: "+str(healthlevel))
        print("your pet will die when you hit 5 health, and health level will be decreased when under 20 depending on how much health left.")
        print()
        print("==HUNGER==")
        print("hunger: "+str(hunger))
        print("level: "+str(hungerlevel))
        print("your pet will take 10 damage per turn when hunger hits 10.")
        print()
        print("==CLEANESS==")
        print("cleaness: "+str(clean))
        print("level: "+str(cleanlevel))
        print("your pets love will decrease by 10 per turn when this hits 0.")
        print()
        print("==LOVE==")
        print("love: "+str(love))
        print("level: "+str(lovelevel))
        print("your pet's health level will be decreased depending on how much love it has left when value falls below 15.")
        print()
        print("==OWNER==")
        print("salary: "+str(salary))
        print("balance: "+str(bal))
        print("your salary will increase by 5 percent when you do well at your job, but drop by 10 percent if you don't.")
    elif(command=="balance"):
        print("balance: "+str(bal))
        print("to earn money, use 'work'")
        print("to use money, use 'shop', then 'buy'")
    elif(command=="inventory"):
        print("items in inventory: ")
        print(inventory)

#shop and buy
    #shop
    elif(command=="shop"):
        print("==SHOP==")
        print("dog toy - 50 coins") #done
        print("string - 50 coins") #done
        print("mouse - 70 coins") #done
        print("cat food - 120 coins") #done
        print("dog food - 110 coins") #done
        print("medical kit - 370 coins") #done
        print("instant food and health - 995 coins") #done
        print("magic soap - 340 coins") #done
        print("use 'buy' to buy")
    
    #buy

    #dog toy
    elif(command=="buy dog toy"):
        cost=50
        item="dog toy"
        if(bal>cost):
            print("you bought a "+item+" for "+str(cost)+" coins.")
            temp=bal
            bal=bal-cost
            inventory.append(item)
        else:
            print("you don't even have "+str(cost)+". what a fucking normie.")
    
    #string
    elif(command=="buy string"):
        cost=50
        item="string"
        if(bal>cost):
            print("you bought a "+item+" for "+str(cost)+" coins.")
            temp=bal
            bal=bal-cost
            inventory.append(item)
        else: print("you don't even have "+str(cost)+". what a fucking normie.")

    #mouse
    elif(command=="buy mouse"):
        cost=70
        item="mouse"
        if(bal>cost):
            print("you bought a "+item+" for "+str(cost)+" coins.")
            temp=bal
            bal=bal-cost
            inventory.append(item)
        else: print("you don't even have "+str(cost)+". what a fucking normie.")
    
    #cat food
    elif(command=="buy cat food"):
        cost=120
        item="cat food"
        if(bal>cost):
            print("you bought a "+item+" for "+str(cost)+" coins.")
            temp=bal
            bal=bal-cost
            inventory.append(item)
        else: print("you don't even have "+str(cost)+". what a fucking normie.")

    #dog food
    elif(command=="buy dog food"):
        cost=110
        item="dog food"
        if(bal>cost):
            print("you bought a "+item+" for "+str(cost)+" coins.")
            temp=bal
            bal=bal-cost
            inventory.append(item)
        else: print("you don't even have "+str(cost)+". what a fucking normie.")

    #medical kit
    elif(command=="buy medical kit"):
        cost=370
        item="medical kit"
        if(bal>cost):
            print("you bought a "+item+" for "+str(cost)+" coins.")
            temp=bal
            bal=bal-cost
            inventory.append(item)
        else: print("you don't even have "+str(cost)+". what a fucking normie.")

    #instant food and health
    elif(command=="buy instant food and health"):
        cost=995
        item="instant food and health"
        if(bal>cost):
            print("you bought a "+item+" for "+str(cost)+" coins.")
            temp=bal
            bal=bal-cost
            inventory.append(item)
        else: print("you don't even have "+str(cost)+". what a fucking normie.")

    #magic soap
    elif(command=="buy magic soap"):
        cost=340
        item="magic soap"
        if(bal>cost):
            print("you bought a "+item+" for "+str(cost)+" coins.")
            temp=bal
            bal=bal-cost
            inventory.append(item)
        else: print("you don't even have "+str(cost)+". what a fucking normie.")

#upgrade
    elif command==("upgrade"):
        if bal<1000: print("lol you don't even have 1000")
        else:
            bal=bal-1000
            temp=input("this costs 1000. select category: health, hunger, clean, love, cancel. ")
            print()
            if temp=="health":
                if healthlevel<1:
                    temp2=healthlevel
                    healthlevel=temp2+0.002
                    print("health level is now "+str(healthlevel)+".")
                else: print("health level is already 1")
            elif temp=="hunger":
                if hungerlevel<1:
                    temp2=hungerlevel
                    hungerlevel=temp2+0.004
                    print("hunger level is now "+str(hungerlevel)+".")
                else: print("hunger level is already 1")
            elif temp=="clean":
                if cleanlevel<1:
                    temp2=cleanlevel
                    cleanlevel=temp2+0.001
                    print("clean level is now "+str(cleanlevel)+".")
                else:
                    print("clean level is already 1")
            elif temp=="love":
                if lovelevel<1:
                    temp2=lovelevel
                    lovelevel=temp2+0.003
                    print("love level is now "+str(lovelevel)+".")
                else:
                    print("love level is already 1")
            else:
                bal=bal+1000
                print("cancelled")
                continue

#special
    elif command==("doctor"):
        temp=random.randrange(1,30)
        if not temp==1:
            temp=(100-health)
            health=100
            print("doc has healed your pet by "+str(temp)+" points! make sure to take care of it and use the first aid kit!")
            cost=random.randrange(100,1000)
            if bal<cost:
                print("the doctor requires "+str(cost)+" coins. you only have "+str(bal)+("."))
                print("guess you'll die")
                exit()
            else:
                bal=temp2
                bal=temp2-cost
                print("the doctor has charged "+str(cost)+" for his service. you now have only "+str(bal)+".")
        else:
            print("SHIT! doc has accidentally killed your pet because he chose a random number between 1 and 30 and it was 1.")
            print("lol guess you lost the game")
            exit()
    elif command==("chef"):
        temp=(100-health)
        health=100
        print("chef has fed your pet by "+str(temp)+" points! make sure to take care of it and buy some food!")
        cost=random.randrange(100,1000)
        if bal<cost:
            print("the doctor requires "+str(cost)+" coins. you only have "+str(bal)+("."))
            print("guess you'll die")
            exit()
        else:
            bal=temp2
            bal=temp2-cost
            print("the doctor has charged "+str(cost)+" for his service. you now have only "+str(bal)+".")

#cheat
    elif("cheat" in command):
        if(cheats=="true"):
            if("love" in command):
                love=1000
            if("hunger" in command):
                hunger=1000
            if("health" in command):
                health=1000
            if("clean" in command):
                clean=1000
            if("bal" in command):
                bal=10000
        else:("cheats not enabled")

#misc
    elif command==("exit"):
        temp=input("are you sure you want to exit? y/n: ")
        if(temp=="y"):
            exit()
    elif command==("save"):
        #make it output code to save
        print("work in progress...")

#footer
    else:
        print("command not found, enter 'help' for help.")