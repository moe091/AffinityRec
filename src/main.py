import mal as mal
import matcher as matcher
import averager as averager




if __name__ == "__main__":
    username = "kush_master420"
    token = mal.readToken()
    
    # mean = mal.getAnimeScore(31646, token)

    myData = mal.requestUserData(username, token)['data']
    myIds = []
    print("LENGTH :: ", len(myData))
    for d in myData:
        ani = d['node']
        myIds.append(ani['id'])

    print(myIds)
    matches = matcher.getBestMatches(myData)
    avgs = averager.getAverages(matches, token, myIds, 40)
    diffs = averager.getDifferences(avgs, token)
    
    for r in diffs:
        print(str(r['id']) + "| " + r['name'] + " - " + str(r['diff']) + ". " + str(r['score']))


    #print("AVGS: ", avgs['Manceyy'])
