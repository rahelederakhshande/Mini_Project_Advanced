import requests


class Music:
    def __init__(self, artistName, trackName, trackPrice, trackViewUrl):
        self.artistName = artistName
        self.trackName = trackName
        self.trackPrice = trackPrice
        self.trackViewUrl = trackViewUrl

    def __str__(self) -> str:
        return f"Artist name: {self.artistName}\nTrack name: {self.trackName}\nTrack price: {self.trackPrice}\ntrack Url: {self.trackViewUrl}" 
        

class Fetcher:

    @staticmethod
    def musicFetcher():
        url = f"https://itunes.apple.com/search?term=radiohead"
        response = requests.get(url)
        if response.status_code == 200:
            music_items = response.json()
        else:
            print("Failed")

        music_items = music_items['results']
        music_list = []

        for item in music_items:
            music_obj = Music(
                item.get('artistName', 'Fail'),
                item.get('trackName', 'Fail'),
                item.get('trackPrice','Fail'),
                item.get('trackViewUrl','Fail')
            )
            music_list.append(music_obj)
        return music_list
    

if __name__ == "__main__":
    music_fetcher = Fetcher()
    res = music_fetcher.musicFetcher()
    for music in res:
        print(music)
        print('*' * 10 + '-----' + '*' * 10)

