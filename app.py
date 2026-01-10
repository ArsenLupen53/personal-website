from flask import Flask,render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')

def ana_sayfa():
    kullanici_adi = "Ahmet Berk"
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template("index.html",isim=kullanici_adi,zaman=zaman,tarih=zaman)


if __name__ == '__main__':
    app.run(debug=True)