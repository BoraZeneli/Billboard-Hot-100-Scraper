## Billboard Hot 100 Scraper

# Objective
Scrape the Billboard Hot 100 chart for a specific date and generate a text file called songs.txt that lists the top 100 song titles in ascending order (starting from 1).

The result should look something like this:

1) Song Title 1
2) Song Title 2
3) Song Title 3
... and so on
The central idea behind this project is to be able to use BeautifulSoup to obtain data—like song titles—from a website like Billboard's. The script allows you to select a specific date to retrieve the top songs from that time.

# ⚠️ Important: Use the Billboard Hot 100 Archive Link
Since websites can change frequently, you should use the following structure to ensure your code works correctly:

URL = "https://www.billboard.com/charts/hot-100/" + date
Where date is the date you want to travel to in the format YYYY-MM-DD.

# Solution
You can find the code in the repository. Run the script, enter the desired date, and it will generate the songs.txt file containing the top 100 songs for that date. Each song will be listed with its corresponding rank.
