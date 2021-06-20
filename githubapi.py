############------------ IMPORTS ------------############
import requests


############------------ GLOBAL VARIABLE(S) ------------############

############------------ FUNCTION(S) ------------############
def hit_end_point():
    request = requests.get('https://github.com/aa-ag')

    print(request.status_code)
    # 200


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    hit_end_point()