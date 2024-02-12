from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = ["https://pichold.ru/wp-content/uploads/2018/11/c24f98eba82666ae547b138be9933bd1.jpg",
          "https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663579207_43-mykaleidoscope-ru-p-veselie-koshechki-krasivo-46.jpg",
          "https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663579262_51-mykaleidoscope-ru-p-veselie-koshechki-krasivo-54.jpg",
          "https://wallbox.ru/wallpapers/main2/201728/14998384635965b7ffade143.60855190.jpg"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")