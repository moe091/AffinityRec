from os import listdir

dir = listdir('data')

for filename in dir:
    users = {}
    file = open('data/' + filename)
    lines = file.readlines()
    for l in lines:
        user,score = l.split("||")
        users[user] = score
    file.close()

    newfile = open('data2/' + filename, 'a')
    for u in users:
        newfile.write(u + '||' + users[u])
    newfile.close()
