from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.reddit.com/r/programming/"
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, "html.parser")


titulo = soup.find_all('shreddit-post')[0]['post-title']
link = soup.find_all('shreddit-post')[0]['content-href']
upvotes = soup.find_all('shreddit-post')[0]['score']

dados_reddit = [
    {"titulo": soup.find_all('shreddit-post')[0]['post-title'], "link": soup.find_all('shreddit-post')[0]['content-href'], "upvotes": soup.find_all('shreddit-post')[0]['score']},
    {"titulo": soup.find_all('shreddit-post')[1]['post-title'], "link": soup.find_all('shreddit-post')[1]['content-href'], "upvotes": soup.find_all('shreddit-post')[1]['score']},
    {"titulo": soup.find_all('shreddit-post')[2]['post-title'], "link": soup.find_all('shreddit-post')[2]['content-href'], "upvotes": soup.find_all('shreddit-post')[2]['score']}
]
df = pd.DataFrame.from_dict(dados_reddit)
df.to_csv('dados_reddit.csv', index=False)

print(df)