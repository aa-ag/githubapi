############------------ IMPORTS ------------############
import requests
import pprint
import settings
import subprocess

############------------ GLOBAL VARIABLE(S) ------------############
github_auth = settings.GITHUB_AUTH

############------------ FUNCTION(S) ------------############
def hit_end_point():
    '''
     imports github auth from settings,
     hits enpoint, creates a json with it, 
     and prettyprints the jston with an 
     indentation of 4 spaces (2 tabs)
    '''
    request = requests.get('https://api.github.com/users/aa-ag/repos', data=github_auth)
    
    request = request.json()

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(request)

    for repo in request:
        print(repo['html_url'])


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    hit_end_point()

'''
https://github.com/aa-ag/5artists_Angular
https://github.com/aa-ag/About_Time
https://github.com/aa-ag/astp
https://github.com/aa-ag/audiobooks
https://github.com/aa-ag/Avengers_Phonebook
https://github.com/aa-ag/bicycles_rental
https://github.com/aa-ag/bitcoinprice
https://github.com/aa-ag/blog
https://github.com/aa-ag/bootstrap
https://github.com/aa-ag/calculator
https://github.com/aa-ag/camelstuff
https://github.com/aa-ag/chipy.org
https://github.com/aa-ag/clock.js
https://github.com/aa-ag/commands
https://github.com/aa-ag/computer-science
https://github.com/aa-ag/cookiescacheclear
https://github.com/aa-ag/counting_stuff
https://github.com/aa-ag/cpython
https://github.com/aa-ag/css-animations
https://github.com/aa-ag/CSVstuff
https://github.com/aa-ag/curriculum
https://github.com/aa-ag/dadjokes
https://github.com/aa-ag/deleteemails
https://github.com/aa-ag/delhistory
https://github.com/aa-ag/designing-programs
https://github.com/aa-ag/developer-roadmap
https://github.com/aa-ag/dirtree
https://github.com/aa-ag/discrete
https://github.com/aa-ag/dmwp
https://github.com/aa-ag/domain_data
'''