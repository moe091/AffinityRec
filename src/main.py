import mal as mal
import matcher as matcher
import averager as averager

# x - update code to read data from redis instead of text files
#weight matches for anime with lower total views higher
    # x - add func to get # of scores for an anime
    # create weighting curve with min/max values. e.g.  <50k=2x, 50k-200k=~2-0.5, >200k=0.5
    # add weighting to matcher.py
#slightly increase affscore for anime with lower total views??
#weight matches with other users based on how popular common animes are(less common = better match)
    # Implement popularity multiplier(getPopMulti function in MAL). Returns values from 0.8 to 1.2.
#weight matches with other users HEAVILY when you have common ratings for an anime, and that rating varies from the average
    # in matcher, grab the mean for each anime before looping through other users ratings
    # when looping through userRatings, average myScore and score, then subtract that val from the MAL mean score to get a diff(don't forget to use absolute value!!).
    # weight the match value using the diff. e.g. if me and user have exact same rating(which would usually give +2 matchScore), instead of just adding
        # 2, multiply that 2 by a diff weight modifier. diff < 1 modifier = 0. diff > 1 modifier = root(diff - 1)? 
        #if avg is a 9 and you and other user rate it a 5, then the weight would be doubled. if avg is 7.5 and you and other user rate it 9, weight would be ~1.224
# x- Add an affinityScore for users who you match with based on how well you match up, affinity score will be used to weight animes they rated when making recommendations
#use 'related_anime' field from MAL to combine seasons into single anime - do this at the results level so individual season ratings don't get conflated, but we can avoid recommending 5 seasons of the same anime
#average out a users matchScore with how many anime they matched on, so you get matched with ppl who have similar tastes instead of ppl who have rated all the anime
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
    #print("MATCHES: ", matches)
    avgs = averager.getAverages(matches, token, myIds, 40)
    diffs = averager.getDifferences(avgs, token)
    
    for r in diffs:
        print(str(r['id']) + "| " + r['name'] + " - " + str(r['diff']) + ". " + str(r['score']))
