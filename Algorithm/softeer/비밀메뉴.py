m, k, n = map(int , input().split())
secret = input().replace(' ', '')
button = input().replace(' ', '')

if button.find(secret) >= 0:
    print('secret')
else:
    print('normal')
