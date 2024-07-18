from bs4 import BeautifulSoup
import requests

content = BeautifulSoup(requests.get("https://news.ycombinator.com/news").text, "html.parser")

article_title = [tag.text for tag in content.select("span.titleline a")[0::2]]
article_link = [tag["href"] for tag in content.select("span.titleline a")[0::2]]
article_votes = [int(vote.text.split()[0]) for vote in content.select("span.subline span.score")]

top_article = article_title[article_votes.index(max(article_votes))]
top_link = article_link[article_votes.index(max(article_votes))]

top_news = f"Top article for today at {max(article_votes)} votes!!! \nRead {top_article} at {top_link}"
print(top_news)
