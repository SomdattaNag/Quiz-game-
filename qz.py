score=0
qno=0
name=input("What is your name?")
print('hi',name,'lets start the quiz')
qno+=1
q1= input(" Who is known as the father of Computer?")
ans1='Charles Babbage'
if (q1==ans1):
    print("Correct!")
    score+=1
else:
    print("oops correct answer is", ans1)

qno+=1
q2=input("Who is the author of 'Pride and Prejudice'?")
ans2= 'Jane Austen'
if(q2==ans2):
    print("Correct!")
    score+=1
else:
    print("oops correct answer is", ans2)

qno+=1
q3=input("What character have both Robert Downey Jr. and Benedict Cumberbatch played?")
ans3= 'Sherlock Holmes'
if(q3==ans3):
    print("Correct!")
    score+=1
else:
    print("oops correct answer is", ans3)

qno+=1
q4=input("Which planet in the Milky Way is the hottest?")
ans4= 'Venus'
if(q4==ans4):
    print("Correct!")
    score+=1
else:
    print("oops correct answer is", ans4)

qno+=1
q5=input("What city is known as The Eternal City?")
ans5= 'Rome'
if(q5==ans5):
    print("Correct!")
    score+=1
else:
    print("oops correct answer is", ans5)

qno+=1
q6=input("Who discovered that the earth revolves around the sun?")
ans6= 'Nicolaus Copernicus'
if(q6==ans6):
    print("Correct!")
    score+=1
else:
    print("oops correct answer is", ans6)
qno+=1
q7=input("Which planet has the most moons?")
ans7= 'Saturn'
if(q7==ans7):
    print("Correct!")
    score+=1
else:
    print("oops correct answer is", ans7)

qno+=1
q8=input("How many bones do we have in an ear? ")
ans8= '3'
if(q8==ans8):
    print("Correct!")
    score+=1
else:
    print("oops correct answer is", ans8)

qno+=1
q9=input("What sports car company manufactures the 911?")
ans9= 'Porsche'
if(q9==ans9):
    print("Correct!")
    score+=1
else:
    print("oops correct answer is", ans9)

qno+=1
q10=input("What software company is headquartered in Redmond, Washington?")
ans10= 'Microsoft'
if(q10==ans10):
    print("Correct!")
    score+=1
else:
    print("oops correct answer is", ans10)
print(f'your score is {score}/{qno}')
try:
    percentage = (score *100)/qno
except ZeroDivisionError:
    print('0% questions are correct')
if(percentage>=50):
    print(f'{percentage}% questions are correct.\n Congrats you did better than average')
else:
    print(f'{percentage}% questions are correct.\n Better luck next time')