"""Get name and marks of the students from the user and store it in a list.
Determine and display the average mark for a specific student's name. 
Show the result rounded to two decimal places. """

n = int(input())
student_marks = {}
for _ in range(n):
    name, *marks = input().split()
    s_marks = list(map(float, marks))
    student_marks[name] = s_marks
query_name = input()
list_of_marks = student_marks.get(query_name)
avg_mark = sum(list_of_marks) / len(list_of_marks)
print("%.2f" % avg_mark)
