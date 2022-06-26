import random
#from words import words

words = ["Programming", "Python", "Future", "Programmer", "Coding", "Computer"]

def get_word():
    words = ["Programming", "Python", "Future", "Programmer", "Coding", "Computer"]
    word = random.choice(words)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("\n")
    print(word_completion)
    print(display_jumper(tries))
    print("\n")
    print("^^^^^^^")
    while not guessed and tries > 0:
        guess = input("Guess a letter [a-z]: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("\n")
        print(word_completion)
        print(display_jumper(tries))
        print("^^^^^^^")


def display_jumper(tries):
    stages = [  
    """              



 
   x
  /|\
  / \



                """,
                
                """



 \   /
   0
  /|\
  / \



                """,
                
                """


\     / 
 \   /
   0
  /|\
  / \



                """,
                
                """
  
   _ 
\     / 
 \   /
   0
  /|\
  / \


                """,
               
                """
  
 _____
\     / 
 \   /
   0
  /|\
  / \


                """,
               
                """
  
/_____\
\     / 
 \   /
   0
  /|\
  / \


                """
                    ,
                """
  ___
/ ___ \
\     / 
 \   /
   0
  /|\
  / \

    
                """
                           
                            
                            ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Would you like to play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
