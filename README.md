🖼️ Stegno Encoder – Image-Based Steganography (LSB Method)

Stegno Encoder is a simple Python tool that hides secret text inside an image using the Least Significant Bit (LSB) steganography technique. The encoded image looks identical to the original, making the hidden data secure and undetectable to the human eye.

🚀 Features

Hide text messages inside PNG images

Uses LSB (Least Significant Bit) encoding

Maintains image quality and structure

Simple modular Python implementation

Clear user instructions and error handling

📁 Project Structure
stegno-encoder/
│── encoder.py
│── sample.png
│── README.md

🧠 How It Works

Each pixel in an image contains RGB values.

LSB steganography modifies the last bit of the red channel to store message bits.

Text → Binary → Embedded into image pixels.

A delimiter (###) is added to mark message ending.

▶️ Usage
1. Install dependencies
pip install pillow

2. Run the encoder script
python encoder.py

3. Code Example
encode_image("sample.png", "your secret message", "output.png")


The encoded image will be saved as output.png, visually identical to the original.
