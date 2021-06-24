############------------ IMPORTS ------------############
import requests
import pprint
import settings
import subprocess

'''
Requests that return multiple items will be paginated to 30 items by default. 
You can specify further pages with the page parameter. 
For some resources, you can also set a custom page size up to 100 with the per_page parameter. 
Note that for technical reasons not all endpoints respect the per_page parameter, 
see events for example.

source: https://docs.github.com/en/rest/overview/resources-in-the-rest-api#pagination
''' 

############------------ GLOBAL VARIABLE(S) ------------############
github_auth = settings.GITHUB_AUTH
destination_path = settings.DESTINATION



############------------ FUNCTION(S) ------------############
def save_locally():
    '''
     helper function to `clone` each repo
     locally to a give path -- for now
     manually adding url & path
    '''
    repo_being_cloned = 'https://github.com/aa-ag/groomer'
    path_where_repo_will_be_cloned_to = destination_path

    command = ["git", "clone", repo_being_cloned]

    subprocess.run(command, cwd=path_where_repo_will_be_cloned_to)

    '''
     If cwd is not None, the function changes the working directory
     to cwd before executing the child.
    '''


def hit_end_point():
    '''
     imports github auth from settings,
     hits enpoint, creates a json with it, 
     and prettyprints the jston with an 
     indentation of 4 spaces (2 tabs)
    '''
    global github_auth

    page = 1
    n = 1

    # #### check requests status to see if limit was hit
    # url = f'https://api.github.com/users/aa-ag/repos?page={page}&per_page=100'

    # request = requests.get(url, data=github_auth)

    # print(request.status_code)
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(request)

    ### actual code
    while page < 3:
        url = f'https://api.github.com/users/aa-ag/repos?page={page}&per_page=100'

        request = requests.get(url, data=github_auth)
        
        request = request.json()

        for repo in request:
            print(n, repo['html_url'])
            n += 1

        page += 1


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    # hit_end_point()
    hit_end_point()
    # 403
    # save_locally()

