############------------ IMPORTS ------------############
import requests
import settings
import subprocess

############------------ GLOBAL VARIABLE(S) ------------############
github_auth = settings.GITHUB_AUTH
destination_path = settings.DESTINATION


############------------ FUNCTION(S) ------------############
def save_locally(repo_being_cloned):
    '''
     helper function to `clone` each repo
     locally to a give path
    '''
    global destination_path

    path_where_repo_will_be_cloned_to = destination_path

    command = ["git", "clone", repo_being_cloned]

    subprocess.run(command, cwd=path_where_repo_will_be_cloned_to)


def hit_end_point():
    '''
     imports github auth from settings,
     hits endpoint, creates a json with it, 
     then saving each locally to given path
    '''
    global github_auth

    page = 1

    while page < 3:
        url = f'https://api.github.com/users/aa-ag/repos?page={page}&per_page=100'

        request = requests.get(url, data=github_auth)
        
        request = request.json()

        for repo in request:
            save_locally(repo['html_url'])

        page += 1


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    hit_end_point()