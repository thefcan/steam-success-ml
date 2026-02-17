import requests
import pandas as pd
import time

def get_top_games(pages=5):
    all_games = []

    for page in range(pages):
        url = f"https://steamspy.com/api.php?request=all&page={page}"
        print(f"page {page} çekiliyor")

        response = requests.get(url)
        data = response.json()

        for appid, game in data.items():
            all_games.append({
                "appid": appid,
                "name": game.get("name"),
                "release_year": game.get("release_year"),
                "owners": game.get("owners"),
                "positive": game.get("positive"),
                "negative": game.get("negative"),
                "average_forever": game.get("average_forever"),
                "median_forever": game.get("median_forever"),
                "price": game.get("price"),
                "genres": game.get("genre")
            })

        time.sleep(1)

    return pd.DataFrame(all_games)


def main():
    print("SteamSpy veri çekiliyor...")
    df = get_top_games(pages=6)   # ~6000 oyun
    df.to_csv("data/raw/raw_games.csv", index=False)
    print("BİTTİ → data/raw/raw_games.csv oluştu")


if __name__ == "__main__":
    main()