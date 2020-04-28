import random

def random_token(token_length):
    x = 0
    token = []
    while x < token_length:
        token.append(str(random.randrange(0,9)))
        x+=1
        
    return token