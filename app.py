from flask import Flask,render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')

def ana_sayfa():
    kullanici_adi = "Ahmet Berk"
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template("index.html",isim=kullanici_adi,zaman=zaman,tarih=zaman)

@app.route('/hakkimda')
def hakkimda():
    return render_template("hakkimda.html")

if __name__ == '__main__':
    app.run(debug=True, port=8080)

@app.route('/iletisim', methods=['GET', 'POST'])
def iletisim():
    if request.method == 'POST':
        # Formdan gelen verileri alıyoruz
        gonderen = request.form.get('isim')
        mesaj = request.form.get('mesaj')
        
        # Şimdilik sadece terminale yazdıralım (Veritabanı yerine)
        print(f"YENİ MESAJ! Gönderen: {gonderen}, Mesaj: {mesaj}")
        
        return f"<h1>Teşekkürler {gonderen}! Mesajın başarıyla alındı.</h1><a href='/'>Geri Dön</a>"
    
    return render_template("iletisim.html")