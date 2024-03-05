import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


def fetch_games_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(soup)
        games = soup.find_all('div', class_='tab_item_name')
        games_data = []
        for game in games:
            title = game.find('span', class_='top_tag').text
            genres_div = game.find('div', class_='tab_item_name').find_next()
            genres_text = genres_div.text.strip() if genres_div else 'No Genres Found'
            games_data.append({'Title': title, 'Genres': genres_text})

        return pd.DataFrame(games_data)
    else:
        print(f"Failed to fetch data from {url}")
        return pd.DataFrame()

# Function to plot top tags
def plot_top_tags(data):
    tag_counts = data.explode('Tags')['Tags'].value_counts()
    plt.figure(figsize=(10, 6))
    tag_counts.head(10).plot(kind='bar')
    plt.title('Top 10 Most Appeared Tags')
    plt.xlabel('Tags')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to get statistics for a user-specified tag
def get_tag_statistics(data):
    user_tag = input("Enter a tag to see its statistics: ").strip()
    if user_tag:
        tag_counts = data.explode('Tags')['Tags'].value_counts()
        if user_tag in tag_counts:
            total_tags = tag_counts.sum()
            tag_percentage = (tag_counts[user_tag] / total_tags) * 100
            print(f"{user_tag} appears in {tag_percentage:.2f}% of the games list.")
        else:
            print(f"The tag '{user_tag}' was not found in the games list.")
    else:
        print("No tag entered.")

# Main process
if __name__ == '__main__':
    url = "https://store.steampowered.com/search/?filter=topsellers"
    game_data = fetch_games_data(url)
    if not game_data.empty:
        plot_top_tags(game_data)
        get_tag_statistics(game_data)
    else:
        print("No game data was found.")
