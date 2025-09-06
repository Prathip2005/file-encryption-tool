import os
from tkinter import Tk, Label, Button, filedialog, Entry, StringVar, messagebox
from cryptography.fernet import Fernet

# -----------------------------
# Generate or load encryption key
# -----------------------------
def generate_key():
    """Generate and save key if not exists"""
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

def load_key():
    """Load the key from secret.key file"""
    return open("secret.key", "rb").read()

# -----------------------------
# Encryption and Decryption
# -----------------------------
def encrypt_file(filename, key):
    cipher = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):
    cipher = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = cipher.decrypt(encrypted_data)
        new_filename = filename.replace(".enc", "_decrypted")
        with open(new_filename, "wb") as file:
            file.write(decrypted_data)
    except Exception as e:
        messagebox.showerror("Error", "Wrong key or corrupted file!")

# -----------------------------
# Tkinter GUI
# -----------------------------
class FileEncryptorApp:
    def __init__(self, master):
        self.master = master
        master.title("File Encryption & Decryption Tool")
        master.geometry("400x250")
        master.resizable(False, False)

        self.filename = None
        self.key = None

        self.label = Label(master, text="Select a file to Encrypt/Decrypt")
        self.label.pack(pady=10)

        self.select_button = Button(master, text="Choose File", command=self.choose_file)
        self.select_button.pack(pady=5)

        self.encrypt_button = Button(master, text="Encrypt File", command=self.encrypt)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = Button(master, text="Decrypt File", command=self.decrypt)
        self.decrypt_button.pack(pady=5)

        self.status = StringVar()
        self.status_label = Label(master, textvariable=self.status, fg="blue")
        self.status_label.pack(pady=10)

    def choose_file(self):
        self.filename = filedialog.askopenfilename()
        if self.filename:
            self.status.set(f"Selected: {os.path.basename(self.filename)}")

    def encrypt(self):
        if not self.filename:
            messagebox.showwarning("Warning", "Please select a file first!")
            return
        generate_key()
        self.key = load_key()
        encrypt_file(self.filename, self.key)
        self.status.set("File Encrypted Successfully!")

    def decrypt(self):
        if not self.filename:
            messagebox.showwarning("Warning", "Please select a file first!")
            return
        if not os.path.exists("secret.key"):
            messagebox.showerror("Error", "No key found! Encrypt a file first.")
            return
        self.key = load_key()
        decrypt_file(self.filename, self.key)
        self.status.set("File Decrypted Successfully!")

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    root = Tk()
    app = FileEncryptorApp(root)
    root.mainloop()
