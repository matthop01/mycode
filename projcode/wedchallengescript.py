#!usr/bin/env python3

char_name = input("Which character do you want to know about? (Flash, Batman, Superman) ")
char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence) ")
char_name = char_name.lower()
char_stat = char_stat.lower()

dcstats =  {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

value = dcstats.get[char_name][char_stat]
#value = dcstats.call[char_name][char_stat]  
print(f"{char_name}'s {char_stat} is: {value}") 
