import random
from collections import defaultdict

movies = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
users = list('abcdefghijklmnopqrstuvwxyz')
reviews_user = defaultdict(list)
reviews_movie = defaultdict(list)
user_user_recommend = []
global_recommend = []

for user in users:
    for _ in range(random.randint(1, 10)):
        movie_idx = movies[random.randint(0, 25)]
        rank = round(random.random()*5, 2)
        reviews_user[user].append((movie_idx, rank))
        reviews_movie[movie_idx].append((user, rank))

I = 'a'
I_watched = set()
user_user_score = defaultdict(lambda: 5)
for user_info in reviews_user[I]:
    movie = user_info[0]
    I_rank = user_info[1]
    I_watched.add(movie)
    print(f'내가 본 영화 : {movie}')
    print(f'내가 준 평점 : {I_rank}')
    for movie_info in reviews_movie[movie]:
        user = movie_info[0]
        you_rank = movie_info[1]
        user_user_score[user] += 2.5 - abs(I_rank - you_rank)

user_user_list = []
user_user_keys = list(set(user_user_score.keys()) - {I})
for user in user_user_keys:
    user_user_list.append((user_user_score[user], user))

user_user_list.sort(reverse=True)

movie_score = defaultdict(list)
result = []
for score, user in user_user_list:
    if score <= 5:
        break
    for movie_idx, you_rank in reviews_user[user]:
        if I_watched.intersection(set(movie_idx)):
            continue

        if movie_score[movie_idx]:
            movie_score[movie_idx][0] += round(you_rank*(user_user_score[user]-5), 2)
            movie_score[movie_idx][1] += round(user_user_score[user]-5, 2)
            movie_score[movie_idx][2] += 1
        else:
            movie_score[movie_idx] = [round(you_rank*(user_user_score[user]-5), 2), round(user_user_score[user]-5, 2), 1]

for k in movie_score.keys():    
    result.append((movie_score[k][0]/(movie_score[k][1]/movie_score[k][2]), k))

result.sort(reverse=True)

