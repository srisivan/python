
import random

print("Hi! What is your name?")
name = raw_input()

print("hi %s! My name is python." % name)

print("So, what would you like to do?")
players_hobbies = raw_input()


hobbies = ['playing','watching tv', 'reading', 'cycling', 'learning bike']
response = random.choice(hobbies)

print("Well, I like %s too. My hobbies are, %s" % (players_hobbies,response))



