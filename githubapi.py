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
    url = 'https://api.github.com/users/aa-ag/repos?per_page=144'

    request = requests.get(url, data=github_auth)
    
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
https://github.com/aa-ag/download
https://github.com/aa-ag/ds_and_a_projects
https://github.com/aa-ag/emc2
https://github.com/aa-ag/emptytrash
https://github.com/aa-ag/endecrypter
https://github.com/aa-ag/f1_stangins
https://github.com/aa-ag/filecount
https://github.com/aa-ag/fileuploader
https://github.com/aa-ag/first-contributions
https://github.com/aa-ag/flaskapi
https://github.com/aa-ag/freecodecamp1outof5
https://github.com/aa-ag/freecodecamp2outof5
https://github.com/aa-ag/freecodecamp3outof5
https://github.com/aa-ag/freecodecamp4outof5
https://github.com/aa-ag/freecodecamp5outof5
https://github.com/aa-ag/fullstack
https://github.com/aa-ag/fullstack-nanodegree-vm
https://github.com/aa-ag/gamapi
https://github.com/aa-ag/githubapi
https://github.com/aa-ag/github_collab_lab
https://github.com/aa-ag/gitignore
https://github.com/aa-ag/googlesearch
https://github.com/aa-ag/groomer
https://github.com/aa-ag/hangman
https://github.com/aa-ag/haystack
https://github.com/aa-ag/hofvidz
https://github.com/aa-ag/HTMLHint
https://github.com/aa-ag/ignoresnippet
https://github.com/aa-ag/I_Know_Sports
https://github.com/aa-ag/jsprojects
https://github.com/aa-ag/JS_funfacts
https://github.com/aa-ag/launchurls
https://github.com/aa-ag/LawFirmSite
https://github.com/aa-ag/lol
https://github.com/aa-ag/lunchreminder
https://github.com/aa-ag/magic8ball
https://github.com/aa-ag/markets
https://github.com/aa-ag/miniremesh
https://github.com/aa-ag/movefiles
https://github.com/aa-ag/movie_theater_database
https://github.com/aa-ag/nano
https://github.com/aa-ag/off
https://github.com/aa-ag/orbit-model
https://github.com/aa-ag/passwordcracker
https://github.com/aa-ag/passwordgenerator
https://github.com/aa-ag/pcc_2e
https://github.com/aa-ag/pdfs
https://github.com/aa-ag/pg13
https://github.com/aa-ag/phcopy
https://github.com/aa-ag/phonenums
https://github.com/aa-ag/piedpiper
https://github.com/aa-ag/piglatintranslator
https://github.com/aa-ag/project_garage
https://github.com/aa-ag/project_roi
https://github.com/aa-ag/project_sam
https://github.com/aa-ag/pylexa
https://github.com/aa-ag/python-guide
https://github.com/aa-ag/ratings
https://github.com/aa-ag/recipes
https://github.com/aa-ag/redditclone
https://github.com/aa-ag/reformat
https://github.com/aa-ag/RESTcountries
https://github.com/aa-ag/scraper
https://github.com/aa-ag/sec
https://github.com/aa-ag/sendemails
https://github.com/aa-ag/sentiment
https://github.com/aa-ag/signin_final
https://github.com/aa-ag/simple-rss-reader
https://github.com/aa-ag/slacknot
https://github.com/aa-ag/sms
'''