from bs4 import BeautifulSoup
import requests

# Input for the date
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# HTTP request to get the Billboard page for the given date
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

# Creating a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Selecting all song titles
song_names_spans = soup.select("li ul li h3")  # Make sure this selector is correct
# Extracting the text from all found elements and removing unnecessary spaces
songs = [song.getText().strip() for song in song_names_spans]

# Write the songs to a file called "songs.txt" with the numbering
with open("songs.txt", mode="w", encoding="utf-8") as file:
    for index, song in enumerate(songs, start=1):  # start numbering from 1
        file.write(f"{index}. {song}\n")

