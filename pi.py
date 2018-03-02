pwds = []
for num in range(1000000):
    pwds.append("0" * (6 - len(str(num))) + str(num))

with open("Pi-1000000000.txt","r")as f:
    pai=f.read()

#输出字符串的长度和π的前109位
print(len(pai),pai[0:110])
stat = []

for pwd in pwds:
    stat.append([pwd,pai.index(pwd)-1])
    if len(stat) % 1000 == 1:
        print(stat[-1])

with open("Pi-stat.txt","w")as f:
    for data in stat:
        f.write(data[0]+':'+str(data[1])+'\n')
