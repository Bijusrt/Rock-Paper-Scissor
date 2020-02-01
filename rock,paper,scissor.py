print 'Welcome to the Game'
a=raw_input('Enter your name')
b=0
c=0
from random import randint
for i in range(1,6):
    player_choice = raw_input('What do you pick? (rock, paper, scissors) : ')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]
    if player_choice == 'rock' and computer_choice == 'scissors':
        b+=1
    elif player_choice  == 'paper' and computer_choice== 'scissors':
        c+=1
    elif player_choice == 'scissors' and computer_choice == 'paper':
        b+=1
    elif player_choice  == 'scissors' and computer_choice== 'rock':
        c+=1
    elif player_choice  == 'paper' and computer_choice == 'rock':
        b+=1
    elif player_choice  =='rock'  and computer_choice =='paper' :
        c+=1
    elif player_choice!='paper' and player_choice!='scissors' and player_choice!='rock':
    	print 'enter properly'
print 'your score is : ',b
print 'computer score is : ',c
if b>c:
	print 'You win!'
elif b==c:
	print 'Draw!'
else:
	print 'You lose!'