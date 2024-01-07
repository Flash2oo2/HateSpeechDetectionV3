from flask import Flask, render_template, request, jsonify
from utils import model_predict

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    txt_msg = request.form.get("content")
    prediction = model_predict(txt_msg)
    return render_template("index.html", prediction=prediction, txt_msg=txt_msg)


# Create an API endpoint
@app.route("/api/predict", methods=["POST"])
def predict_api():
    data = request.get_json(force=True)  # Get data posted as a json
    txt_msg = data["content"]
    prediction = model_predict(txt_msg)
    return jsonify({"prediction": prediction, "txt_msg": txt_msg})  # Return prediction


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
