import random
total_score = 0

while True:
    random_num = random.randint(1,6)
    user_in=int(input('enter the num : '))
    if (user_in != random_num):
        total_score=total_score+user_in
        print(f"bot_num: {random_num}")
        print(f"User scoure: {total_score}")
        
    
    else:
        print(f"bot_num: {random_num}")
        print(f"User out and total score: {total_score}")
        break;