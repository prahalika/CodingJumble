PROMPT:
Can you create a program to solve a word jumble?  (More info here.)  
The program should accept a string as input, and then return a list of words 
that can be created using the submitted letters.  For example, on the input 
"dog", the program should return a set of words including "god", "do", and "go".
 
Please implement the program in Python but refrain from using any helper 
modules or imports (e.g. itertools). In order to verify your words, just 
download an English word list (here are a few).  

Then upload your program to GitHub or Gist, and send it back!

===========================================================================

ASSUMPTIONS I AM FOLLOWING:
- Can NOT use any imported libraries/modules
- Can use built-in python data structures (lists, dicts, tuples) and functions (strip())
- Allow input string to contain any of the 256 extended ASCII chart characters
- Whitespace at the beginning and end of the input string will be ignored
- Whitespace that's not at the beginning or end of the input string (between the 
  other characters) will not be ignored and will be used towards character limits 
  when comparing with the reference list of words

===========================================================================

STRATEGY:

My solution to this problem involves parsing the input string and constructing a histogram of its characters and then checking each word of the reference list to decide if it's possible to create that word from the input string.

When I first read the prompt, my immediate thought was to first generate all the possible permutations of the input string of length 1 to n, where n is the length of the input string. However, I quickly realized this is not the optimal way of approaching this problem, because even with an input string of 10 characters, there are upwards of 3 million possible permutations.
From my findings, I learned that there are only around 1.02 million recognized words in the English language.
Knowing this, I realized that it is a lot more time-efficient to use the input string only to determine how many of each character is present. Then I iterate through the list of reference words (which will be significantly smaller than the possible number of permutations for large input strings). This way, generating the large number of permutations of the input string (most of which are invalid) can be avoided.

I chose this solution because in addition to being more time-efficient, it is also more space-efficient. If I were to generate all the possible permutations of the input string, I would have to store them all in an appropriate structure. And again, given the large number of possible permutations, this would require a lot more memory than is necessary.