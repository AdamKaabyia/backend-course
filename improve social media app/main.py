from social_media import *
from improved_social_media import *
def main():
    platform = SocialMediaPlatform()

    # Test cycle: register users, post messages, follow users, and generate timelines
    for i in range(1, 4):  # Simulating three users for simplicity
        username = f"user{i}"
        platform.register_user(username)
        user = platform.get_user_by_username(username)
        user.post_message(f"Hello from {username}!")

    # User1 follows User2 and User3
    platform.get_user_by_username("user1").follow(platform.get_user_by_username("user2"))
    platform.get_user_by_username("user1").follow(platform.get_user_by_username("user3"))

    # Generating and printing timelines for each user
    for i in range(1, 4):
        username = f"user{i}"
        timeline = platform.generate_timeline(username)
        print(f"Timeline for {username}: {timeline}")


if __name__ == "__main__":
    main()