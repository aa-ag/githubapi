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

    subprocess.run(command)


def hit_end_point():
    '''
     imports github auth from settings,
     hits enpoint, creates a json with it, 
     and prettyprints the jston with an 
     indentation of 4 spaces (2 tabs)
    '''
    global github_auth

    page = 1

    # #### check requests status to see if limit was hit
    # url = f'https://api.github.com/users/aa-ag/repos?page{page}per_page=100'

    # request = requests.get(url, data=github_auth)

    # return request.status_code

    ### actual code

    while page < 3:
        url = f'https://api.github.com/users/aa-ag/repos?page{page}per_page=100'

        request = requests.get(url, data=github_auth)

        if request.status_code == 200:
        
            request = request.json()

            # pp = pprint.PrettyPrinter(indent=4)
            # pp.pprint(request)

            n = 1

            for repo in request:
                print(n, repo['html_url'])
                n += 1

        page += 1

        print(f"Something went wrong: {request.status_code}")


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    # hit_end_point()
    # print(hit_end_point()) 
    # 403
    save_locally()