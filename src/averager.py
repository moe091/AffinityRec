import mal as mal

#takes in an array of usernames and finds the average ratings for all media rated by those users
#output format is a dict. key is the animeId, value is a 2-element list where l[0]=rating, l[1]=number of users who rated it
def sortScores(a):
    return a[1]

def getAverages(users, token, ignoreIds, count):
    usersData = mal.requestUsersData(users, token)
    scores = {}
    animeNames = {}
    for user in usersData:
        data = usersData[user]['data']
        for a in data:
            animeNames[data[a]['id']] = data[a]['title']
            animeId = data[a]['id']
            animeScore = data[a]['score']
            
            if animeId in ignoreIds:
                continue

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
        if scores[k]['count'] >= 2:
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
    # for s in sortedScores:
    #     print(str(s[0]) + " - " + str(animeNames[s[0]]) + " - " + str(s[1]))

    results = []
    length = min(len(sortedScores), count)
    for i in range(len(sortedScores) - length, len(sortedScores)):
        s = sortedScores[i]
        result = {}
        result['id'] = s[0]
        result['name'] = animeNames[s[0]]
        result['score'] = s[1]
        results.insert(0, result)


    return results



def sortDiffs(val):
    #return (val['diff'] * 1) 
    return (val['diff'] * 3) + val['score']

#takes in a list of results(such as the one returned by getAverages) 
#and adds a 'diff' property to each one.
#diff is the affinityScore of an anime for a particular user, minus the average rating for that anime.
#a high diff means an anime is more suited for a user than it is for the average viewer.
def getDifferences(scores, token):
    for s in scores:
        mean = mal.getAnimeScore(s['id'], token)
        s['diff'] = s['score'] - mean #recommended score minus average rating. 
    
    scores.sort(key=sortDiffs)
    return scores


#affSCore will be diff + score, so base score still counts but it is heavily weighted by diff from mean. 
#without this the top rated MAL anime will be recommended to everyone way too often