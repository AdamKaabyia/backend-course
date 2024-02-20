"""
        create 4 users - V
        create a user from input -V
        take the data of the user in input function -V
        create a set of rules for matching
        check if the user matches any of the previous users
"""
def number_of_matching_letters(string1,string2):
    count=0
    for x in string1:
        for y in string2:
            count+=1
    return count


#incomplete
def ages_match(person1,person2):

class Person:
    def __init__(self, name, gender, age,age_preference, profession, favorite_tv_show, favorite_food):
            self.name=name
            self.gender=gender
            self.age=age
            self.age_preference=age_preference
            self.profession= profession
            self.favorite_tv_show=favorite_tv_show
            self.favorite_food=favorite_food

# i wanna return a compatibility integer such that the more they have in common the higher the score
shows_ganra={
    "drama" : ["breaking bad","black mirror"],
    "comedy":["The Umbrella Academy","better call saul"]
}
def compatability(person1,person2):
    #i wanna see how much letters they have in common in their names
    total=number_of_matching_letters(person2.name,person1.name)
    #age preferences match
    total+=ages_match(person1,person2)
    #if in they shows like the same ganra



def get_new_user():
    return Person(input("please enter name:"),
                  input("please enter gender:"),
                  input("please enter age:"),
                  input("please enter age preferences:"),
                  input("please enter profession:"),
                  input("please enter favorite tv show:"),
                  input("please enter favorite food:"))



jakob = Person("jakob","M",30,[20,30],"race car driver","breaking bad","pasta")
jim = Person("jim","M",20,[18,25],"engineer","black mirror","pizza")
nikita = Person("nikita","F",24,[25,32],"engineer","better call saul","shrimp")
Amelia = Person("Amelia","F",37,[30,40],"chef","The Umbrella Academy","tuna")


