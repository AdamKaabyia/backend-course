"""
        create 4 users - V
        create a user from input -V
        take the data of the user in input function -V
        create a set of rules for matching -V
        check if the user matches any of the previous users -V
"""


def number_of_matching_letters(string1, string2):
    count = 0
    for x in string1:
        for y in string2:
            count += 1
    return count


# incomplete
def ages_match(person1, person2):
    return int(person1.min_age) <= int(person2.age) <= int(person1.max_age) and int(person2.min_age) <= int(
        person1.age) <= int(person2.max_age)

def reverse_lookup(d, v):
    for k in d:
        if v in d[k] :
            return k


# i wanna return a compatibility integer such that the more they have in common the higher the score
shows_ganra = {
    "drama": ["breaking bad", "black mirror"],
    "comedy": ["The Umbrella Academy", "better call saul"]
}

def tvshow_compatability(show1, show2):
    return 10 * (reverse_lookup(shows_ganra,show2) == reverse_lookup(shows_ganra,show1))


class Person:
    def __init__(self, name, gender, age, min_age, max_age, profession, favorite_tv_show, favorite_food):
        self.name = name
        self.gender = gender
        self.age = age
        self.min_age = min_age
        self.max_age = max_age
        self.profession = profession
        self.favorite_tv_show = favorite_tv_show
        self.favorite_food = favorite_food


def compatability(person1, person2):
    # i want to see how much letters they have in common in their names
    total = number_of_matching_letters(person2.name, person1.name)
    # age preferences match
    total += ages_match(person1, person2)
    # if in they shows like the same ganra
    total += tvshow_compatability(person1.favorite_tv_show, person2.favorite_tv_show)
    return total


def get_new_user():
    return Person(input("please enter name:"),
                  input("please enter gender:"),
                  input("please enter age:"),
                  input("please enter minimal age preferences:"),
                  input("please enter maximum age preferences:"),
                  input("please enter profession:"),
                  input("please enter favorite tv show:"),
                  input("please enter favorite food:"))


arr = [Person("jakob", "M", 30, 20, 30, "race car driver", "breaking bad", "pasta"),
       Person("jim", "M", 20, 18, 25, "engineer", "black mirror", "pizza"),
       Person("nikita", "F", 24, 25, 32, "engineer", "better call saul", "shrimp"),
       Person("Amelia", "F", 37, 30, 40, "chef", "The Umbrella Academy", "tuna")]

USER = get_new_user()
threshold=compatability(USER,arr[0])
best_fit=arr[0]
for x in arr:
    if compatability(USER, x)>threshold:
        best_fit=x


print(USER.name + "is compatable with: "+best_fit.name+" by "+str(compatability(USER, best_fit)))
