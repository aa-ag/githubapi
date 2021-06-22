############------------ IMPORTS ------------############
import requests
import pprint
import settings

############------------ GLOBAL VARIABLE(S) ------------############
github_auth = settings.GITHUB_AUTH

############------------ FUNCTION(S) ------------############
def hit_end_point():
    request = requests.get('https://api.github.com/users/aa-ag/repos', data=github_auth)
    request = request.json()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(request)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    hit_end_point()