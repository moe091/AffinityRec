import redis
from os import listdir

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# r.set('foo', 'bar')
# print('set done')
# print('getting foo: ', r.get('foo'))
#print(r.hgetall('ani1'))



# dirs = listdir('../../data')
# for filename in dirs:
#     print(filename)
#     file = open('../../data/' + filename)
#     lines = file.readlines()
#     for l in lines:
#         user,score = l.split("||")
#         r.hset('ani' + filename.split('.')[0], user, score.strip())
#     file.close()



def getRating(animeId, username):
    return r.hget('ani' + str(animeId), username)

def getAllAnimeRatings(animeId):
    return r.hgetall('ani' + str(animeId))



# using animeId 123 for example
# ratings will be stored using the key 'ani123'
# value will be a hashmap of {username,rating}
#   redis.hset('ani123', 'moe091', 9) - sets rating of 9 for anime #123 by user moe091
#   redis.hget('ani123', 'moe091') - gets moes rating specificall
# all = r.hgetall('ani5') # returns ALL ratings for ani123, this is what I'll have to use in matcher.py
# print("ALL = ", all)



# for k in r.scan_iter(match='*'):
#     print("key=", k)










# from os import listdir

# dir = listdir('data')

# for filename in dir:
#     users = {}
#     file = open('data/' + filename)
#     lines = file.readlines()
#     for l in lines:
#         user,score = l.split("||")
#         users[user] = score
#     file.close()

#     newfile = open('data2/' + filename, 'a')
#     for u in users:
#         newfile.write(u + '||' + users[u])
#     newfile.close()

