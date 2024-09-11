print("Welcome to my computer quiz! ")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play")
score = 0

answer = input("CPU stands for ? ")
if answer.lower() == "central processing unit":
    print("correct")
    score = score+1

else:
    print("incorrect")

answer = input("what is ram?")
if answer.lower() == "random access memory":
    print("correct")
    score = score+1

else:
    print('incorrect')
print(score)