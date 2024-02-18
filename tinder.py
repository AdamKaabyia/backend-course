'''
We will simulate a dating app.
● create 4 users with different data.
● using the input function - create a user with the following
attributes: name, gender, age, profession, favorite tv show,
favorite food.
● create a set of rules for each attribute, which will give ok to the
match (for example: age has to be between 20-30, food has to
be pizza or salad, etc).
● check if the user given profile matches with any of the built in
profiles.
● print the result.
Extra:
● if the users don’t match - ask for the data again.
'''

class Person:
    def __init__(self, name, gender, age, profession, favorite_tv_show, favorite_food):
            self.name=name
            self.gender=gender
            self.age=age
            self.profession= profession
            self.favorite_tv_show=favorite_tv_show
            self.favorite_food=favorite_food

    def compare(self,person1,person2):
            