# importing necessary modules for the program
import random
import time
import sys
from threading import Timer


# method to calculate the speed
def calculate_speed(sen, initial, final):
    # calculating the total no of words by counting no of spaces in the sentence
    words = sen.count(" ") + 1
    # calculating the time difference
    time_diff = final - initial

    return words / time_diff


# method to calculate the accuracy
def calculate_accuracy(sen, written):
    # check the length of actual and written sentence
    if len(sen) == len(written):
        count = 0

        # loop to iterate over characters of typed and generated
        for i in range(len(sen)):
            # check if both are same or not
            if sen[i] == written[i]:
                count += 1

        return count / len(sen)

    elif len(sen) > len(written):
        print("Please enter the entire sentence \n")
        return 0

    elif len(sen) < len(written):
        print("Looks like you have entered extra text \n")
        return 0


# method for collecting sentences
def collect_sentence():
    # creating list to store the sentences
    sentence_list = []
    # opening the file
    with open("Sentence.txt", 'rt') as my_file:
        for line in my_file:
            # appending sentences to list
            sentence_list.append(line.strip())

    return sentence_list


# interacting with the user
def play_game():
    sentence_list = collect_sentence()
    # generating random number which contains the index
    sentence_index = random.randrange(0, len(sentence_list), 2)

    # storing the random sentence
    sentence = sentence_list[sentence_index]
    # printing the sentence for the user
    print(sentence)

    # take the initial time of typing
    start_time = time.time()
    # take the input from the user
    statement = input()
    # take the ending time of typing
    end_time = time.time()

    if round(calculate_accuracy(sentence, statement) >= 0.9):
        print("Congratulations you are having a good typing skills")
        print("Your accuracy is " + str(round(calculate_accuracy(sentence, statement) * 100, 2)))
        print(str(round(calculate_speed(sentence, start_time, end_time) * 60, 2)) + "words per minute")

    elif round(calculate_accuracy(sentence, statement) < 0.9) and round(calculate_accuracy(sentence, statement) > 0):
        print("Your accuracy is " + str(round(calculate_accuracy(sentence, statement) * 100, 2)))
        print(str(round(calculate_speed(sentence, start_time, end_time) * 60, 2)) + "words per minute")

    else:
        print("Accuracy will only be calculated if length of displayed sentence and typed sentence is same")


while True:
    print("Ready to test your typing speed")
    print("Enter 1 to test \n2 to exit")

    n = input()
    if n.isdigit():
        if 0 > int(n) > 2:
            print("Invalid option")
            sys.exit()

        elif n == '1':
            play_game()

        elif n == '2':
            sys.exit()

        else:
            print("You have selected the invalid option")
            sys.exit()

    else:
        print("You have entered wrong option")
        print("Please try again")