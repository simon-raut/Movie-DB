# Note this project is developed for educational purposes
# We do not mean to harm others right

# ---------------------------LET'S----------BEGIN-------------------------
#------------------------IMPORTING----------MODELS------------------------
try:
  import os
  import time
  import requests
  from bs4 import BeautifulSoup
  import pandas as pd
  from imdb import IMDb
  import sys
  import webbrowser
  import os
except:
  print('Please download requests, webbrowser, IMDbPY, bs4 and pandas module manually')

def movie_details_fetcher():
  print('Fetching movie details please wait for a while. It takes time depending on you specs')
  response = requests.get("https://vidsrc.xyz/movies/latest/page-1.json").json()
  ia = IMDb()
  pages = int(response['pages'])

  imdb_ids = []
  titles = []
  embed_urls = []
  quality = []
  image_urls = []
  release_dates = []
  descriptions = []

  for i in range(1, pages):
    response = requests.get(f'https://vidsrc.xyz/movies/latest/page-{i}.json').json()
    content = response['result']
    for item in content:

      id = item['imdb_id']
      id = list(id)
      id.remove('t')
      id.remove('t')
      id_ignore_tt = ' '
      for numbers in id:
        id_ignore_tt += numbers


      title = item['title']
      totle = title.split()
      r_data = len(totle)
      r_date = totle[r_data - 1]
      titled = title.strip(r_date)

    # Search for a movie by title
      movie_title = id_ignore_tt
      movies = ia.get_movie(movie_title)


# Update movie information to get details
      ia.update(movies)

# Get movie details
      title = movies.get('title')
      year = movies.get('year')
      plot = movies.get('plot outline') or movies.get('plot', [''])[0]
      poster_url = movies.get('full-size cover url')

      image_urls.append(poster_url)
      imdb_ids.append(item['imdb_id'])
      titles.append(titled)
      embed_urls.append(item['embed_url'])
      quality.append(item['quality'])
      release_dates.append(r_date)
      descriptions.append(plot)
    print(f'FETCHED = {i}, TOTAL = {pages}, REMAINING = {pages - i}')
    dataset = {'TITLE': titles,
             'IMDB_ID': imdb_ids,
             "URL": embed_urls,
             'QUALITY': quality,
             'IMAGE_URLS': image_urls,
             'RELEASE_DATES': release_dates}
    df = pd.DataFrame(dataset)
    df.to_csv(f'vidsrc_dataset{i}.csv', index=False)
    try:
      os.remove(f'vidsrc_dataset{i-1}.csv')
    except FileNotFoundError:
      pass
      time.sleep(2)

def social_media():
  print('How do you want to contact us')
  print('==================================')
  print('''
   +=================================+ 
   +                                 +
   +  [1] Facebook  [2] Instagram    +
   +                                 +
   +=================================+
''')
  opt = int(input('Enter either 1 or 2: '))
  if opt == 1:
    url = 'https://www.facebook.com/simonraut69'
    webbrowser.open(url, new=0, autoraise=True)
  elif opt == 2:
    url = 'https://www.instagram.com/simon_69/'
    webbrowser.open(url, new=0, autoraise=True)
  else:
    print('Please type either 1 or 2')

def read_me():
  print('''Dear user this program is developed for educational purposes. \n If anyone have problem with us then they can simply contact us. \n
If in any way we harm your rights then we request the authors to report us we will discontinue this project. \n
NOTE :- This program is for educational purposes. If anyone use this to harm other then respective user will be responsible Thank you''')

def main():
  print('\n===================================================')
  print('[1] Download movie data[73000]     [2] Contact us')
  print('[3] Policy (read before using)     [4] Exit ')
  print('[5] Check our more or updated products')
  print('================================================')
  print('We do not force you but if you want then you can donate us')
  print('BINANCE ID = 553 632 672 ')
  print('You small donation can encourage us to develop more exciting product.')
  print('===================================================')
  option = int(input("Enter option (1 or 2 or 3 or 4 or 5): "))
  if option == 1:
    movie_details_fetcher()
  elif option == 2:
    social_media()
  elif option == 3:
    read_me()
  elif option == 4:
    sys.exit()
  elif option == 5:
    webbrowser.open('https://spexaxsimon.blogspot.com/')
  else:
    print('Please select either 1 or 2 or 3')
    print('================================== \n')
    read_me()

while True:
  main()
