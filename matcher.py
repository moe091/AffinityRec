import main

def getBestMatches(username, token):
    #token = main.readToken()
    myData = main.requestUserData(username, token)['data']
    matches = {}

    for d in myData:
        myScore = d['list_status']['score']
        if myScore != 0:
            animeFile = open("data/" + str(d['node']['id']) + ".txt")
            ani = animeFile.readlines()

            for l in ani:
                user,score = l.split("||")
                if int(score) == myScore:
                    if user in matches:
                        matches[user] = matches[user] + 1
                    else:
                        matches[user] = 1

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
        if len(bestMatches) < 20:
            bestMatches = bestMatches + orderedMatches[k]
        else:
            break

    return bestMatches

# m = getBestMatches("moe091", main.readToken())
# print(m)






















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
