import os
import time
print('Welcome to the Depths Below')
time.sleep(1)
os.system("PAUSE")

print("You wake up in a dark room, without a memory to your name...\n 'What is my name?'\n")
time.sleep(3)
print('You try your hardest to remember you name, What what could it be?')
time.sleep(2)
print(' Hmm.... Hmmmm...')
time.sleep(2)
Name = input('You remember it is...\n')

if Name == "Edgar" or Name == "David" or Name == "Daniel":
 Name = input("Well, That is...intersting, {}. That couldn't possibly be your name.\n".format(Name))
 time.sleep(3)
 print('Ok, you name is {}, now that we have wasted all this time coding in this meecrob... Lets continue with the story.'.format(Name))
elif Name == "Shia LaBeouf":
    print("Welcome to die, master {}. You have nothing to fear and all is well. Your next vittim has arrived,\n"
          "Shall we begin?\n\n--------GAMEWON--------\n".format(Name))
    os.system("PAUSE")
    exit()
time.sleep(1.5)

print("You don't remeber having a voice in your head. You decide to ask it what it is and what is going on.")
time.sleep(2)
print("It tells you that it is the voice of a disembodied spirit that died here before you.\n It also informs you that you are in an underground complex that is a vampire's lair."
      "You will be it's next meal if you don't escape, but be carfeul...\n The vampire's servents, the drudge are patrolling the area to prevent your escape.")
time.sleep(10)
x = 0
y = 0
while x >= 3:
    look = input('{},Would you like to look around? [Y/N]\n'.format(Name))
    y += 1
    x += 1
    time.sleep(3)
    if look == 'Y':
        x = 3
        y = 0
    elif look == 'N':
        print('What are you waiting for, do something!')
    elif look == 'something':
       print('Smart @$$...')
    else:
        print('...Some time passes by as you ponder what to do.')


if y == 3:
    print('Good job you accomplished nothing, you die of starvation...\n\n----------GAMEOVER----------\n')
    os.system("PAUSE")
    exit()

time.sleep(5)

print('You look around the room. It has rough hewn walls of solid stone and there is a heavy door set securley into one of the walls.')
time.sleep(2)

lookm = input('You may have missed something, do you want to look more closely? [Y/N]\n')
time.sleep(3)
if not lookm == 'Y':
    print("I've wasted enough time coding this mess, lets get the hell out of here!!!")
elif lookm == 'Y':
    print('There is strange writing on the wall, all you can decipher is the letters "L E"...\n'
          'You also notice a small hole in the wall, but you cannot fit, you think you hear a faint bark come from the hole')
time.sleep(3)
ex = input('You decide to leave the room, however the door leading to the exit doesnt budge...\n Should you try to kick the door down or pick the lock [Kick/Pick]\n')
time.sleep(3)
if ex == 'Kick':
    print('You manage to bust the door ajar, but the loud noise from kicking the door alerted one of the dredge!\n'
          'You try you best to run away to no avail, the drudge wraps it mouth around your neck and drains your life force...\n\n ----------GAMEOVER----------\n')
    os.system("PAUSE")
    exit()
elif ex == 'Pick':
    print('You realize that there is nothing around to pick the lock with.\n After checking your pockets, you find a key that appears to fit the door.')
    print('The key Works!, you cautiously enter the next room')
elif ex == 'Whistle':
    print('A dog comes out of the hole in the wall and it gives you a key before running off...')
    print('You use the key to unlock the door, It worked!')
else:
    print('That typo caused a heartattack!!!, your body was later found scattered around the mysterious dungeon.\n\n----------GAMEOVER----------\n')
    os.system("PAUSE")
    exit()
time.sleep(3)
d = input('You peer cautiously into a hallway that breaks off into two directions:\n'
          'In one direction, there is a drudge guarding the a large door.\n In the other direction, there is an unguarded door.\n\n'
          'Do you try to sneek past the Drudge, or avoid pursuing the large door he is guarding [Empty/Sneak]\n')
time.sleep(5)
if d == 'Empty':
    print("You decide to avoid the vampire's servant and go down the unguarded path to the door:\n"
          "The door is unlocked and you enter into the room. It is empty except for a coffin lying in the center of the room.\n"
          "You have just wandered into the vampier's room. They awake and without a moment to waste set upon you, fangs sinking into your neck...\n\n----------GAMEOVER----------\n")
    os.system("PAUSE")
    exit()
elif d == 'Sneak':
    print('You decide to trust your sick ninja skills and try to sneak past the drudge.\n')
