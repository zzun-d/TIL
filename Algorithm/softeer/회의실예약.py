n, m = map(int, input().split())
boot_info = {}
for _ in range(n):
    room_name = input()
    boot_info[room_name] = list(range(9, 18))

for _ in range(m):
    room_name, start_time, end_time = input().split()
    start_time = int(start_time)
    end_time = int(end_time)

    for i in range(start_time, end_time):
        boot_info[room_name].remove(i)

room_list = sorted(list(boot_info.keys()))
for room in room_list:
    if boot_info[room]:
        available = []
        time_stack = [boot_info[room].pop(0)]
        for i in boot_info[room]:
            if time_stack[-1] + 1 == i:
                time_stack.append(i)
            else:
                available.append((time_stack[0], time_stack[-1] + 1))
                time_stack = [i]
        available.append((time_stack[0], time_stack[-1] + 1))
        

        print(f'Room {room}:')
        print(f'{len(available)} available:')
        for time in available:
            print(f'{time[0] if time[0] > 9 else "09"}-{time[1]}')
    else:
        print(f'Room {room}')
        print('Not available')

    if room != room_list[-1]:
        print('-----')
