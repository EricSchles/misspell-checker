"""
Mis-spell-checker:
1) different difficulty settings:low medium and high
2) misspells between 40-60% of the words you write
"""
import sys
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
        

            
