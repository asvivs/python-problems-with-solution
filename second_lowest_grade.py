"""Create a nested list with student names and grades. 
Find and display the name(s) of student(s) with the second lowest grade. 
If there are multiple students with this grade, list their names alphabetically, each on a new line """

records = []
list_of_scores = []
for _ in range(int(input())):
    name = input()
    score = int(input())
    l1 = [name, score]
    list_of_scores.append(score)
    records.append(l1)
sec_score = sorted(list(set(list_of_scores)))[1]
for name, score in sorted(records):
    if score == sec_score:
        print(name)
