T = int(input())
for tc in range(1, T+1):
    S = input()
    cards = [S[i:i+3] for i in range(0, len(S), 3)]
    deck = {'S':[], 'D':[], 'H':[], 'C':[]}
    ans = {'S':13, 'D':13, 'H':13, 'C':13}
    for card in cards:
        if card[1:] in deck[card[0]]:
            ans = False
            break
        else:
            deck[card[0]].append(card[1:])
            ans[card[0]] -= 1
    if ans:
        print(f'#{tc}', *ans.values())
    else:
        print(f'#{tc} ERROR')
