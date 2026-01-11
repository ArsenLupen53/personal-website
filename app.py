from flask import Flask,render_template, request,flash,redirect,url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = "çok_gizli_bir_anahtar" #Flash mesajlar için bu şarttır

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
        gonderen = request.form.get('isim')
        mesaj = request.form.get('mesaj')
        
        # Gerçek bir uygulamada burada veritabanına kayıt yapılır
        print(f"Mesaj: {gonderen} - {mesaj}")
        
        # Kullanıcıya mesaj gönderildiğini bildir
        flash(f"Teşekkürler {gonderen}, mesajın başarıyla alındı!")
        return redirect(url_for('iletisim')) # Sayfayı yeniler ve formu temizler
    
    return render_template("iletisim.html")

if __name__ == '__main__':
    app.run(debug=True, port=8080)
