from user import *

class SocialMediaPlatform:
    def __init__(self):
        # Changed to a dictionary for O(1) access by username
        self.users = {}

    def register_user(self, username):
        # Time complexity: O(1) with hash map lookup
        if username not in self.users:
            user = User(username)
            self.users[username] = user

    def get_user_by_username(self, username):
        # Time complexity: O(1) with hash map lookup
        return self.users.get(username, None)

    def generate_timeline(self, username):
        user = self.get_user_by_username(username)
        if not user:
            return []

        timeline = []
        for followed_user in user.following:
            followed_posts = [post for post in posts if post['username'] == followed_user.username]
            timeline.extend(followed_posts)
        return timeline
