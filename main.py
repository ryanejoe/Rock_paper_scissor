
import random
choices = ['paper','rock','scissor','rock']
print('how many rounds would you like?')
total_Bot_points = 0
total_User_points = 0
rounds = int(input(''))
for i in range(rounds):
    print('YOUR CHOICES ARE: rock, paper and Scissor')
    user = input("what do you pick:")
    bot = random.choice(choices)
    print('YOU PICKED  ', user)
    print('THE COMPUTER PICKED: ',bot)
    if bot == user:
        print('DRAW')
    elif bot == 'rock' and user == 'paper':
        print('user WINS')
        total_User_points += 1
    elif bot == 'paper' and user == 'rock':
        print('bot WINS')
        total_Bot_points += 1
    elif bot == 'paper' and user == 'scissor':
        print('User wins')
        total_User_points += 1
    elif bot == 'scissor' and user == 'paper':
        print('Bot wins')
        total_Bot_points += 1
    elif bot == 'rock' and user == 'scissor':
        print('Bot  wins')
        total_Bot_points += 1
    elif bot == 'scissor' and user == ' rock':
        print('User wins')
        total_User_points += 1
    else:
        print('err')
if total_User_points == total_Bot_points:
    print('FINAL: DRAW')
elif total_Bot_points > total_User_points:
    print('FINAL: BOT WINS')
elif total_Bot_points < total_User_points:
    print('FINAL: USER WINS')
else:
    print('err')

