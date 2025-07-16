# Flask ile Nesne Tanıma Uygulaması

Bu proje, Flask tabanlı bir web uygulaması kullanarak görüntüleri sınıflandıran bir **derin öğrenme modeli** içerir. Model, kullanıcı tarafından yüklenen görselleri analiz eder ve en yakın sınıf tahminini yapar.

---

## 🚀 Kurulum ve Çalıştırma

### **1️⃣ Projeyi Klonlayın**
Öncelikle terminal veya komut istemcisini açın ve projeyi yerel makinenize indirin:

```bash
git clone <https://github.com/bektas-sari/nesne-tanima>
cd nesne-tanima
```

---

### **2️⃣ Sanal Ortam (Virtual Environment) Oluşturun**
Python bağımlılıklarını izole etmek için bir sanal ortam oluşturup etkinleştirin:

Windows için:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux için:
```bash
python -m venv venv
source venv/bin/activate
```

---

### **3️⃣ Gerekli Kütüphaneleri Yükleyin**
Bağımlılıkları `requirements.txt` dosyasından yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
```

Bu işlem **Flask**, **TensorFlow**, **NumPy** ve diğer gerekli kütüphaneleri yükleyecektir.

---

### **4️⃣ Model Dosyasını Kontrol Edin**
Google Colab’de eğitilmiş olan modeli proje klasörüne koyduğunuzdan emin olun:

```
product_verification/
│── app.py            # Flask uygulaması
│── product_verification_model.h5  # Model dosyası
│── static/           # CSS, JS ve görseller için
│── templates/        # HTML sayfaları
│── templates/index.html  # Kullanıcı arayüzü
```

Eğer model dosyanız eksikse, Google Colab üzerinden eğitip **`product_verification_model.h5`** olarak kaydedin ve proje dizinine taşıyın.

---

### Lisans
MIT Lİsans. 

---

## 👤 Geliştirici

**Bektas Sari**  

Email: bektas.sari@gmail.com  <br>
GitHub: https://github.com/bektas-sari <br>
LinkedIn: www.linkedin.com/in/bektas-sari <br>
Researchgate: https://www.researchgate.net/profile/Bektas-Sari-3 <br>
Academia: https://independent.academia.edu/bektassari <br>
