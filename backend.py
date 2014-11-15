"""
Mis-spell-checker:
1) different difficulty settings:low medium and high
2) misspells between 40-60% of the words you write
"""
import sys
import random
class MissSpell:
    def __init__(self,level,percentage=4):
        if percentage in range(4,7):
            self.percentage = percentage
        if level.lower() in ["low","medium","high"]:
            self.level = level.lower()
        else:
            print "level is not properly set, please use low, medium, or high"
            sys.exit(0)

    def checker(self,text):
        if self.level == "low":
            self.low_checker(text)
        elif self.level == "medium":
            self.medium_checker(text)
        elif self.level == "high":
            self.high_checker(text)
        else:
            print "You have some how gotten around setting a level, we cannot proceed without this"
            sys.exit(0)
    def low_checker(self,text):
        words = text.split(' ')
        words_to_misspell = int(len(words)*(.01*self.percentage))
        if words_to_misspell == 0: words_to_misspell = 1
        count = 0
        indexes_used = []
        while count < words_to_misspell:
            index = random.randint(0,len(words)-1)
            indexes_used.append(index)
            if index in indexes_used:
                index = random.randint(0,len(words)-1)
                while index in indexes_used:
                    indexes_used.append(index)
                    index = random.randint(0,len(words)-1)
            word = words[index]
            characters = [x for x in word]
            vowels = [x for x in "aeiou"]
            consonants = [x for x in "bcdfghjklmnpqrstvxzwy"]
            vowel_mapping = {"a":"e",
                             "i":"o",
                             "u":"a",
                             "o":"u",
                             "e":"i"
                             }
            consonants_mapping ={"l":"r",
                                 "t":"v",
                                 "q":"w",
                                 "x":"z",
                                 "b":"r",
                                 "k":"l"
                                 }
            new_word = []
            for ind,letter in enumerate(characters):
                if letter in vowels:
                    new_word.append(vowel_mapping[letter])
                else:
                    if ind%3==0 or ind%4==1:
                    
                    else:
                        new_word.append(letter)
            count += 1

            
