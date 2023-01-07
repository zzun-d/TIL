N = int(input())
load = list(map(int, input().split()))
gas = list(map(int, input().split()))
cost = 0
now_gas = gas[0]
distance = 0
for i in range(N-1):
    distance += load[i]
    if gas[i+1] < now_gas:
        cost += distance * now_gas
        now_gas = gas[i+1]
        distance = 0
if distance:
    cost += distance*now_gas
print(cost)
