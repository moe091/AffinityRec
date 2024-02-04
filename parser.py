import json

with open("sample.json") as file:
    print("opened file")
    lines = file.readlines()
    print("lines = ", len(lines))
    for l in lines:
        user = json.loads(l)
        print("Reading " + user['username'])
        data = user['data']
        for k in data:
            anime = data[k]
            animeFile = open("data/" + k + ".txt", "a")
            animeFile.write(user['username'] + "||" + str(anime['score']) + "\n")
            animeFile.close()
            #open file:  k (animeId)
            #append line: user['username']||anime['score']

print("DONE!!!!!!!!!!")
