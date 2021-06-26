############------------ IMPORTS ------------############
import requests
import settings
import subprocess
import json
import csv

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

    n = 1

    dictionary_for_local_copy = dict()

    while page < 3:
        url = f'https://api.github.com/users/aa-ag/repos?page={page}&per_page=100'

        request = requests.get(url, data=github_auth)
        
        request = request.json()

        for repo in request:
            dictionary_for_local_copy[n] = repo['html_url']
            n += 1

        # for repo in request:
        #     save_locally(repo['html_url'])

        page += 1

    local_copy_just_in_case = open('local_copy.csv', 'w')

    writer = csv.writer(local_copy_just_in_case)

    for k, v in dictionary_for_local_copy.items():
        writer.writerow([k, v])


def get_one_object_to_check_keys_and_values():
    '''
     hits endpoint to get all info within repo object
     then creates json output file to make it easier to 
     vizualise entire object
    '''
    global github_auth

    url = 'https://api.github.com/repos/aa-ag/cpython'

    request = requests.get(url, data=github_auth)
        
    request = request.json()

    pretty_printed_formatted_response = open('full_response.json', 'w')
    
    json.dump(request, pretty_printed_formatted_response, indent=4)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    hit_end_point()

    # get_one_object_to_check_keys_and_values()