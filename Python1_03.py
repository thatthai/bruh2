import statistics

print("*** Election ***")
n = int(input("Enter a number of voter(s) : "))
l = []
x = input()
l = x.split(" ")
for i in range(0, len(l)):
    l[i] = int(l[i])
    if l[i] > n :
        l[i] = "x"

while 'x' in l :
    l.remove('x')

try:
    print(statistics.mode(l))
except :
    print("*** No Candidate Wins ***")


