from turtle import *

def startup():
    win=Screen()
    setup(width=.9, height=0.9, startx=None, starty=None)
    win.title("Hangman")
    win.clear()
    hideturtle()
    speed(10)
    pencolor("black")
    penup()
    origin=drawGallows()
    clearStk(incorrect)
    return (win,origin)

def moveTurtle(face,units):
    pendown()
    setheading(face)
    forward(units)
    penup()
    return

def drawGallows():
    moveTurtle(right,2*unit)
    goto(pos()[0]//2,pos()[1])
    moveTurtle(up,4*unit)
    moveTurtle(right,2*unit)
    moveTurtle(down,0.4*unit)
    return pos()

def drwHead(origin):
    goto(origin[0]-0.2*unit,origin[1]-0.2*unit)
    pendown()
    circle(0.2*unit)
    penup()
    return pos()

def drwTorso(origin):
    goto(origin[0]+0.2*unit,origin[1]-0.2*unit)
    moveTurtle(down,unit)
    return pos()

def drwLArm(origin):
    goto(origin[0],origin[1]+0.6*unit)
    moveTurtle(left,0.4*unit)
    goto(origin)
    return origin

def drwRArm(origin):
    goto(origin[0],origin[1]+0.6*unit)
    moveTurtle(right,0.4*unit)
    goto(origin)
    return origin

def drwLLeg(origin):
    goto(origin[0],origin[1]+0.1*unit)
    moveTurtle(leftTilt,0.6*unit)
    goto(origin)
    return origin

def drwRLeg(origin):
    goto(origin[0],origin[1]+0.1*unit)
    moveTurtle(rightTilt,0.6*unit)
    goto(origin)
    return origin

def makeStk():
    return 'stk',[]

def elements(s):
    return s[1]

def push(s,el):
    elements(s).insert(0,el)

def fullStk(s):
    if len(elements(s)) == 0:
        return True
    return False

def clearStk(s):
    del elements(s)[:]

def getWords():
    print ("Judge, please enter 3 words, one at a time")
    
    a = input("Enter a word...")
    b = input("Enter a word...")
    c = input("Enter a word...")
    print("Accused, guess the words and avoid being hanged!")
    
    return [a,b,c]

def maskLetters(mask,string):
    a = len(string)
    b= list(mask * a)
    c = " ".join(b)
    return " "+c

def showCorrect(let,word):
    a =""

    for i in word:
        if i  == let:
            a+= i 
        else :
            a+= " "
    a = list(a)
    a = " ".join(a)
    return "  "+a

def getGuess(window):
    w = window
    a = textinput("Enter a single letter as a guess","")
    if len(a) != 1:
        while(True):
            a = textinput("Enter a single letter as a guess","")
            if len(a) == 1:
                break
    return a        
    

def goodGuess(let,word):
    if word == "":
        return 0
    elif word[0] == let:
       return  1 + goodGuess(let,word[1:])
    else:
       return goodGuess(let,word[1:])

def displayWord(c,word,funct):
    a=funct(c,word)
    hideturtle()
    goto(-300,-120)
    if c == "_":
        write(str(a), font=("Arial", 40, "normal"))
    else:
       write(str(a), font=("Arial", 38, "normal")) 

# a function to test the previous function
def test():
	startup()
	displayWord('_','hangman',maskLetters)
	displayWord('a','hangman',showCorrect)


def wordCount(word):
    a = list(word)
    a = list(set(a))
    a = len(a)
    return a

def reverse(lst):
	if lst == []:
		return []
	else:
		return  reverse(lst[1:]) + [lst[0]]

def combine():
    return ",".join(reverse(elements(incorrect)))

def showIncorrect():
    goto(-300,-180)
    write(combine(), font=("Arial", 30, "normal"))

def play(lst):
    #lst = getWords()
    s=startup()
    count = 0
    displayWord('_',lst[0],maskLetters)
    default = True
    pos = s[1]
    correct = 0
    def helper(lst,count,default,correct):
        if lst == [] or count > 6:
            goto(-300,-260)
            write("Ouch!", font=("Arial", 30, "normal"))
            return "game is over"

        elif wordCount(lst[0]) == correct:
            goto(-300,-260)
            write("You Guessed it!", font=("Arial", 30, "normal"))
            return "you won"
        
        elif count ==1 and default == False:
            word = lst[0]
            drwBody[1](pos)
            
            let = getGuess(s)
            

            if goodGuess(let,word) > 0:
               displayWord(let,word,showCorrect)
            else:
                push(incorrect,let)
                showIncorrect()
                return helper(lst,count +1,False,correct)   
           

            return helper(lst,count,True,correct+1)

        elif count ==2 and default == False:
            word = lst[0]
            
            drwBody[2]((140.00,170.00))
            let = getGuess(s)

            if goodGuess(let,word) > 0:
               displayWord(let,word,showCorrect)
            else:
                push(incorrect,let)
                showIncorrect()
                return helper(lst,count +1,False,correct)   

            return helper(lst,count,True,correct+1)

        elif count ==3 and default == False:
            word = lst[0]

            drwBody[3]((150.00,110.00))
            let = getGuess(s)

            if goodGuess(let,word) > 0:
               displayWord(let,word,showCorrect)
            else:
                push(incorrect,let)
                showIncorrect()
                return helper(lst,count +1,False,correct)   

            return helper(lst,count,True,correct+1)
        
        elif count ==4 and default == False:
            word = lst[0]

            drwBody[4]((150.0, 110.0))
            let = getGuess(s)

            if goodGuess(let,word) > 0:
               displayWord(let,word,showCorrect)
            else:
                push(incorrect,let)
                showIncorrect()
                return helper(lst,count +1,False,correct)   

            return helper(lst,count,True,correct+1)

        elif count ==5 and default == False:
            word = lst[0]

            drwBody[5]((150.0, 110.0))
            let = getGuess(s)

            if goodGuess(let,word) > 0:
               displayWord(let,word,showCorrect)
            else:
                push(incorrect,let)
                showIncorrect()
                return helper(lst,count +1,False,correct)   

            return helper(lst,count,True,correct+1)

        elif count ==6 and default == False:
            word = lst[0]

            drwBody[6]((150.0, 110.0))
            return helper(lst,count + 1,False,correct) 
            let = getGuess(s)

            if goodGuess(let,word) > 0:
               displayWord(let,word,showCorrect)
            else:
                push(incorrect,let)
                showIncorrect()
                return helper(lst,count + 1,False,correct)   

            return helper(lst,count,True,correct+1)

        elif default == True:
            word = lst[0] 
            
            let = getGuess(s)
            
            
            if goodGuess(let,word) > 0:
               displayWord(let,word,showCorrect)
               
            else:
                push(incorrect,let)
                showIncorrect()
                return helper(lst,count +1,False,correct)
                

            
            return helper(lst,count,True,correct+1)


    helper(lst,count,default,correct)
        

def hangman():
    lst = getWords()
    play([lst[0]])
    play([lst[1]])
    play([lst[2]])


	

	
    


#Global data
up=90
down=270
leftTilt=225
left=180
rightTilt=315
right=0
unit=50
incorrect = makeStk()
drwBody = {1:drwHead,2:drwTorso,3:drwLArm,4:drwRArm,5:drwLLeg,6:drwRLeg}



    

    
