score1 = int(input('Enter score1: '))
score2 = int(input('Enter score2: '))
score3 = int(input('Enter score3: '))
average = (score1 + score2 + score3)/3
print('Average score is: ', average)
if average > 95:
    print('Congratulations')
if average < 50:
    print('Keep trying')