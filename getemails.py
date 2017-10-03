import urllib2
import json

f = open('contacts.json', 'a')

with open('accounts.txt') as rf:
    lines = rf.readlines()
    for user in lines:
        user = user.replace('\n', '')
        print user
        response = urllib2.urlopen('https://api.github.com/users/' + user + '/events/public')
        data = json.load(response)

        for i in range(len(data)):
            if data[i].has_key('payload'):
                if data[i]['payload'].has_key('commits'):
                    if len(data[i]['payload']['commits']) > 0:
                        author = data[i]['payload']['commits'][0]['author']
                        print author['email']
                        f.write(json.dumps(author) + ',\n')
                        break
f.close