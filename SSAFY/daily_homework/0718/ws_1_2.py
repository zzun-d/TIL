post = int(input('게시글의 총 갯수를 입력하세요 : '))
post_per_page = int(input('한 페이지에 필요한 게시글 수를 입력하세요 : '))
print((post-1)//post_per_page + 1)
