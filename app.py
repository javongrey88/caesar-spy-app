from flask import Flask, render_template, request

app = Flask(__name__)

alphabet = list("abcdefghijklmnopqrstuvwxyz")

def caesar_cipher(text, shift, direction="encode"):
    result = ""
    shift = int(shift)

    for char in text.lower():
        if char in alphabet:
            idx = alphabet.index(char)
            if direction == "encode":
                shifted_idx = (idx + shift) % 26
            else:
                shifted_idx = (idx - shift) % 26
            result += alphabet[shifted_idx]
        else:
            result += char  # Keep punctuation, numbers, etc.
    return result

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    original_text = ""
    shift = ""
    action = "encode"

    if request.method == "POST":
        original_text = request.form["message"]
        shift = request.form["shift"]
        action = request.form["action"]
        result = caesar_cipher(original_text, shift, action)

    return render_template("index.html", result=result, original_text=original_text, shift=shift)

if __name__ == "__main__":
    app.run(debug=True)