time.sleep(3)
dumb = input("You edge ever so slowly twards the monter by the door. You freeze. You notice that the drudge seems to have heard you as it's ears are perked up.\n"
      "Do you make a run for it and try to get past the creature quickly or do you hide and hope it dosen't notice you. [Run/Hide]\n")
time.sleep(4)
if dumb == 'Run':
    print ('You foolishly decide to make a brake for it. The drudge instantley spots you and pounces on you, tearing out your throat.\n\n--------GAMEOVER--------\n')
    os.system("PAUSE")
    exit()
elif dumb == "Hide":
    print('You wait silently in the shadows listening to the drudge droning on about annoying spiders and you manage to stay out of view.')

else:
    print('You made a typo, such mistakes will not be tolerated.\n ----------GAMEOVER---------\n\n')
    os.system("PAUSE")
    exit()
time.sleep(3)
sto = input('On your way by, you find a storage room. Should you Investigate? [Y/N]\n')
while not sto == 'Y' and not sto == 'N':
    print('Try again...')
    sto = input("Should you Investigate the Storage Room, you don't have much time before he comes back... [Y/N]\n")
    time.sleep(3)
if sto == 'Y':
    print('You dig through a pile of junk and find something useful in the rubble:\n You have aquired an Oil Lamp w/ Two Matches...\n'
          'The room behind the large door is surrounded by complete darkness')
    Oil = 1
elif sto == 'N':
    print ('You run right by the storage room without a second thought'
    'oppening the large door, you see nothing but darkness')
    Oil = 0
time.sleep(3)
if Oil == 0:
    dark = input('Do you try to navigate yourself thorough the darkness, or do you turn around and look for something that can help? {Navigate/Turn around]\n')
    while not dark == 'Navigate' and not dark == 'Turn around':
        print ('Please Input a Valid Choice')
        dark = input('"Navigate" through the dark or "Turn around" and look for something?\n')
        time.sleep(3)
    if dark == 'Navigate':
        print('You attempt to Navigate through the darkness, you feel something grab your leg!\n When you turn around, you see a creature with glowing yellow eyes\n'
        'The monster snaps your neck before you have time to react\n\n----------GAMEOVER----------\n')
        os.system('PAUSE')
        exit ()
    elif dark == 'Turn around':
        print('You forgot that there was a drudge behind you.\nBefore you have a change to get back to the storage room, the drudge corners and kills you mercilessly\n\n'
        '----------GAMEOVER----------\n')
        os.system('PAUSE')
        exit()

if Oil == 1:
    dark = input('Luckily you aquired an Oil Lamp, that will allow you to navigate the darkness.\n Do you wish to use one of your matches {Y/N]\n')
    if dark == 'Y':
        dark == input('You fumble around trying to light the lamp but you lost one of your matches in the process.\n'
                      'Do you want to attempt to light the lamp again? [Y/N]\n')
    while not dark == 'Y' and not dark == 'N':
        print('Try Again...')
        dark = input('Do you want to use your last match to light the lantern? [Y/N]\n')
    if dark == 'N':
        print( 'You attempt to Navigate through the darkness, you feel something grab your leg!\n When you turn around, you see a creature with glowing yellow eyes\n'
        'The monster snaps your neck before you have time to react\n\n----------GAMEOVER----------\n')
        os.system('PAUSE')
        exit()
    elif dark == 'Y':
        print('You did it, you managed to light the lamp a you can now see your way around.')

tun = input('Navigating even with the Oil Lamp proved to be difficult, but you made it.\n'
            'You have reached a forked tunnel, will you go "left" or "right"?')
while not tun == 'left' and not tun == 'right':
    print('Please Try Again...')
    tun = input ('left or right?\n')
if tun == 'left':
    print('Good Choice, you made it through the shaft safely.')
elif tun == 'right':
    print('Wrong Choice, you angered a cyclops...\n\n----------GAMEOVER----------\n')
    os.system('PAUSE')
    exit()

hole = input("As you make your way through the underground tunnels you spot a small crawlspace off to the side.\n"
             'It is big enough for you to fit into, but there are some webs in the way.\n'
             'Do you wish to explore this tunnel or ignore it and countine on?  [Ignore/Explore]\n')
while not hole == 'Explore' and not hole == 'Ignore':
    print('You are really trying my patience here, can we please get this over with?')
    hole = input("As you make your way through the underground tunnels you spot a small crawl space off to the side.\n"
             'It is big enough for you to fit into, but there are some webs in the way.\n'
             'Do you wish to explore this tunnel or ignore it and countine on?  [Ignore/Explore]\n')
