n = int(input())
w = list(input().split())
check_list = ['and', 'not', 'that', 'the', 'you']
for c in check_list:
    if c in w:
        print('Yes')
        exit()
print('No')