import time
ques = ('what is 1+1', 'what is 2+2', 'what is 3+3','what is 4+4','what is 5+5')
ans = (2,4,6,8,10)

a = int(input('Do you want to play a game: '))

def first():
    print('Hello welcome to My KBC. We here will display you 5 questions at max. '\
    'Each question carries 10k. If you win you will get on to next question or if the answer is wrong will takehome last won price.\n'\
        'The rules are simple. Each question has 4 opotions one is correct you have to input the correct option.'\
            'Lets directly got to questions now without any timepass')
    print('---------------------------------------------------------')
    print('lets start with first question now.','\n','\t',ques[0],'\n','Youre options are --> 1,2,3,4')
    ans = int(input('Enter your ans here: '))
    if(ans == 2):
        print('Congratulations!!! Your ans is correct\n Hold it tight. Your next question will display in just 10 secs')
        time.sleep(10)
        result = second()
        print(result)
    else:
        print('You are wrong. The game is closed\n Unfortunately you were not able to cross even first question and thus you didnt won any price home.\n Happy life ahead and best of luck for next time')
        restart()

def second():
    print('Your second questions is','\n','\t',ques[1],'\n','Youre options are --> 1,10,6,4')
    ans = int(input('Enter your ans here: '))
    if(ans == 4):
        print('Congratulations!!! Your ans is correct\n Hold it tight. Your next question will display in just 10 secs')
        time.sleep(10)
        result = third()
        print(result)
    else:
        print('You are wrong. The game is closed\n But still congratulations you have won 10 thousand rupees')
        restart()

def third():
    print('Your third questions is','\n','\t',ques[2],'\n','Youre options are --> 6,0,9,2')
    ans = int(input('Enter your ans here: '))
    if(ans == 6):
        print('Congratulations!!! Your ans is correct\n Hold it tight. Your next question will display in just 10 secs')
        time.sleep(10)
        result = fourth()
        print(result)
    else:
        print('You are wrong. The game is closed\n But still congratulations you have won 20 thousand rupees')
        restart()   

def fourth():
    print('Your third questions is','\n','\t',ques[3],'\n','Youre options are --> 11,1,7,8')
    ans = int(input('Enter your ans here: '))
    if(ans == 8):
        print('Congratulations!!! Your ans is correct\n Hold it tight. Your next question will display in just 10 secs')
        time.sleep(10)
        result = fifth()
        print(result)
    else:
        print('You are wrong. The game is closed\n But still congratulations you have won 30 thousand rupees')
        restart() 



def fifth():
    print('Your third questions is','\n','\t',ques[4],'\n','Youre options are --> 5,10,3,0')
    ans = int(input('Enter your ans here: '))
    if(ans == 10):
        print('Congratulations!!! Your ans is correct\n')
        time.sleep(5)
        print('Many Many Congratulations. You have completed this game and you have won 50 thousand rupees. \nAgain congratulations and happe life ahead')
        exit
    else:
        print('You are wrong. The game is closed\n But still congratulations you have won 40 thousand rupees')
        restart() 





def restart():
    print('You have an option to restart the game.\nDo you want to replay the game.\n')
    restart = int(input('To restart enter 1 now: '))
    if(restart == 1):
        to_game = first()
        print(to_game)
    else:
        print('You are out of game now you can close the window. Thank You for you time.')










# calling function
if(a==1):
    result = first()
    print(result)
else:
    print('Sorry to see you go without playing.')