if hole == 'Explore':
    print('You clear away the webs at the entrance and make your way into the confined space.\n'
          'You are then quickly devoured by a giant spider.\n\n----------GAMEOVER----------\n')
    os.system("PAUSE")
    exit()
elif hole == 'Ignore':
    print('You move onward ignoring the hole, you are pathetic and afraid of spiders\n')
time.sleep(3)

room = input('The passage opens up into a large room with dozens of pillars leading up to the ceiling. You can also just barely see a door opposite of you in the room.\n'
             'Do you head directly for the door, or wait to see what happens?  [Wait/Forward]\n')
time.sleep(2)
while not room == 'Wait' and not room == 'Forward':
    print('Shall we keep this adventure going?')
    room = input ('Do you head for the door, or wait to see what happens?  [Wait/Forward]\n')
if room == 'Wait':
    print('You wait in the entrance of the room, suddenly you are grabbed from behind by some unforeseen creature.\n\n----------GAMEOVER----------\n')
    os.system("PAUSE")
    exit()
elif room == 'Forward':
    print("You don't care if you live or die and boldy cross the room to the door.\n"
          "To your surpise nothing happens and you reach your destination.\n")
time.sleep(2)

bon = input('You go through the door. On the other side is a room filled with bones. There are no other ways out of the room besides the way you came in.\n'
            'You hear something coming down the path you just took.\n'
            'Do you try and leave the room or do you hide amongst the piles of bones?  [Hide/Escape}\n')
while not bon == 'Hide' and not 'Escape':
    print('Try again')
    bon = input('There are no other ways out of the room besides the way you came in.\n'
            'You hear something coming down the path you just took.\n'
            'Do you try and leave the room or do you hide amongst the piles of bones?  [Hide/Escape}\n')
if bon == 'Escape':
    print('Dummkopf, you rush out of the room and run straight into your purserer.\n'
           'The drudge lifts you up and smashes your frail mortal body into the stone wall. Yor lifeless body slumps to the ground.\n\n----------GAMEOVER----------\n')
    os.system("PAUSE")
    exit()
if bon == 'Hide':
    print('You dive gracefully behind a pile of bones.\n'
          'From your hiding spot you see a drudge enter the room. It does not see you hiding cleverly in the bones.\n')
time.sleep(3)

en = input('You recognize it as the same creature that was guarding your cell.\n'
            'Do you remain in hiding or do you decide you want to be brave and try to lock the drudge in this room?  [Hide/Lock]\n')
while not en == 'Hide' and not 'Lock':
    print('You end up dying of boredom.\n----------GAMEOVER----------\n\n')
    os.system("PAUSE")
    exit()
if en == 'Lock':
    print('You slip out of them room and close the door behind you and lock it.\n'
          'You smile to youself knowing you have outwitted the dumb creature. You turn to leave and you see that the vampire is right there.\n'
          'Yu are unable to do anything as the vampire happily drinks your blood.\n----------GAMEOVER----------\n\n')
    os.system("PAUSE")
    exit()
if en == 'Hide':
    print("You stay hidden amongst the bones of your fellow humans and watch as the vampire's servant moves about the room\n")
time.sleep(2)

esc = input("The creature walks over to a portion of the wall and suddenly a new tunnel appears out of nowhere.\n"
            "Now it is time for your hardest choice. Do you try and knock him out or do you wait for him to leave?  [Wait/Attack]")
while not esc =='Wait' and not esc == 'Attack':
    print("Let's read that again carefully and then choose, OK?\n")
    esc = input("The creature walks over to a portion of the wall and suddenly a new tunnel appears out of nowhere.\n"
            "Now it is time for your hardest choice. Do you try and knock him out or do you wait for him to leave?  [Wait/Attack]")
if esc == 'Wait':
    print('You decide to wait it out to see what happens. Suddenly the drudge turns around and runs towards you. It has caught your scent and there is no escaping it.\n----------GAMEOVER----------\n\n')
    os.system("PAUSE")
    exit()
elif esc == 'Attack':
    print('You creep up on the monster weilding a femur bone. Quickly you use all you might and swing at his head.\n'
          'You did it! You knocked him out!\n')
time.sleep(3)
flu = input('You can now go down the passageway. Do you take a leisurely stroll or run?  [Walk,Run]\n')
while not flu == 'Walk' and not flu == 'Run':
    print("After all this time you are still doing this? Go again.")
    flu = input('You can now go down the passageway. Do you take a leisurely stroll or run?  [Walk,Run]\n')
