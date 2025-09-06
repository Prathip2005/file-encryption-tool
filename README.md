🔐 File Encryption & Decryption Tool

A simple Python-based GUI tool for encrypting and decrypting files using the AES (Fernet) algorithm. This project ensures secure file handling and helps protect sensitive data from unauthorized access.

🚀 Features

Encrypt any file (text, PDF, image, etc.)

Decrypt files back to their original form

User-friendly Tkinter GUI

Secret key automatically generated and stored securely

Error handling for invalid files or wrong keys

🛠️ Tech Stack

Python 3.x

Tkinter – GUI framework

cryptography (Fernet AES) – Encryption library

📂 Project Structure
📁 file-encryption-tool
 ┣ 📜 mini.py            # Main program
 ┣ 📜 secret.key         # Auto-generated encryption key (keep safe!)
 ┣ 📜 README.md          # Project documentation
 ┗ 📜 requirements.txt   # Required Python libraries

⚙️ Installation

Install dependencies:

pip install cryptography
Run the program:
python mini.py

🎮 Usage

Open the tool (mini.py).

Click Choose File → Select a file from your computer.

Click Encrypt File → An encrypted .enc file is created.

To decrypt, select the .enc file and click Decrypt File.

Decrypted files will have _decrypted added to their names.

🔮 Future Enhancements

Password-based encryption (instead of auto key).

Support for multiple algorithms (AES, RSA, Blowfish).

File/folder drag & drop support.

Cloud integration for encrypted storage.

👨‍💻 Author

Developed by Your Name
📧 Email: prathipsiva55@gamil.com

🔗 LinkedIn https://www.linkedin.com/in/prathips/

