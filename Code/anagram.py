import random

def anagram(user_input):
    
    # for char in range(len(user_input)-1, 0, -1):
    for indx in user_input:

        rand_indx = random.randint(0, indx)
    #     user_input[indx], user_input[rand_indx] = user_input[rand_indx], user_input[indx]
        # print(char)
    print(user_input[rand_indx])



if __name__ == '__main__':
    user_input = input("Insert the first word: ")
    anagram(user_input)
