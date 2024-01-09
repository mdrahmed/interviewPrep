'''
2000-2060, 2010-2070, 1900-2000
1900, 2000, 2010
2060, 2000, 2070
'''

people = [[2000,2060], [2005,2009], [2006,2008], [2010,2070], [1900,2000], [1800,1850]]
# Brute force - check each year
minn = people[0][0]
for b,d in people:
    if minn > b:
        minn = b
maxx = people[0][1]
for b,d in people:
    if maxx < d:
        maxx = d
max_people = 0
print(minn, maxx)
for i in range(minn,maxx):
    total_alive = 0
    for b,d in people:
        if b <= i and i <= d:
            total_alive += 1
            if i == 2006:
                print(b,d)
    max_people = max(total_alive, max_people)
print(max_people)

## 
max_people = 0

print(max_people)