if flu == 'Walk':
    print('You decide that you have earned a break and decide to talk a slow walk down the hall.\n'
          'However you are still being pursued by the vampire and in this slow pace he easily catches you and dispatches you. Good job.\n----------GAMEOVER----------\n\n')
    os.system("PAUSE")
    exit()
elif flu == 'Run':
    print("You can't wait freedom awaits you rush down the corridor.\n"
          "You escaped from the vampire's liar. Good job.")

print("But this is not the end. You Now find yourself in the middle of the woods./n"
      "You see him out of the corner of your eye...It's Shia LaBeouf!!")
shia = input("He is right behind you. Do you look for your car or run?  [Look for car/Run]")
if shia == 'Look for car':
    print('You waste too much time looking for your car and Shia LaBeouf attacks you and begins to devour you.\n--------GAMEOVER--------\n\n')
    os.system("PAUSE")
    exit()
elif shia == 'Run':
    print('You take of running, But Shia LaBeouf is quick to follow.')
time.sleep(2)

lost = input("You manage to lose him, but now you are hoplessly lost yourself. You see a cabin in the distance. Do you go to investigate it?  [Y/N]")
while not lost == 'Y' and not lost == 'N':
    print('Last time I ask you Nicely')
    lost = input("You manage to lose him, but now you are hoplessly lost yourself. You see a cabin in the distance. Do you go to investigate it?  [Y/N]")
if lost == 'N':
    print('You decide to avoid it and wander around aimlessly. You get lost and eventually die in some horrible way.\n--------GAMEOVER--------\n\n')
    os.system("PAUSE")
    exit()
elif lost == 'Y':
    print("You go and investigate the cabin...")
time.sleep(2)


trap = input("AGHHHHH!! You're foot gets caught in a beartrap. Do you chew it off or leave it?  [Chew it off/Wait]")
while not trap == 'Wait' and not trap == 'Chew it off':
    print('Try again')
    trap = input("AGHHHHH!! You're foot gets caught in a beartrap. Do you chew it off or leave it?  [Chew it off/Wait]")
if trap == 'Wait':
    print('You opt to wait and you slowly bleed out and die.\n--------GAMEOVER--------\n\n')
    os.system("PAUSE")
    exit()
elif trap == 'Chew it off':
    print('You gnaw of your foot and continue twards the cabin on your stump leg.')
time.sleep(2)

cabin = input('You look inside the cabin. Shia LaBeouf is inside! Do you try to kill him or run away?  [Run/Attack]')
while not cabin == 'Run' and not cabin =='Attack':
    print('Last time for sure.')
    cabin = input('You look inside the cabin. Shia LaBeouf is inside! Do you try to kill him or run away?  [Run/Attack]')
if cabin == 'Run':
    print('You limp away from the scene as fast as you can. Unfotanaltey you catch an infection in your leg and die.\n--------GAMEOVER-------\n\n')
    os.system("PAUSE")
    exit()
elif cabin == 'Attack':
    print('You go on the offensive againt the cannibal.')
time.sleep(2)

fight = input('You enter the cabin. You find a knife on the table and sneek up behind Shia LaBeouf. Do you strangle him or stab him? [Strangle/Stab]')
while not fight == 'Stab' and not fight == 'Strangle':
    print('You take to long. He spins around and kills you.\n--------GAMEOVER--------\n\n')
    os.system("PAUSE")
    exit()
if fight == 'Strangle':
    print('You try to strangle him. But it is no use, he overpowers you and returns the favor. You soon blackout.\n-------GAMEOVER--------\n\n')
    os.system("PAUSE")
    exit()
elif fight == 'Stab':
    print('You stab him in his kiddney and he falls heavily to the ground. You did it, now it is time to get going.')
time.sleep(3)

print("But he isn't dead Shia surprise!")
time.sleep(2)

edd = input("He has a gun in his hand and death in his eyes. Do you fight him or run?  [Fight,Run.]")
while not edd == 'Fight' and not edd == 'Run':
    print('Too late, he gets you.\n--------GAMEOVER--------\n\n.')
    os.system("PAUSE")
    exit()
if edd == 'Run':
    print('You try to run, but he shots you in your back. You are dead.\n--------GAMEOVER--------\n\n')
    os.system("PAUSE")
    exit()
elif edd == 'Fight':
    print('You know ju jitsu. You disarm him and then with a nearby axe decapitate him. Congrats on the win you survived for today.\n--------VICTORY-------\n\n')
    
    
