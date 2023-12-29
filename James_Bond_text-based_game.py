print('''
       ________   ________    _________  ____________;_
      - ______ \ - ______ \ / _____   //.  .  ._______/
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/
''')

print("Hey James, we were waiting for you for quite a while. We've got to save the world. Again. The detonator is in this house, go and defuse it. Make every decision wisely, there is a bunch of bad guys. In the meantime, I will test drive your new Aston Martin. Good luck!" )
dec_1 = input('To use the main entrance or to climb the fire ladder to the top? Type \'m\' for main entrance or \'l\' for the ladder\n ').lower()
if dec_1 == 'l':
    dec_2 = input("As you climbed to the roof you see a bomb in front of you and 5 guys that surround some victim. What will you do? Try to defuse the bomb that is at arm's distance or try to rescue someone? Type \'d\' for defuse, \'r\' for helping\n ").lower()
    if dec_2 == 'r':
        print('You have beaten the guys and rescued a beauty. She tells you to cut the blue wire.')
        dec_3 = input('As you look closer to the bomb you see there are 6 wires of different colours: midnight_blue, magenta, green, purple, white, crimson-red. Which one will you cut? Type the colour fully\n').lower()
        if dec_3 == 'midnight_blue':
            print('The bomb has been deactivated. You take the beauty to the cafe. You have won!')
        elif dec_3 in ['magenta', 'green', 'purple', 'white', 'crimson-red']:
            print('Wrong wire. Game over')
        else:
            print('Sorry, didn\'t catch what you mean by that.')


    elif dec_2 == 'd':
            dec_3 = input("As you look closer to the bomb you see there are 6 wires of different colours: midnight_blue, magenta, green, purple, white, crimson-red. Which one to cut? Type the colour fully\n ").lower()
            if dec_3 == 'midnight_blue':
                 print('Nice guess! You won!')
            elif dec_3 in ['magenta', 'green', 'purple', 'white', 'crimson-red']:
                 print('Wrong wire. Game over')
            else:
                print('Sorry, didn\'t catch what you mean by that.')

elif dec_1 == 'm':
    print('You were shot from behind. The guy was hiding behind the curtain.')
else:
            print('Sorry, didn\'t catch what you mean by that.')



