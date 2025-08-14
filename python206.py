#1.no words and letters without inbuilt function
# n=input()
# c=0
# co=0
# for i in n:
#     if i==" ":
#         co+=1
#     c+=1
# print(c-1)
# print(co+1)

#2 counting numbers and alphabets 
# n=input()
# no=0
# al=0
# l=["0","1","2","3","4","5","6","7","8","9"]
# for i in n:
#     if i in l:
#         no+=1
#     elif i==" ":
#         continue
#     else:
#         al+=1
# print(f"NUMBERS={no} AND ALPHABETS={al}")

#3
#adding first two last two
# n = input()
# s = ""
# for c in n:
#     if c != ' ':
#         s += c
# print(s[0] + s[1] + s[-2] + s[-1])
# print(s[3:-2])

#4
# removing first2 and last2
# n=input()
# print(n[2:-2])


#5 remove index no
# s,n = (input().split())
# count = 0
# for i in s:
#     if count==int(n):
#         count+=1
#         continue
#     else:
#         print(i,end="")
#     count+=1


#6swap 
# n = input()
# x = input()
# y = input()
# l = []

# for c in n:
#     l.append(c)

# for i in range(len(l)):
#     if l[i] == x:
#         l[i] = y
#     elif l[i] == y:
#         l[i] = x
# print("".join(l))
