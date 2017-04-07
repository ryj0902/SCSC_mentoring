#-*- coding: utf-8 -*-
import random as r

def getRandomNum(cipher):
    result = ""
    while(len(result) != cipher):
        digit = str(r.randint(0, 9))
        if not digit in result:
            result += digit

    print result # debug
    return result

def getGuess(guessed, num, cipher):
    if not num.isdigit():
        print "Input value not consist of digit number"
        return False
    if len(num) != cipher:
        print "Please enter %d-digit number." % cipher
        return False
    for i in range(len(num)):
        if num[i] in num[:i] + num[i+1:]:
            print "There are repeated number. Choose another number."
            return False
    if num in guessed:
        print "You have already guessed that number. Choose another number."
        return False


    return True

def playAgain():
    replay = raw_input("Do you want to play again? (yes or no) ")
    return replay.lower().startswith('y')

def getCipher() :
    while True :
        print "Input the number of cipher. (1 ~ 9)"
        cipher = raw_input()
        if not cipher.isdigit():
            print "Input must be digit number"
            continue
        cipher = int(cipher)
        if cipher < 1 or cipher > 9:
            print "Cipher must be between 1 and 9"
            continue

        break

    return cipher

print "S T A R T"
print "=========================\n"

cipher = getCipher()
secret = getRandomNum(cipher)
guessed = []
while(True):
    print "Guess numbers ({0} ~ {1}):".format("0"*int(cipher), "9"*int(cipher))
    guess = raw_input()
    if not getGuess(guessed, guess, cipher):
        continue
    guessed.append(guess)

    strike = 0
    ball = 0
    for i in range(cipher):
        if guess[i] in secret:
            if guess[i] == secret[i]:
                strike += 1
            else:
                ball += 1

    if strike < cipher:
        #print "{0} strike, {1} ball.".format(strike, ball)
        #print "%d strike, %d ball." % (strike, ball)
        print str(strike) + " strike, " + str(ball) + " ball."
        print "\n=========================\n"
    else:
        print 'Yes! The secret number is "' + str(secret) + '"! You have won!\n'

        if not playAgain():
             break
        else:
            guessed = []
            cipher = getCipher()
            secret = getRandomNum(cipher)
