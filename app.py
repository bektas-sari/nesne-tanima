from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Modeli yükle
model = tf.keras.models.load_model("product_verification_model.h5")

# Klasörleri oluştur (Eğer yoksa)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Kullanıcının yüklediği dosyayı al
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            img_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
            uploaded_file.save(img_path)

            # Görseli modele uygun hale getirme
            img = image.load_img(img_path, target_size=(32, 32))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Model tahmini yap
            prediction = model.predict(img_array)
            predicted_class = np.argmax(prediction, axis=1)[0]

            # CIFAR-10 sınıf isimleri
            class_names = ["Uçak", "Araba", "Kuş", "Kedi", "Geyik", "Köpek", "Kurbağa", "At", "Gemi", "Kamyon"]
            predicted_label = class_names[predicted_class]

            return render_template("index.html", uploaded_image=uploaded_file.filename, result=predicted_label)

    return render_template("index.html", uploaded_image=None, result=None)

if __name__ == "__main__":
    app.run(debug=True)
