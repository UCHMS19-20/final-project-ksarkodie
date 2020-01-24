import random 
import time

# Ask user for name to begin
name = input("Welcome to Footy Frenzy! What is your name, player? ")
# greet player
print(f"What's up {name}? Let's start playing Footy Frenzy!")

# set starting score for player
points = 0

# making a class for the questions 
class q:
    """For describing a question asked to user"""
    def __init__ (self, Question, Answer, AnswerChoices):
        self.question = Question
        self.answer = Answer
        self.answerchoices = AnswerChoices

# all trivia questions, mostly getting harder as user moves on
question1 = q("Who is the only player who can use his/her hands?", "Goalkeeper" , ["Striker", "Defender", "Goalkeeper", "Midfielder"])
question2 = q("How many players are on the field for one team in a game?", "11" , ["10", "3", "9", "11"])
question3 = q("Which player is responsible for scoring goals most of the time?", "Striker" , ["Striker", "Defender", "Winger", "Attacking Midfielder"])
question4 = q("Which country won the 2018 Fifa World Cup?", "France" , ["Croatia", "France", "Belgium", "Germany"])
question5 = q("In addition to the US and Canada, what other country calls the sport 'soccer'?", "Australia" , ["England", "Australia", "India", "Iceland"])
question6 = q("Which country won the 2014 Fifa World Cup?", "Germany" , ["Germany", "Spain", "Greece", "Italy"])
question7 = q("What country is Pele from?", "Brazil" , ["Argentina", "Brazil", "DR Congo", "Mars"])
question8 = q("Which country has won the most world cups in history?", "Brazil" , ["England", "Argentina", "Germany", "Brazil"])
question9 = q("Who is the top scorer for the US Women's National Team?", "Abby Wambach" , ["Abby Wambach", "Hope Solo", "Alex Morgan", "Serena Williams"])
question10 = q("Which country won the 2010 Fifa World Cup?", "Spain" , ["Brazil", "France", "Spain", "Netherlands"])
question11 = q("What country is the sport said to have originated?", "England" , ["England", "Brazil", "Netherlands", "Ghana"])
question12 = q("Who has the most assists in EPL history?", "Ryan Giggs" , ["Kevin De Bruyne", "Paul Scholes", "Ryan Giggs", "Alan Shearer"])
question13 = q("How many times has Lionel Messi won the ballon d'or?", "6" , ["3", "6", "5", "10"])
question14 = q("Who has scored the most goals in English Premier League history?", "Alan Shearer" , ["Wayne Rooney", "Cristiano Ronaldo", "Lionel Messi", "Alan Shearer"])
question15 = q("Who is the top scoring African in English Premier League history?", "Didier Drogba" , ["Didier Drogba", "Yaya Toure", "Samuel Eto'o", "John Smith"])

# need to create list for questions for loops
qs = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15]

for questioni in qs:
  time.sleep(2.0)
  print(f"{questioni.question}")
  time.sleep(4.0)
  print(f"Choices: {questioni.answerchoices}")
  user_answer = input("What is your answer? ")
# ask user the question and display choices, and ask for input

  if user_answer not in questioni.answerchoices:
    input("Please pick one of the answer choices. ")
    # check if user's answer is valid
  elif user_answer == questioni.answer:
    points += 1
    # add point to the player's score if correct
    print("That's correct! Take a point, my friend.")
  else:
    print(f"WRONG! The answer is actually: {questioni.answer}")
    # prints the actual answer 

  print (f"You have {points} points.")
# updates player on their score

  if points == 8:
    print("The Einstein of footy! Congratulations, you have won!")
    keephergoing = input("Would you like to keep going? Enter 'yes' or 'no'. ")
    # allows player to keep going even if they have won already
  else:
    pass
    # this is a check/prompt for if player wins game
    keephergoing = input("Would you like to keep going? Enter 'yes' or 'no'. ")
    # allows player to keep going even if they have won already

  if keephergoing == "yes":
    print("We move!")
    # lets player keep playing
  else:
    print("Thanks for playing Footy Frenzy!")
    break
    # exit