import mal as mal
#takes in an array of usernames and finds the average ratings for all media rated by those users
#output format is a dict. key is the animeId, value is a 2-element list where l[0]=rating, l[1]=number of users who rated it
def sortScores(a):
    return a[1]

def getAverages(users, token, ignoreIds, count):
    usernames = []
    matchValues = {}
    minMatchVal = -1
    for val in users:
        usernames.append(val[0])
        matchValues[val[0]] = val[1]
        if minMatchVal < 0 or val[1] < minMatchVal:
            minMatchVal = val[1]
    
    usersData = mal.requestUsersData(usernames, token)
    scores = {}
    animeNames = {}
    for match in usersData: #loop through each matched user
        user = match
        matchVal = matchValues[user]
        data = usersData[user]['data']

        for a in data: #loop through each anime for current user
            animeNames[data[a]['id']] = data[a]['title'] #create id-to-title mapping for use later
            animeId = data[a]['id']
            animeScore = data[a]['score']
            
            if animeId in ignoreIds: #ignoreIds are already rated by main user, don't include those in results
                continue

            if animeId in scores:
                cur = scores[animeId]
                cur['scores'].append([animeScore, matchVal - (minMatchVal / 2)])
                cur['count'] += 1
            else:
                scores[animeId] = {}
                scores[animeId]['scores'] = [[animeScore, matchVal - (minMatchVal / 2)]]
                scores[animeId]['count'] = 1
    

    affScores = {} #grab all scores with at least X matches
    for k in scores:
        if scores[k]['count'] >= 3:
            affScores[k] = scores[k]

    sortedScores = []
    for k in affScores:
        anime = affScores[k]
        total = 0
        weightedCount = 0
        for s in anime['scores']:
            total+= s[0] * s[1]
            weightedCount+= s[1]
        anime['avg'] = total / weightedCount
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


    print("AVERAGER RESULTS:", results)
    return results



def sortDiffs(val):
    #return (val['diff'] * 1) 
    return (val['diff'] * 2) + val['score']

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