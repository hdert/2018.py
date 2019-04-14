'''
Author: Justin
Date Started: 26/07/2018
Date Now: 26/07/2018
'''

# -- Librarys --

import random as rand
from tkinter import *

# -- Setup --

root = Tk()
root.title("Questions")
root.geometry("700x700+10+10")
root.configure(bg = "lightgrey")

# -- Constant Lists --

answers = ['deepweb', 'darkweb', 'darknet', 'the onion router',
           'the amnesic incognito live system', 'yes', 'yes', 'yes']

questions = ['What\'s the name of the part of the internet that\'s\n hundreds of times bigger than the internet you can see?',
             'What\'s the name of the part of the internet\n you can access with Tor?',
             'What\'s the name of the framework that the darkweb runs on?',
             'What does Tor stand for?',
             'What does Tails stand for?',
             'Are flags the name for experimental features in Google Chrome?',
             'Is Chromium an open source project?',
             'Is there a Chromium OS?']

# -- Variables --

rand_ = 0
answer = answers[0]
guess = ""
guesses = 0
points = 0
font = ("ariel", 14)
colour = "lightgrey"
setup = False
name = ""
finished = False
length = len(questions)

# -- Functions --

def start(event = None):
    global setup
    global rand_
    global answer
    global guess
    global points
    global guesses
    global length
    
    if setup == False:
        global name
        name = en.get()
        en.delete(0, END)
        rand_ = rand.randint(0, len(answers)-1)
        answer = answers[rand_]
        text.configure(text = questions[rand_])
        msgBox.configure(text = "Please Answer The Above Question")
        setup = True
    else:
        
        guess = en.get()

        if answer == guess:
            msgBox.configure(text = '\nCorrect\n')
            points += 1
            answers.remove(answer)
            questions.remove(questions[rand_])
        else:
            msgBox.configure(text = '\nIncorrect\n')
            answers.remove(answer)
            questions.remove(questions[rand_])
        guesses += 1

        if guesses == length:
            
            if points >= length:
                msgBox.configure(
                    text = 'You did really well, you got {} points'.format(
                        point()))
                end()
            elif (points >= int(length/2)):
                msgBox.configure(text = 'You did okay, you got {} points'.format(
                    point()))
                end()
            else:
                msgBox.configure(
                    text = 'You did not pass, you got {} points'.format(
                        point()))
                end()
                
        if finished == False:
            rand_ = rand.randint(0, len(answers)-1)
            answer = answers[rand_]
            text.configure(text = questions[rand_])
                                     
    try:
        en.delete(0, END)
    except:
        pass

def end():
    global name
    global finished
    text.configure(text = 'Thanks for playing {}'.format(name))
    root.configure(bg = 'green')
    text.configure(bg = 'green')
    en.destroy()
    btn.destroy()
    finished = True

def point():
    global points
    global length
    return (str(int(points)*10) + '/' + str(int(length)*10))
    
# -- Widgets --

text = Label(root, text = "Welcome To My Quiz",
             font = font, bg = colour)

en = Entry(root, bg = colour)

btn = Button(root, text = "Enter", command = start)

msgBox = Label(root,
               text = "Please Enter Your Name In The Entry Box\nAnd Press Enter",
               font = ("ariel", 10), bg = "grey")

# -- Code --

text.pack()

en.pack()
en.focus()
en.bind("<Return>", start)

btn.pack()

msgBox.pack()

root.mainloop()
