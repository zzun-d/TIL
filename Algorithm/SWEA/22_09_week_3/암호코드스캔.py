dct1 = {'0':'0000', '1':'0001', '2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
dct3 = {'211':0,'221':1,'122':2,'411':3,'132':4,'231':5,'114':6,'312':7,'213':8,'112':9}

T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    arr = [input() for _ in range(R)]
    old_st = []
    ans = []
    for st in arr:
        if st != old_st and st.count('0') != len(st):
            old_st = st    
            bst = ''
            for ch in st:
                bst += dct1[ch]
 
            old = 0
            cnts = []
            for i in range(len(bst)):
                if bst[old]!=bst[i]:
                    cnts.append(i-old)
                    old = i
 
            pwd=[]
            for i in range(1, len(cnts), 4):
                mn = min(cnts[i:i+3])
                key = str(cnts[i]//mn)+str(cnts[i+1]//mn)+str(cnts[i+2]//mn)
                pwd.append(dct3[key])
 
            for i in range(0, len(pwd), 8):
                if pwd[i:i+8] not in ans:
                    ans.append(pwd[i:i+8])
 
    sol = 0
    for code in ans:
        even = code[0]+code[2]+code[4]+code[6]
        odd = code[1]+code[3]+code[5]+code[7]
        if (even*3 + odd)%10 == 0:
            sol += even+odd
 
    print(f'#{tc} {sol}')