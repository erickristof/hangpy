#!/usr/bin/env python3

import random

def wincheck(guesses, a, b):
    if guesses == 10:
        print ('you lose')
        return False
    elif a == b:
        print('you win')
        return False
    else:
        return True

progress = (['','\n\n\n\n\n   ===','\n    |\n    |\n    |\n    |\n   ===',' ____\n    |\n    |\n    |\n    |\n   ===',
         ' ____\n |  |\n    |\n    |\n    |\n   ===',' ____\n |  |\n O  |\n    |\n    |\n   ===',
         ' ____\n |  |\n O  |\n |  |\n    |\n   ===',' ____\n |  |\n O  |\n |  |\n/   |\n   ===',
         ' ____\n |  |\n O  |\n |  |\n/ \ |\n   ===',' ____\n |  |\n O  |\n/|  |\n/ \ |\n   ===',
         ' ____\n |  |\n O  |\n/|\ |\n/ \ |\n   ==='])

with open('sowpods.txt', 'r') as f:
    lines = f.readlines()

while True:
    correct = []
    used = []
    guesses = 0
    
    choice = str(input("Would you like to play easy(e), medium(m), or hard(h)? (q to quit) "))
    if choice == 'q':
        break
    elif choice == 'e':
        the_word = random.choice([i for i in lines if len(i) <= 5]).strip()
    elif choice == 'm':
        the_word = random.choice([i for i in lines if len(i) > 5 and len(i) <= 10]).strip()
    elif choice == 'h':
        the_word = random.choice([i for i in lines if len(i) > 10 and len(i) <= 16]).strip()
    else:
        print ("Please choose 'e' for Easy, 'm' for Medium, 'h' for Hard, or 'q' if you'd like to quit")
        continue
    
    blanks = ['_' for i in the_word]
    print (''.join(blanks))
    
    while wincheck(guesses, blanks, [str(i) for i in the_word]):
        a = str(input("guess:"))
        if len(a) != 1:
            print (''.join(blanks),"(%s)\n%s" % (','.join(used), progress[guesses]))
            continue
        if a in the_word or a in the_word.lower():
            blanks = ['_' if i != a and i.lower() != a and i not in correct else i for i in the_word]
            correct.append(a.upper())
            correct.append(a.lower())
        elif a not in used:
            used.append(a)
            guesses += 1
        print (''.join(blanks),"(%s)\n%s" % (','.join(used), progress[guesses]))
    
    print ("The word was %s!" % the_word)
    continue
