import random
import sys

def rearrange(user_input):
    """
    Returns randomly rearranged words taken from the command line
    """
    # Fisher-Yates shuffle
    for indx in range(len(user_input)-1, 0, -1):
        rand_indx = random.randint(0, indx)
        # swapping
        user_input[indx], user_input[rand_indx] = user_input[rand_indx], user_input[indx]
    print(user_input)



if __name__ == '__main__':
    user_input = sys.argv[1:]
    rearrange(user_input)
