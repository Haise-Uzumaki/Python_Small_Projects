print("Welcome To My Computer Quiz Game!")

playing = input("Do You Wish To Play? ")

if playing.lower() != "yes":
    quit()
    
    
print("Okay! Let's Play !")
score = 0

answer = input("What does CPU stand for? : ")

if answer.lower() == "central processing unit" :
    print("Correct!")
    score += 1
else:  
    print("Incorrect!")
    
answer = input("What does GPU stand for? : ")
if answer.lower() == "graphics processing unit" :
    print("Correct!")
    score += 1
else:  
    print("Incorrect!")
 
answer = input("What does RAM stand for? : ")   
if answer.lower() == "random access memory" :
    print("Correct!") 
    score += 1
else:  
    print("Incorrect!")

answer = input("What does SSD stand for? : ") 
if answer.lower() == "solid state drive" :
    print("Correct!")
    score += 1
else:  
    print("Incorrect!")

answer = input("What does HDD stand for? : ")  
if answer.lower() == "hard disk drive" :
    print("Correct!")
    score += 1
else:  
    print("Incorrect!")
    
print("You have got " + str(score) + " answers correct!!")
print("Quiz Game Ends.Feel Free To Play Again")