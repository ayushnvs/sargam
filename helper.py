import json

def readEnviron():
    with open('./.env') as env:
        content = env.read()
    return json.loads(content)