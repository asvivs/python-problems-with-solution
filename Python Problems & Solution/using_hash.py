# For an integer n, input n space-separated integers to form a tuple, then calculate and display the result of hash(t)

n = int(input())
integer_tuple = tuple(map(int, input().split()))
print(hash(integer_tuple))
