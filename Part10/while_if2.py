# while
# import random, time
# learning_score = random.randint(1,100)
# # print(learning_score)

# while learning_score < 90:
#     print(f'학습 스코어 미달 : {learning_score}')
#     learning_score = random.randint(1,100)
#     time.sleep(1)
# print(f'최종 학습 스코어 : {learning_score}')

# while true
import random, time
learning_score = None

while True:
    learning_score = random.randint(1,100)
    time.sleep(1) 
    if learning_score >= 90:
        break
    print(f'학습 스코어 미달 : {learning_score}')
print(f'최종 학습 스코어 : {learning_score}') 