############------------ IMPORTS ------------############
import requests
import pprint
import settings

############------------ GLOBAL VARIABLE(S) ------------############
github_token = settings.GITHUB_TOKEN

############------------ FUNCTION(S) ------------############
def hit_end_point():

    request = requests.get('https://api.github.com/notifications', auth=('aa-ag', github_token))
    
    print(request.json())


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    hit_end_point()