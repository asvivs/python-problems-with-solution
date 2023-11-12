"""Perform various operations on a list: insert, delete, append, sort, pop, and reverse.
Read a value and execute commands to manipulate the list accordingly."""

list1 = []
n = int(input())
for _ in range(n):
    user_request = input().split()
     if user_request[0] == "insert":
          list1.insert(int(user_request[1]), int(user_request[2]))
      elif user_request[0] == "remove":
          list1.remove(int(user_request[1]))
      elif user_request[0] == "append":
          list1.append(int(user_request[1]))
      elif user_request[0] == "pop":
          list1.pop()
      elif user_request[0] == "sort":
          list1.sort()
      elif user_request[0] == "reverse":
          list1.reverse()
      else:
          print(list1)
        
