class User:

    # Initializes a new user with a username and an empty list of users they're following.
    def __init__(self, username):
        self.username = username
        self.following = []

    # Adds another user to the following list, if not already followed. Time complexity is O(n) due to the search in the list.
    def follow(self, other_user):
        if other_user not in self.following:
            self.following.append(other_user)

    # Appends a new post to the global posts list. Time complexity is O(1) assuming list append operation is constant time.
    def post_message(self, message):
        post = {'username': self.username, 'message': message}
        posts.append(post)


posts = []
