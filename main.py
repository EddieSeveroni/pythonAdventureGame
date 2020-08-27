print('Welcome to Jumanji: Adventure Game')
name = input('What is your name? ')
age = int(input('What is your age? '))

health = 10

if age >= 18:
    print('You are old enough to play!')

    wants_to_play = input('Do you want to play? ')
    if wants_to_play == 'yes' or 'Yes':
        print('You are starting with', health, 'health.')
        print("Let's play!")

        left_or_right = input('First choice... Left or Right (left/right)? ')
        if left_or_right == 'left':
            ans = input('Nice, you followed the path and reached a lake... Do you swim across or go around (across/around)? ')

            if ans == 'around':
                print('You went around and reached the other side of the lake.')

            elif ans == 'across':
                print('You managed to get across but you were bit by a piranha and lost 6 health.')
                health -= 5
            
            ans = input('You notice a house and a river. Which do you go to (river/house)? ')
            if ans == 'house':
                print('You go to the house and are greeted by the owner... He does not like you and you lose 6 health.')
                health -= 6
                
                if health <= 0:
                    print('You now have 0 health and you lose the game...')
                elif health >= 0:
                    print('You now have 4 health remaining. You win!')
                '''else:
                    print('You have survived... You win!')'''
            else:
                print('You fell in the river and lost...')

        else:
            print('You fell down and lost...')

    else:
        print('See ya!')

else:
    print('You are not old enough to play...')