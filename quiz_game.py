print("Welcome to Simple Basic Computer Quiz")

playing = input('DO you want to play ?yes|no :')

if playing.lower() != 'yes':
    quit()
print('Okay! Let\'s play') 
score = 0

answer = input("who is father of Python is  ?").lower() 
if answer =='gudio van rossum':
    print('Correct!')
    score += 1
else:
    print('Incorrect !')
answer = input("what does RAM stands for ?").lower() 
if answer =='random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect !')
answer = input("what does PSU stands for ?").lower() 
if answer =='power supply':
    print('Correct!')
    score += 1
else:
    print('Incorrect !')
answer = input("what does CPU stands for ?").lower() 
if answer =='central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect !')
    
print("You Got",str(score),"Questions Correct")
print("You Got",str(score/4 *100),"%.")
