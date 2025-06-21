from flask import Flask, render_template, request, send_file
from datetime import datetime
import io

app = Flask(__name__)

# Caesar cipher alphabet
alphabet = list("abcdefghijklmnopqrstuvwxyz")

# Caesar cipher encode/decode function
def caesar_cipher(text, direction="encode"):
    shift = 3  # Fixed cipher key
    result = ""

    for char in text.lower():
        if char in alphabet:
            idx = alphabet.index(char)
            if direction == "encode":
                shifted_idx = (idx + shift) % 26
            elif direction == "decode":
                shifted_idx = (idx - shift) % 26
            result += alphabet[shifted_idx]
        else:
            result += char  # Leave punctuation and spaces unchanged
    return result

# Main route for encoding and decoding
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    original_text = ""
    action = ""

    if request.method == "POST":
        action = request.form.get("action", "").strip().lower()

        if action == "encode":
            original_text = request.form.get("encode_input", "")
            result = caesar_cipher(original_text, direction="encode")

        elif action == "decode":
            original_text = request.form.get("decode_input", "")
            result = caesar_cipher(original_text, direction="decode")

        print(f"[DEBUG] ACTION: {action}, TEXT: {original_text}, RESULT: {result}")

    return render_template(
        "index.html",
        result=result,
        original_text=original_text,
        action=action
    )

# File download route for saving messages
@app.route("/save", methods=["POST"])
def save_to_file():
    encoded_message = request.form["encoded_message"]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"encoded_message_{timestamp}.txt"

    # Create file in memory
    file_stream = io.BytesIO()
    file_stream.write(encoded_message.encode("utf-8"))
    file_stream.seek(0)

    return send_file(
        file_stream,
        as_attachment=True,
        download_name=filename,
        mimetype='text/plain'
    )

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)




