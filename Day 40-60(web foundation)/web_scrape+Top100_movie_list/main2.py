from bs4 import BeautifulSoup
import requests

content = BeautifulSoup(requests.get("https://web.archive.org/web/20200518055830/"
                                     "https://www.empireonline.com/movies/features/best-movies-2/").text,
                        "html.parser")

movie_object_list = content.select("div.article-title-description h3")
movielist = [movie_title.text for movie_title in movie_object_list]
movielist.reverse()

modified_movie_list = [movie + "\n" for movie in movielist]

movie_string = "".join(modified_movie_list)

with open('Top100_movielist.txt', "w", encoding='utf-8') as file:
    file.write(movie_string)

