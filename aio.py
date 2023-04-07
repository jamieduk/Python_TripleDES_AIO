#!/usr/bin/env python3
# (c)J~Net 2023
# jnet.sytes.net
#
# ./aio.py
#
from Crypto.Cipher import DES3
from Crypto import Random
import os

def generate_key():
    key=Random.get_random_bytes(24)
    with open("key.txt", "wb") as key_file:
        key_file.write(key)
    print("🔐 Key Generated Successfully.")

def get_key():
    if not os.path.exists("key.txt"):
        print("Key Not Found. Please Generate A Key First.")
        return
    with open("key.txt", "rb") as key_file:
        key=key_file.read()
    return key

def encrypt_message():
    key=get_key()
    if key is None:
        return
    message_file=input("Enter The Message File To Encrypt (default message.txt): ")
    if message_file == "":
        message_file="message.txt"
    if not os.path.exists(message_file):
        print("Message File Not Found!")
        return
    with open(message_file, "rb") as f:
        message=f.read()
    message_length=len(message)
    padding_length=8 - (message_length % 8)
    padding=bytes([padding_length]) * padding_length
    padded_message=message + padding
    iv=Random.get_random_bytes(8)
    cipher=DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext=cipher.encrypt(padded_message)
    with open("encrypted.txt", "wb") as f:
        f.write(iv)
        f.write(ciphertext)
    print("🔐 Encryption Complete.")


def decrypt_message():
    key=get_key()
    if key is None:
        return
    if not os.path.exists("encrypted.txt"):
        print("Encrypted Message Not Found.")
        return
    with open("encrypted.txt", "rb") as f:
        iv=f.read(8)
        ciphertext=f.read()
    cipher=DES3.new(key, DES3.MODE_CBC, iv)
    plaintext=cipher.decrypt(ciphertext)
    with open("decrypted.txt", "wb") as f:
        f.write(plaintext)
    print("Decryption Complete.")

while True:
    print("==============================")
    print("TripleDES Encryption Menu")
    print("==============================")
    print("1. 🔐 Generate Key")
    print("2. Encrypt Message")
    print("3. Decrypt Message")
    print("4. Exit")
    choice=input("Enter Your Choice (1-4): ")
    if choice == "1":
        generate_key()
    elif choice == "2":
        encrypt_message()
    elif choice == "3":
        decrypt_message()
    elif choice == "4":
        break
    else:
        print("Invalid Choice. Please Enter A Number From 1 to 4.")

