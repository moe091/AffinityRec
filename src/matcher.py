import reddb.db as db
import mal as mal


#TODO:: add arg for # of matches to return
def getBestMatches(myData):
    matches = {}
    userMatchCount = {}

    for d in myData: #loop through all anime I have rated
        myScore = d['list_status']['score']
        if myScore != 0: #if my rating for anime d isn't a 0(unrated), then
            # animeFile = open("../data/" + str(d['node']['id']) + ".txt")
            # ani = animeFile.readlines() #read in all user ratings for anime d

            ani = db.getAllAnimeRatings(d['node']['id']) #returns dict of username:score

            for k in ani: #loop through each users rating for anime d
                # user,score = l.split("||") #get username and score for anime d
                user = k
                score = ani[k]

                #increase matchCount by 1 for this user
                if user in userMatchCount:
                    userMatchCount[user]+= 1
                else:
                    userMatchCount[user] = 1

                ##NEXT: calculate affinity score by simply adding 2-(diff between my score and theirs)
                ##also, in addition to affinity score, add a weight to each user, which could just be the # of 
                #anime incommon - 5 or something(negative scores will be zeroed, so they don't count at all instead of counting negatively)

                if user in matches:
                    matches[user] = matches[user] + 2 - abs(myScore - int(score))
                else:
                    matches[user] = 2 - abs(myScore - int(score))

    orderedMatches = {}
    for m in matches:
        n = matches[m]
        if userMatchCount[m] > 4: #user needs at least 3 ratings in common to be considered
            mScore = n / userMatchCount[m]
            if mScore in orderedMatches:
                orderedMatches[mScore].append(m)
            else:
                orderedMatches[mScore] = [m]

    ky = list(orderedMatches.keys())
    ky.sort(reverse = True)
    bestMatches = []
    for k in ky:
        if len(bestMatches) < 30:
            bestMatches = bestMatches + orderedMatches[k]
        else:
            break

    def mapResult(v):
        return [v, matches[v]]
    
    return list(map(mapResult, bestMatches))

# print(mal)
# m = getBestMatches("moe091", mal.readToken())
# print(m)


##TODO:: After getting the x best matches:
#use MAL api to grab full data for each of those users
#create a dict using animeId as key, value is an array containing all ratings from the users(if original user already rated animeId, don't add to dict)
    #generate affinity value for each animeId. This will be based on the average rating of all users, and then will be weighted based on how many of the users rated it
    #in the future each similar user will have its own weighting based on their similarity to original user, and this weighting will be used when averaging the user ratings.
    #after each animeId gets it's weighted affinity score, grab the title for that animeId and share recommendations with user



















    # bestMatches = {}
    # bestMatch = 3
    # for m in matches:
    #     if matches[m] > bestMatch:
    #         bestMatches = {m: matches[m]}
    #         bestMatch = matches[m]
    #     elif matches[m] == bestMatch:
    #         bestMatches[m] = matches[m]
    #
    # print(bestMatches)



##TODO::
    #get list of all files in data folder
    #loop through all files
        #for each file, create a dict and store username: score in a dict, this will remove duplicates
        #rewrite a new file from dict to replace old one with duplicates

    #once I fix files, change the bestmatches algo to sort all users with matches in order of # of matches, then
    #i can easily use the top X matches to compare and find common highly-rated anime that haven't been rated by
    #the original user yet
