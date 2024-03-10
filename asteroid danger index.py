import concurrent.futures
import numpy as np
import requests
from datetime import datetime, timedelta
import json
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

from config import api_key


def fetch_data_for_period(start_date, end_date):
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None


def fetch_data_for_days_default_is_month(start_date, days=30):
    end_date = start_date + timedelta(days=days)
    periods = []
    while start_date < end_date:
        period_end = min(start_date + timedelta(days=6), end_date)
        periods.append((start_date.strftime('%Y-%m-%d'), period_end.strftime('%Y-%m-%d')))
        start_date += timedelta(days=7)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(fetch_data_for_period, start, end) for start, end in periods]
        data = [r.result() for r in concurrent.futures.as_completed(results)]

    return data


def process_data(data):
    processed_asteroids = []
    for period_data in data:
        if period_data is None:
            continue
        for date, asteroids in period_data['near_earth_objects'].items():
            for asteroid in asteroids:
                processed_asteroids.append({
                    'id': asteroid['id'],
                    'name': asteroid['name'],
                    'est_diameter_min': asteroid['estimated_diameter']['kilometers']['estimated_diameter_min'],
                    'est_diameter_max': asteroid['estimated_diameter']['kilometers']['estimated_diameter_max'],
                    'miss_distance_km': float(asteroid['close_approach_data'][0]['miss_distance']['kilometers']),
                    'relative_velocity_kmh': float(
                        asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']),
                })
    return processed_asteroids


def calculate_danger_index(asteroids, A=1, B=1, C=1):
    for asteroid in asteroids:
        avg_diameter = (asteroid['est_diameter_min'] + asteroid['est_diameter_max']) / 2
        asteroid['danger_index'] = (A * avg_diameter) + (B * asteroid['relative_velocity_kmh']) * (
                1 / (C * asteroid['miss_distance_km']))
    return asteroids


def plot_danger_index(asteroids, title_suffix=''):
    names = [a['name'] for a in asteroids]
    danger_indexes = [a['danger_index'] for a in asteroids]
    fig, ax = plt.subplots()
    ax.barh(names, danger_indexes)
    ax.set_xlabel('Danger Index')
    ax.set_title(f'Top 50 Asteroid Danger Index - {title_suffix}')
    plt.tight_layout()
    plt.show()


def plot_danger_index(asteroids, title_suffix=''):
    asteroids_sorted = sorted(asteroids, key=lambda x: x['danger_index'], reverse=True)
    names = [a['name'] for a in asteroids_sorted][:50]
    danger_indexes = [a['danger_index'] for a in asteroids_sorted][:50]
    fig, ax = plt.subplots(figsize=(10, 8))
    bars = ax.barh(names, danger_indexes)
    ax.set_xlabel('Danger Index')
    title = 'Top 50 Asteroid Danger Index'
    if title_suffix:
        title += f' - {title_suffix}'
    ax.set_title(title)
    ax.tick_params(axis='y', which='major', labelsize=8)
    plt.tight_layout()
    plt.show()


def perform_statistical_analysis(asteroids):
    est_diameter_min = [a['est_diameter_min'] for a in asteroids]
    est_diameter_max = [a['est_diameter_max'] for a in asteroids]
    miss_distance_km = [a['miss_distance_km'] for a in asteroids]
    relative_velocity_kmh = [a['relative_velocity_kmh'] for a in asteroids]

    print("Average Estimated Minimum Diameter (km):", np.mean(est_diameter_min))
    print("Average Estimated Maximum Diameter (km):", np.mean(est_diameter_max))
    print("Average Miss Distance (km):", np.mean(miss_distance_km))
    print("Average Relative Velocity (km/h):", np.mean(relative_velocity_kmh))


def week_month(WeekOrMonth):
    file_suffix = 'week' if WeekOrMonth == 'week' else 'month'
    days = 7 if WeekOrMonth == 'week' else 30
    start_date = datetime.now() - timedelta(days=days)
    data = fetch_data_for_days_default_is_month(start_date, days)
    processed_asteroids = process_data(data)
    with open(f"asteroids_information_{file_suffix}.json", "w") as outfile:
        json.dump(processed_asteroids, outfile)

    return processed_asteroids


def run_in_parallel():
    with ThreadPoolExecutor() as executor:
        week_future = executor.submit(week_month, 'week')
        month_future = executor.submit(week_month, 'month')
        week_data = week_future.result()
        month_data = month_future.result()

    week_data = calculate_danger_index(week_data)
    month_data = calculate_danger_index(month_data)

    plot_danger_index(week_data, 'Week')
    plt.savefig('danger_index_week.png')
    plt.close()

    plot_danger_index(month_data, 'Month')
    plt.savefig('danger_index_month.png')
    plt.close()

    perform_statistical_analysis(week_data)
    perform_statistical_analysis(month_data)


if __name__ == "__main__":
    run_in_parallel()

