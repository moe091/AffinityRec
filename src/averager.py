import mal as mal

#takes in an array of usernames and finds the average ratings for all media rated by those users
#output format is a dict. key is the animeId, value is a 2-element list where l[0]=rating, l[1]=number of users who rated it
def sortScores(a):
    return a[1]

def getAverages(users, token):
    usersData = mal.requestUsersData(users, token)
    scores = {}
    animeNames = {}
    for user in usersData:
        data = usersData[user]['data']
        for a in data:
            animeNames[data[a]['id']] = data[a]['title']
            animeId = data[a]['id']
            animeScore = data[a]['score']
           
            if animeId in scores:
                cur = scores[animeId]
                cur['scores'].append(animeScore)
                cur['count'] += 1
            else:
                scores[animeId] = {}
                scores[animeId]['scores'] = [animeScore]
                scores[animeId]['count'] = 1
    
    affScores = {}
    for k in scores:
        if scores[k]['count'] >= 10:
            affScores[k] = scores[k]

    sortedScores = []
    for k in affScores:
        anime = affScores[k]
        total = 0
        for s in anime['scores']:
            total+= s
        anime['avg'] = total / anime['count']
        sortedScores.append([k, anime['avg']])
        #print(str(k) + " - " + str(anime['avg']))

    sortedScores.sort(key=sortScores)
    for s in sortedScores:
        # print(s[0], s[1])
        print(str(animeNames[s[0]]) + " - " + str(s[1]))




    return affScores