import mal as mal
import matcher as matcher
import averager as averager




if __name__ == "__main__":
    username = "moe091"
    token = mal.readToken()
    
    myData = mal.requestUserData(username, token)['data']
    matches = matcher.getBestMatches(myData)
    avgs = averager.getAverages(matches, token)
    #print("AVGS: ", avgs['Manceyy'])
