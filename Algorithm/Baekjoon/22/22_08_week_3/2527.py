for _ in range(4):
    lef_1, bot_1, rig_1, top_1, lef_2, bot_2, rig_2, top_2 = map(int, input().split())
    if rig_1 < lef_2 or lef_1 > rig_2 or top_1 < bot_2 or top_2 < bot_1:
        print('d')
    elif (rig_1 == lef_2 and top_1 == bot_2) or (top_1 == bot_2 and lef_1 == rig_2) or (top_2 == bot_1 and rig_2 == lef_1) or (rig_1 == lef_2 and bot_1 == top_2):
        print('c')    
    elif rig_1 == lef_2 or rig_2 == lef_1 or top_1 == bot_2 or top_2 == bot_1:
        print('b')
    else:
        print('a')