'''
1 https://github.com/aa-ag/5artists_Angular
2 https://github.com/aa-ag/About_Time
3 https://github.com/aa-ag/astp
4 https://github.com/aa-ag/audiobooks
5 https://github.com/aa-ag/Avengers_Phonebook
6 https://github.com/aa-ag/bicycles_rental
7 https://github.com/aa-ag/bitcoinprice
8 https://github.com/aa-ag/blog
9 https://github.com/aa-ag/bootstrap
10 https://github.com/aa-ag/calculator
11 https://github.com/aa-ag/camelstuff
12 https://github.com/aa-ag/chipy.org
13 https://github.com/aa-ag/clock.js
14 https://github.com/aa-ag/commands
15 https://github.com/aa-ag/computer-science
16 https://github.com/aa-ag/cookiescacheclear
17 https://github.com/aa-ag/counting_stuff
18 https://github.com/aa-ag/cpython
19 https://github.com/aa-ag/css-animations
20 https://github.com/aa-ag/CSVstuff
21 https://github.com/aa-ag/curriculum
22 https://github.com/aa-ag/dadjokes
23 https://github.com/aa-ag/deleteemails
24 https://github.com/aa-ag/delhistory
25 https://github.com/aa-ag/designing-programs
26 https://github.com/aa-ag/developer-roadmap
27 https://github.com/aa-ag/dirtree
28 https://github.com/aa-ag/discrete
29 https://github.com/aa-ag/dmwp
30 https://github.com/aa-ag/domain_data
31 https://github.com/aa-ag/download
32 https://github.com/aa-ag/ds_and_a_projects
33 https://github.com/aa-ag/emc2
34 https://github.com/aa-ag/emptytrash
35 https://github.com/aa-ag/endecrypter
36 https://github.com/aa-ag/f1_stangins
37 https://github.com/aa-ag/filecount
38 https://github.com/aa-ag/fileuploader
39 https://github.com/aa-ag/first-contributions
40 https://github.com/aa-ag/flaskapi
41 https://github.com/aa-ag/freecodecamp1outof5
42 https://github.com/aa-ag/freecodecamp2outof5
43 https://github.com/aa-ag/freecodecamp3outof5
44 https://github.com/aa-ag/freecodecamp4outof5
45 https://github.com/aa-ag/freecodecamp5outof5
46 https://github.com/aa-ag/fullstack
47 https://github.com/aa-ag/fullstack-nanodegree-vm
48 https://github.com/aa-ag/gamapi
49 https://github.com/aa-ag/githubapi
50 https://github.com/aa-ag/github_collab_lab
51 https://github.com/aa-ag/gitignore
52 https://github.com/aa-ag/googlesearch
53 https://github.com/aa-ag/groomer
54 https://github.com/aa-ag/hangman
55 https://github.com/aa-ag/haystack
56 https://github.com/aa-ag/hofvidz
57 https://github.com/aa-ag/HTMLHint
58 https://github.com/aa-ag/ignoresnippet
59 https://github.com/aa-ag/I_Know_Sports
60 https://github.com/aa-ag/jsprojects
61 https://github.com/aa-ag/JS_funfacts
62 https://github.com/aa-ag/launchurls
63 https://github.com/aa-ag/LawFirmSite
64 https://github.com/aa-ag/lol
65 https://github.com/aa-ag/lunchreminder
66 https://github.com/aa-ag/magic8ball
67 https://github.com/aa-ag/markets
68 https://github.com/aa-ag/miniremesh
69 https://github.com/aa-ag/movefiles
70 https://github.com/aa-ag/movie_theater_database
71 https://github.com/aa-ag/nano
72 https://github.com/aa-ag/off
73 https://github.com/aa-ag/orbit-model
74 https://github.com/aa-ag/passwordcracker
75 https://github.com/aa-ag/passwordgenerator
76 https://github.com/aa-ag/pcc_2e
77 https://github.com/aa-ag/pdfs
78 https://github.com/aa-ag/pg13
79 https://github.com/aa-ag/phcopy
80 https://github.com/aa-ag/phonenums
81 https://github.com/aa-ag/piedpiper
82 https://github.com/aa-ag/piglatintranslator
83 https://github.com/aa-ag/project_garage
84 https://github.com/aa-ag/project_roi
85 https://github.com/aa-ag/project_sam
86 https://github.com/aa-ag/pylexa
87 https://github.com/aa-ag/python-guide
88 https://github.com/aa-ag/ratings
89 https://github.com/aa-ag/recipes
90 https://github.com/aa-ag/redditclone
91 https://github.com/aa-ag/reformat
92 https://github.com/aa-ag/RESTcountries
93 https://github.com/aa-ag/scraper
94 https://github.com/aa-ag/sec
95 https://github.com/aa-ag/sendemails
96 https://github.com/aa-ag/sentiment
97 https://github.com/aa-ag/signin_final
98 https://github.com/aa-ag/simple-rss-reader
99 https://github.com/aa-ag/slacknot
100 https://github.com/aa-ag/sms
1 https://github.com/aa-ag/sounds
2 https://github.com/aa-ag/spellcheck
3 https://github.com/aa-ag/strongpassword
4 https://github.com/aa-ag/tictactoe
5 https://github.com/aa-ag/todoapp
6 https://github.com/aa-ag/tracephonenumber
7 https://github.com/aa-ag/transcripts
8 https://github.com/aa-ag/udacity
9 https://github.com/aa-ag/uniqueemails
10 https://github.com/aa-ag/urlshortener
11 https://github.com/aa-ag/validurl
12 https://github.com/aa-ag/venmolikeapi
13 https://github.com/aa-ag/viewsbot
14 https://github.com/aa-ag/w2d1py1-3jn
15 https://github.com/aa-ag/w2d2py1-2jn
16 https://github.com/aa-ag/w2d3py1-2jn
17 https://github.com/aa-ag/w2d4py1-2jn
18 https://github.com/aa-ag/w3_1n3_jn
19 https://github.com/aa-ag/w3_d4_regex-project_jn
20 https://github.com/aa-ag/w3_e1-2_jn
21 https://github.com/aa-ag/w3_e1-5_jn
22 https://github.com/aa-ag/w4d2_SQLhomework
23 https://github.com/aa-ag/W4D4_Joins-NestedQueries
24 https://github.com/aa-ag/w4d5_cardealership
25 https://github.com/aa-ag/w5d1_homework
26 https://github.com/aa-ag/w6d1-js
27 https://github.com/aa-ag/w6d2-js
28 https://github.com/aa-ag/w8d1_jn
29 https://github.com/aa-ag/w8_d3_jn
30 https://github.com/aa-ag/weatherApp-React
31 https://github.com/aa-ag/website
32 https://github.com/aa-ag/websiteblocker
33 https://github.com/aa-ag/Week5
34 https://github.com/aa-ag/whatsapp
35 https://github.com/aa-ag/whoisonwifi
36 https://github.com/aa-ag/wifipasswords
37 https://github.com/aa-ag/wifiswitch
38 https://github.com/aa-ag/wordcloud
39 https://github.com/aa-ag/wordcount
40 https://github.com/aa-ag/xmling
41 https://github.com/aa-ag/xmlpar
(base) taylormadlener@Taylors-MacBook-Air githubapi % /usr/local/bin/python3 /Users/taylormadlener/Desktop/aaron_temporary/githubapi/githubapi.py
1 https://github.com/aa-ag/5artists_Angular
2 https://github.com/aa-ag/About_Time
3 https://github.com/aa-ag/astp
4 https://github.com/aa-ag/audiobooks
5 https://github.com/aa-ag/Avengers_Phonebook
6 https://github.com/aa-ag/bicycles_rental
7 https://github.com/aa-ag/bitcoinprice
8 https://github.com/aa-ag/blog
9 https://github.com/aa-ag/bootstrap
10 https://github.com/aa-ag/calculator
11 https://github.com/aa-ag/camelstuff
12 https://github.com/aa-ag/chipy.org
13 https://github.com/aa-ag/clock.js
14 https://github.com/aa-ag/commands
15 https://github.com/aa-ag/computer-science
16 https://github.com/aa-ag/cookiescacheclear
17 https://github.com/aa-ag/counting_stuff
18 https://github.com/aa-ag/cpython
19 https://github.com/aa-ag/css-animations
20 https://github.com/aa-ag/CSVstuff
21 https://github.com/aa-ag/curriculum
22 https://github.com/aa-ag/dadjokes
23 https://github.com/aa-ag/deleteemails
24 https://github.com/aa-ag/delhistory
25 https://github.com/aa-ag/designing-programs
26 https://github.com/aa-ag/developer-roadmap
27 https://github.com/aa-ag/dirtree
28 https://github.com/aa-ag/discrete
29 https://github.com/aa-ag/dmwp
30 https://github.com/aa-ag/domain_data
31 https://github.com/aa-ag/download
32 https://github.com/aa-ag/ds_and_a_projects
33 https://github.com/aa-ag/emc2
34 https://github.com/aa-ag/emptytrash
35 https://github.com/aa-ag/endecrypter
36 https://github.com/aa-ag/f1_stangins
37 https://github.com/aa-ag/filecount
38 https://github.com/aa-ag/fileuploader
39 https://github.com/aa-ag/first-contributions
40 https://github.com/aa-ag/flaskapi
41 https://github.com/aa-ag/freecodecamp1outof5
42 https://github.com/aa-ag/freecodecamp2outof5
43 https://github.com/aa-ag/freecodecamp3outof5
44 https://github.com/aa-ag/freecodecamp4outof5
45 https://github.com/aa-ag/freecodecamp5outof5
46 https://github.com/aa-ag/fullstack
47 https://github.com/aa-ag/fullstack-nanodegree-vm
48 https://github.com/aa-ag/gamapi
49 https://github.com/aa-ag/githubapi
50 https://github.com/aa-ag/github_collab_lab
51 https://github.com/aa-ag/gitignore
52 https://github.com/aa-ag/googlesearch
53 https://github.com/aa-ag/groomer
54 https://github.com/aa-ag/hangman
55 https://github.com/aa-ag/haystack
56 https://github.com/aa-ag/hofvidz
57 https://github.com/aa-ag/HTMLHint
58 https://github.com/aa-ag/ignoresnippet
59 https://github.com/aa-ag/I_Know_Sports
60 https://github.com/aa-ag/jsprojects
61 https://github.com/aa-ag/JS_funfacts
62 https://github.com/aa-ag/launchurls
63 https://github.com/aa-ag/LawFirmSite
64 https://github.com/aa-ag/lol
65 https://github.com/aa-ag/lunchreminder
66 https://github.com/aa-ag/magic8ball
67 https://github.com/aa-ag/markets
68 https://github.com/aa-ag/miniremesh
69 https://github.com/aa-ag/movefiles
70 https://github.com/aa-ag/movie_theater_database
71 https://github.com/aa-ag/nano
72 https://github.com/aa-ag/off
73 https://github.com/aa-ag/orbit-model
74 https://github.com/aa-ag/passwordcracker
75 https://github.com/aa-ag/passwordgenerator
76 https://github.com/aa-ag/pcc_2e
77 https://github.com/aa-ag/pdfs
78 https://github.com/aa-ag/pg13
79 https://github.com/aa-ag/phcopy
80 https://github.com/aa-ag/phonenums
81 https://github.com/aa-ag/piedpiper
82 https://github.com/aa-ag/piglatintranslator
83 https://github.com/aa-ag/project_garage
84 https://github.com/aa-ag/project_roi
85 https://github.com/aa-ag/project_sam
86 https://github.com/aa-ag/pylexa
87 https://github.com/aa-ag/python-guide
88 https://github.com/aa-ag/ratings
89 https://github.com/aa-ag/recipes
90 https://github.com/aa-ag/redditclone
91 https://github.com/aa-ag/reformat
92 https://github.com/aa-ag/RESTcountries
93 https://github.com/aa-ag/scraper
94 https://github.com/aa-ag/sec
95 https://github.com/aa-ag/sendemails
96 https://github.com/aa-ag/sentiment
97 https://github.com/aa-ag/signin_final
98 https://github.com/aa-ag/simple-rss-reader
99 https://github.com/aa-ag/slacknot
100 https://github.com/aa-ag/sms
101 https://github.com/aa-ag/sounds
102 https://github.com/aa-ag/spellcheck
103 https://github.com/aa-ag/strongpassword
104 https://github.com/aa-ag/tictactoe
105 https://github.com/aa-ag/todoapp
106 https://github.com/aa-ag/tracephonenumber
107 https://github.com/aa-ag/transcripts
108 https://github.com/aa-ag/udacity
109 https://github.com/aa-ag/uniqueemails
110 https://github.com/aa-ag/urlshortener
111 https://github.com/aa-ag/validurl
112 https://github.com/aa-ag/venmolikeapi
113 https://github.com/aa-ag/viewsbot
114 https://github.com/aa-ag/w2d1py1-3jn
115 https://github.com/aa-ag/w2d2py1-2jn
116 https://github.com/aa-ag/w2d3py1-2jn
117 https://github.com/aa-ag/w2d4py1-2jn
118 https://github.com/aa-ag/w3_1n3_jn
119 https://github.com/aa-ag/w3_d4_regex-project_jn
120 https://github.com/aa-ag/w3_e1-2_jn
121 https://github.com/aa-ag/w3_e1-5_jn
122 https://github.com/aa-ag/w4d2_SQLhomework
123 https://github.com/aa-ag/W4D4_Joins-NestedQueries
124 https://github.com/aa-ag/w4d5_cardealership
125 https://github.com/aa-ag/w5d1_homework
126 https://github.com/aa-ag/w6d1-js
127 https://github.com/aa-ag/w6d2-js
128 https://github.com/aa-ag/w8d1_jn
129 https://github.com/aa-ag/w8_d3_jn
130 https://github.com/aa-ag/weatherApp-React
131 https://github.com/aa-ag/website
132 https://github.com/aa-ag/websiteblocker
133 https://github.com/aa-ag/Week5
134 https://github.com/aa-ag/whatsapp
135 https://github.com/aa-ag/whoisonwifi
136 https://github.com/aa-ag/wifipasswords
137 https://github.com/aa-ag/wifiswitch
138 https://github.com/aa-ag/wordcloud
139 https://github.com/aa-ag/wordcount
140 https://github.com/aa-ag/xmling
141 https://github.com/aa-ag/xmlpar
'''