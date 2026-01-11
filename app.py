from flask import Flask,render_template, request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "çok_gizli_bir_anahtar" #Flash mesajlar için bu şarttır

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mesajlar.db'
db = SQLAlchemy(app)

# Veritabanı Tablosu (Modeli) - Doğru Hali
class Mesaj(db.Model):
    id = db.Column(db.Integer, primary_key=True) # db.Model.Integer değil db.Integer
    isim = db.Column(db.String(100), nullable=False) # db.Model.String değil db.String
    icerik = db.Column(db.Text, nullable=False)
    tarih = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


@app.route('/')

def ana_sayfa():
    kullanici_adi = "Ahmet Berk"
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template("index.html",isim=kullanici_adi,zaman=zaman,tarih=zaman)

@app.route('/hakkimda')
def hakkimda():
    return render_template("hakkimda.html")


@app.route('/iletisim', methods=['GET', 'POST'])
def iletisim():
    if request.method == 'POST':
        gonderen_ismi = request.form.get('isim')
        mesaj_icerigi = request.form.get('mesaj')
        
        # Veritabanına yeni mesaj ekleme
        yeni_mesaj = Mesaj(isim=gonderen_ismi, icerik=mesaj_icerigi)
        db.session.add(yeni_mesaj)
        db.session.commit()
        
        flash(f"Teşekkürler {gonderen_ismi}, mesajın veritabanına kaydedildi!")
        return redirect(url_for('iletisim'))
    
    return render_template("iletisim.html")


@app.route("/mesajlar")
def mesajlari_listele():
    tum_mesajlar = Mesaj.query.all() # Veritabanındaki tüm mesajları çek
    return render_template("mesajlar.html", mesajlar=tum_mesajlar)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
