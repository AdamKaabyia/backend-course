import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


def fetch_games_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        games = soup.find_all('div', class_='tab_item_content')
        games_data = []
        for game in games:
            title = game.find('div', class_='tab_item_name').text
            genres = game.find_all('div', class_='tab_item_top_tags')
            if genres:
                genres = genres[0].text.replace(' ', '').split(',')
            else:
                genres = []
            games_data.append({'Title': title, 'Genres': genres})

        return pd.DataFrame(games_data)
    else:
        print(f"Failed to fetch data from {url}")
        return pd.DataFrame()


def plot_genres(data):
    genre_counts = data.explode('Genres')['Genres'].value_counts()
    plt.figure(figsize=(10, 6))
    genre_counts.head(10).plot(kind='bar')
    plt.title('Top 10 Most Common Genres')
    plt.xlabel('Genre')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def get_genre_statistics(data):
    user_genre = input("Enter a genre to see its statistics: ").strip()
    if user_genre:
        genre_counts = data.explode('Genres')['Genres'].value_counts()
        if user_genre in genre_counts.index:
            total_count = genre_counts.sum()
            genre_percentage = (genre_counts[user_genre] / total_count) * 100
            print(f"{user_genre} appears in {genre_percentage:.2f}% of the games list.")
        else:
            print(f"The genre '{user_genre}' was not found in the list.")
    else:
        print("No genre entered.")


if __name__ == '__main__':
    url = "https://store.steampowered.com"
    game_data = fetch_games_data(url)
    if not game_data.empty:
        game_data['Genres'] = game_data['Genres'].apply(lambda x: x if isinstance(x, list) else [])
        print(game_data.head())
        plot_genres(game_data)
        get_genre_statistics(game_data)
    else:
        print("No game data found.")
