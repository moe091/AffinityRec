import mal as mal
import matcher as matcher




if __name__ == "__main__":
    username = "moe091"
    token = mal.readToken()
    
    myData = mal.requestUserData(username, token)['data']
    matches = matcher.getBestMatches(myData)
    print("MATCHES = ", matches)
