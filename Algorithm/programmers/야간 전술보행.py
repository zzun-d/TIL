distance = 12
scope = [[7, 8], [4, 6], [11, 10]]
times = [[2, 2], [2, 4], [3, 3]]

#############################################

for i in range(len(scope)):
    scope[i].sort()
    scope[i].append(times[i])
scope.sort()
answer = distance
for s, e, (w, r) in scope:
    if s % (w + r) <= w:
        answer = s
        break
    elif e - s - 1 > r - (s % (w + r) - w):
        answer = s + r - (s % (w + r) - w) 
        break
    else:
        continue
print(answer)
        
