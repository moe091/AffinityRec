import urllib.request
import json
import requests
from types import SimpleNamespace



def getToken() -> str:
    r = requests.post("https://myanimelist.net/v1/oauth2/token",  data={'client_id': 'd805e23abfb5ceef8043f6422bfb0c87', 'code': 'def5020024dabe94ffca786a2fb9d872fe13d6ab51afb617dea87ca0377392dde723c59a35e772b3ffc27a6f309222cf13f0cce9062d0ac6c738abb0d5789cc86c5d4fa22a9a148c492bc0912d4530b0db593fefeb9c3ab85e180dd4ce793dbd8665e940303275f05d9a0f878719e1f9be9174660f8bfc5f4ec520cea445234fd36a1e26f5c69b0b497482b66038e13148369f011dbb31051bd6c232ef7a9de91bd3f5284d52c7ac3a126af6464c29e16d9402dfb1d29b051e260a61439ab8764aa367ad1e6346daddf447bb1abc0d777710afb8e0d1b0c101bc42dfabe181307edec081afd089711deda7457d74b1f5913445dbf64e012aa19701d5a19742ca9ce1c519fefaa7d4913457a0336d2c9dd2ed31ffddfd6b2f0ae96f590e5578d1b7319af28bda17cd3a53a79b68ce5b1f9dc351d317addd25eedeedd803e29fee75a861f44ea8274bfcef96a73c908ebc484e878cf43e4fe92e7fa97c8fbd2825aba9a216a155dfc97eace567f7d75641d326fa2b650559399703cedb6ab4cf6930b00e18c4dd52aafb55e7c27e9c1b341d24a968e26cff446326f7478ee41eeeef4f53569fcbaec167ce7fb6d768e80e8004df34f3aabbd71ab6715963bc3b448c930dd5d67a97808ff7f717260545c3bb918693afef3d2bfe1ba0c44adc51b62e033b4155dcb77c1cc5', 'code_verifier': 'cHVKOBIomkkhIqNO_ZtuwFoj3gI3Ka6RpKqkcrVYxLNEIejBnnB-jebe4NFUMByGRuAhLQQZiBW4qNsHPUDIBpcIFMyDO449qaH6T5nsYu9lnJLQ-AmFPJfbYTe5e_71', 'grant_type': 'authorization_code'})

    x = json.loads(r.text)
    return x


def readToken() -> str:
    with open('token.json') as f:
        d = json.load(f)
        return d['access_token']


def getUsersList():
    file = open("namelist.txt")
    data = file.read()
    file.close()
    return data.split("\n")


def requestUserData(user, token) -> str:
    r = requests.get("https://api.myanimelist.net/v1/users/" + user + "/animelist?limit=1000&fields=list_status", headers={'Authorization': 'Bearer ' + token})

    x = json.loads(r.text)
    return x


def requestUsersData(users, token):
    usersData = {}
    for u in users:
        usersData[u] = {}
        try:
            userData = requestUserData(u, token)
            usersData[u]['username'] = u
            usersData[u]['data'] = {}
            for d in userData['data']:
                o = {
                    'title': d['node']['title'],
                    'id': d['node']['id'],
                    'status': d['list_status']['status'],
                    'score': d['list_status']['score']
                }

                #don't include ratings of 0
                if d['list_status']['score'] > 0:
                    usersData[u]['data'][o['id']] = o

            if (len(usersData[u]['data']) < 20):
                print("NOT USING DATA FOR " + u + ". ONLY CONTAINS " + str(len(usersData[u]['data'])) + " RATINGS!!!!!!!!!!!!!.")
                del usersData[u]
            else:
                print("Got data for " + u + ". Contains " + str(len(usersData[u]['data'])) + " ratings.")
        except:
            print("FAILED TO GET DATA FOR ", u)

    print(usersData)
    return usersData

def writeUsersData(users, token):
    usersData = requestUsersData(users, token)
    with open("sample.json", "a") as outfile:
        for d in usersData:
            json.dump(usersData[d], outfile)
            outfile.write("\n")


if __name__ == "__main__":
    token = readToken()
    d = requestUserData("freere", token)['data']
    for l in d:
        print("\n")
        print(l)
    # print("GOT TOKEN ")
    #
    # l = getUsersList()
    #
    #
    # #grab user data and write after every 10 so I don't lose everything if something goes wrong before completion
    # for i in range(0, int(len(l) / 10)):
    #     print("Getting Users Data for users " + str(i*10) + " through " + str(i*10+9))
    #     writeUsersData(l[i*10:i*10+9], token)
    #
    # print(len(l))
