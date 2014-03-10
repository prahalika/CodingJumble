'''
Can you create a program to solve a word jumble? (More info here.)
The program should accept a string as input, and then return a list of words
that can be created using the submitted letters.  For example, on the input
"dog", the program should return a set of words including "god", "do", and "go".

Please implement the program in Python but refrain from using any helper
modules or imports (e.g. itertools). In order to verify your words, just
download an English word list (here are a few).

Then uplaod your program to GitHub or Gist, and send it back!

Assumptions I am following:
- Can NOT use any imported libraries/modules
- Can use built-in python data structures (lists, dicts, tuples) and functions (strip())
- Allow input string to contain any of the 256 extended ASCII chart characters
- Whitespace at the beginning and end of the input string will be ignored
- Whitespace that's not at the beginning or end of the input string (between the 
  other characters) will not be ignored and will be used towards character limits 
  when comparing with the reference list of words
Created on Mar 10, 2014
@author: Prahalika
'''

'''
Print out the list of words that can be made from the input string
and are legitimate words, as compared to the reference list of words
'''
def print_output(output_list):
    for word in output_list:
        print(word)

'''
Iterate through the list of words in the reference list.
For each word, iterate through each letter and compare with the dict 
created in parse_input_word(). If the letter in the reference word
doesn't appear in the input string dict or if the number of times
that character appears in the reference word exceeds the number of 
times that character appears in the input string, that reference word
cannot be created from the input string. At that point, move on to
checking the next word.
If all of the letters in the reference word appear with appropriate 
counts in the input string, the reference word is a valid creation
using the input string letters. Save that word to an output list. 
'''
def check_words(input_dict, file_path):
    output_list = []
    try:
        word_list = open(file_path)
    except IOError as err:
        print('File error: ' + str(err))
        return list()
    
    for word in word_list:
        clean_word = word.strip()
        word_dict = {}
        let_cnt = 0
    
        for let in clean_word:
            if let not in input_dict:
                break
        
            if let not in word_dict:
                word_dict[let] = 1
            else:
                word_dict[let] += 1
                if word_dict[let] > input_dict[let]:
                    break
            let_cnt += 1
    
        if let_cnt == len(clean_word):
            output_list.append(clean_word)
            
    return output_list

'''
Go through the input string and determine how many of each character
are present. Save that information to a dict where the key is the character
and the value is the count of appearance of that character. 
'''
def parse_input_word(input_word):
    input_dict = {}
    for let in input_word:
        if let not in input_dict:
            input_dict[let] = 1
        else:
            input_dict[let] += 1
    return input_dict

'''
Ask the user to input the string and path to the reference list
and save that information
'''
def get_input():
    input_word = input("Enter input word: ")
    file_path = input("Enter path to reference list: ")
    return (input_word, file_path)

'''
Start the program here.
Retrieve the input from the user
Parse the inputted string to create a character histogram
Read in the reference list of words and compare with the 
character histogram
Output the list of valid words
'''
def main():
    (input_word, file_path) = get_input()
    input_dict = parse_input_word(input_word)
    output_list = check_words(input_dict, file_path)
    print_output(output_list)

if __name__ == "__main__":
    main()