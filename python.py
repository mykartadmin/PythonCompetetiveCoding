# Enter your code here. Read input from STDIN. Print output to STDOUT
nroll = set(map(int,input().split()))
t = int(input())
x = True
for i in range(t):
    broll = set(map(int,input().split()))
    if not (nroll.issuperset(broll) and len(nroll)>len(broll)):
        x = False
        break
print(x)
