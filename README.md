# Hava Durumu Uygulaması — Flask

OpenWeatherMap API'den gerçek zamanlı hava durumu verisi alan modern bir Flask tabanlı hava durumu uygulaması.

## Özellikler

- 🌡️ **Gerçek Zamanlı Hava Durumu**: Herhangi bir şehir için anlık hava durumunu öğren
- 📅 **Günlük ve Haftalık Tahmin**: Günlük hava durumu veya 5 günlük tahmin görüntüle
- 🎨 **Modern Arayüz**: Temiz ve responsive tasarım
- ⚡ **Hızlı ve Hafif**: Flask ve vanilla JavaScript ile yapılmış
- 🛡️ **Hata Yönetimi**: Kullanıcı dostu hata mesajları
- 🔍 **Otomatik Tamamlama**: Şehir adını yazarken öneriler göster

## Kurulum

### Gereksinimler
- Python 3.8+
- pip

### Adım Adım Kurulum

1. Repoyu klonla:
```bash
git clone https://github.com/3mr3x/weather-app-flask.git
cd weather-app-flask
```

2. Sanal ortam oluştur:
```bash
python -m venv venv
source venv/bin/activate  # Windows'ta: venv\Scripts\activate
```

3. Bağımlılıkları yükle:
```bash
pip install -r requirements.txt
```

## API Anahtarı Kurulumu

Uygulamayı kullanabilmek için OpenWeatherMap API anahtarına ihtiyacın var:

### API Anahtarı Nasıl Alınır:

1. **OpenWeatherMap Sitesini Ziyaret Et**: [https://openweathermap.org/api](https://openweathermap.org/api)

2. **Hesap Oluştur**: [https://openweathermap.org/api](https://openweathermap.org/api) adresine git
   - "Sign Up" butonuna tıkla
   - Bilgilerini doldur
   - E-posta adresini doğrula

3. **API Anahtarını Al**:
   - Giriş yap
   - Hesap sayfasına git
   - "API keys" sekmesine tıkla
   - **Default API key** alanından anahtarını kopyala

4. **weather.py'ye Anahtarı Ekle**:
   - `weather.py` dosyasını aç
   - `API_KEY = 'XXXXXXXXX'` satırını bul
   - `'XXXXXXXXX'` yerine API anahtarını yapıştır:
   ```python
   API_KEY = 'senin_api_anahtarin_burada'
   ```

### Örnek:
```python
# Öncesi:
API_KEY = 'XXXXXXXXX'

# Sonrası (gerçek anahtarınla):
API_KEY = '1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p'
```

> ⚠️ **Önemli**: API anahtarını hiç kimseyle paylaşma! Eğer bu projeyi açık repositoryse paylaş, `weather.py` dosyasını `.gitignore` dosyasına ekle.

## Kullanım

Uygulamayı başlat:
```bash
python weather.py
```

Tarayıcını aç ve şu adrese git:
```
http://localhost:5000
```

### Örnek Aramalar:
- "London" şehrini ara ve "Günlük Tahmin" seç
- "New York" şehrini ara ve "Haftalık Tahmin (5 Gün)" seç
- Dünyadaki herhangi bir şehri dene!

## Proje Yapısı

```
weather-app-flask/
├── weather.py              # Ana Flask uygulaması
├── requirements.txt        # Python bağımlılıkları
├── templates/
│   ├── home.html          # Ana sayfa / arama sayfası
│   ├── index.html         # Hava durumu sonuçları sayfası
│   ├── weather.html       # Detaylı hava durumu gösterimi
│   └── simple_error.html  # Hata sayfası
└── static/
    └── style.css          # CSS stilleri
```

## API Uç Noktaları

### GET `/`
Ana sayfayı göster (arama formu).

### GET `/forecast?city=<şehir>&period=<dönem>`
Hava durumu tahmini getir.

**Parametreler:**
- `city` (zorunlu): Şehir adı (örn: "London", "İstanbul", "Tokyo")
- `period` (zorunlu): 'daily' (günlük) veya 'weekly' (haftalık)

**Örnek URL'ler:**
- `http://localhost:5000/forecast?city=London&period=daily`
- `http://localhost:5000/forecast?city=Istanbul&period=weekly`

**Yanıt**: Hava durumu verileri ile render edilmiş sayfa

## Hata Yönetimi

Uygulama şu hatalarla ilgilenir:
- **400**: Yanlış İstek (eksik parametreler)
- **404**: Şehir bulunamadı
- **500**: İç sunucu hatası

Tüm hatalar kullanıcı dostu mesajlar ile birlikte gösterilir.

## Teknolojiler

- **Backend**: Flask 3.0.0
- **API**: OpenWeatherMap
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **HTTP İstemcisi**: requests
- **Dağıtım**: Heroku, PythonAnywhere, vb. ile uyumlu

## Sorun Giderme

### Sorun: "Şehir bulunamadı" hatası
- `weather.py` dosyasında geçerli bir API anahtarına sahip olduğundan emin ol
- Şehir adının doğru yazıldığını kontrol et
- Şehrin İngilizce adını kullan

### Sorun: "Geçersiz API anahtarı" veya API hatası
- `weather.py` dosyasındaki API anahtarının doğru olduğunu doğrula
- OpenWeatherMap hesabının aktif olduğundan emin ol
- Free tier planının aktif olduğundan emin ol

### Sorun: Uygulama başlamıyor
- Tüm bağımlılıkların yüklenmiş olduğundan emin ol: `pip install -r requirements.txt`
- Python sürümünü kontrol et (3.8+ gerekli)
- Port 5000'in başka bir uygulama tarafından kullanılmadığını kontrol et

## Özellikleri Detaylı

### Otomatik Tamamlama
- Şehir adını yazarken 50+ popüler şehirden öneriler al
- ⌨️ Ok tuşları ile navigasyon yap
- Enter ile seç, Escape ile iptal et

### Responsive Tasarım
- 📱 Mobil cihazlarda mükemmel görünüm
- 💻 Desktop'ta tam genişlikte
- 🎨 Tüm tarayıcılarda uyumlu

### Modern Arayüz
- Gradient arka plan
- Smooth animasyonlar
- Hover efektleri
- Professional renkler

## Lisans

MIT Lisansı — Bu projeyi istediğin gibi kullanabilirsin.

## Katkıda Bulun

Bir hata buldun mu veya iyileştirme önerio mu var? Pull request açmaktan çekinme!

---

**Yazar**: 3mr3x  
**Son Güncelleme**: Aralık 2025
