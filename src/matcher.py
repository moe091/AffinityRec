
#TODO:: add arg for # of matches to return
def getBestMatches(myData):
    #myData = mal.requestUserData(username, token)['data']
    matches = {}

    for d in myData:
        myScore = d['list_status']['score']
        if myScore != 0:
            animeFile = open("../data/" + str(d['node']['id']) + ".txt")
            ani = animeFile.readlines()

            for l in ani:
                user,score = l.split("||")
                ##NEXT: calculate affinity score by simply adding 2-(diff between my score and theirs)
                ##also, in addition to affinity score, add a weight to each user, which could just be the # of 
                #anime incommon - 5 or something(negative scores will be zeroed, so they don't count at all instead of counting negatively)
                if int(score) == myScore:
                    if user in matches:
                        matches[user] = matches[user] + 1
                    else:
                        matches[user] = 1
                if abs(int(score) - myScore) > 2: #if rating is off by more than 3 then deduct an affinity point. 
                    if user in matches:
                        matches[user] = matches[user] - 1
                    else:
                        matches[user] = -1

    orderedMatches = {}
    for m in matches:
        n = matches[m]
        if n in orderedMatches:
            orderedMatches[n].append(m)
        else:
            orderedMatches[n] = [m]

    ky = list(orderedMatches.keys())
    ky.sort(reverse = True)
    bestMatches = []
    for k in ky:
        if len(bestMatches) < 9:
            bestMatches = bestMatches + orderedMatches[k]
        else:
            break

    return bestMatches

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
