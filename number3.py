Initial_list=[]
Secondary_list=[]
n=int(input("How many numbers do you want ? "))
for i in range(n):
    k=int(input("Please enter the number : "))
    Initial_list.append(k)
    Secondary_list.append(k)
Secondary_list.sort()
if Initial_list==Secondary_list:
    print('Your list has been sorted')
    print(Secondary_list)
else :
    print('Your list is not sorted')
    print('Do you want your list to be sorted ?')
    print('YES or NO ? ')
    yes_no=input()
    if yes_no=='YES' or  yes_no=='yes' or yes_no=='Y' or yes_no=='y':
        Initial_list.sort()
        print(Initial_list)
    else:
        print('We look forward to seeing you again :( ')