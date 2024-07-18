import random

from flask import Flask

server = Flask(__name__)


def get_random_number():
    number = random.randint(0, 9)
    print(number)
    return str(number)


right_number = get_random_number()


@server.route("/")
def index():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media4.giphy.com/media/"
            "v1.Y2lkPTc5MGI3NjExcDF2bjgyMjlybmRob3hyajl5c3Zsd2N5c"
            "TR2NWlpNHI3Z3N4d2J2eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/0OgdJVNjbcIifqSb7U/giphy.webp'></img>")


@server.route("/<number>")
def path(number):
    if f"{number}" == right_number:
        return ("<h1 style='color: green'>You guessed Right!</h1>"
                "<img src='https://media4.giphy.com/media/YTbZzCkRQCEJa/"
                "200.webp?cid=790b761193y1jcwbbljh91zz2o6i15ae03mx5bej013ba3bk&ep=v1_gifs_trending&rid=200.webp&ct=g'>")
    elif f"{number}" < right_number:
        return ("<h1 style='color: red'>You guessed Wrong!</h1>"
                "<h2>It's too low</h2>"
                "<img src='https://media4.giphy.com/media/PNlNcLUSK5tbE5a973/"
                "200.webp?cid=82a1493bewg8t9yaddkbqiu1ehwcqmjyecj52lplpghomln5&ep=v1_gifs_trending&rid=200.webp&ct=g'>")

    elif f"{number}" > right_number:
        return ("<h1 style='color: blue'>You guessed Wrong!</h1>"
                "<h2>It's too High</h2>"
                "<img src='https://media0.giphy.com/media/"
                "v1.Y2lkPTc5MGI3NjExOTN5MWpjd2JibGpoOTF6ejJvNmkxNWFlMDNteDViZWowMTNiYTNiayZlcD12MV"
                "9naWZzX3RyZW5kaW5nJmN0PWc/IvBc7QKyaGFZdM9GZi/200.webp'>")


if __name__ == "__main__" :
    server.run(debug=True)
