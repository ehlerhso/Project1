num_students = int(input("Enter number of students: "))
scores = input(f'Enter {num_students} score(s): ').split()
if len(scores) == 1:
    scores = [int(scores[0])]
else:
    scores = [int(scores[i]) for i in range(num_students)]
top = max(scores)
low = min(scores)
while len(scores) < num_students or top > 100 or low < 0:
    scores = input(f'Enter {num_students} score(s): ').split()
    if len(scores) == 1:
        scores = [int(scores[0])]
    else:
        scores = [int(scores[i]) for i in range(num_students)]
    top = max(scores)
    low = min(scores)
for i in range(num_students):
    if scores[i] >= top - 10:
        print(f'Student {i+1} score is {scores[i]} and grade is A')
    elif scores[i] >= top - 20:
        print(f'Student {i+1} score is {scores[i]} and grade is B')
    elif scores[i] >= top - 30:
        print(f'Student {i+1} score is {scores[i]} and grade is C')
    elif scores[i] >= top - 40:
        print(f'Student {i+1} score is {scores[i]} and grade is D')
    else:
        print(f'Student {i+1} score is {scores[i]} and grade is F')




