
# pip install pycryptodome  # Pour Crypto.PublicKey et Crypto.Cipher
# pip install cryptography  # Pour cryptography.fernet


import streamlit as st
import sqlite3
from cryptography.fernet import Fernet
from rsa import RSA, PrivateKey, PublicKey
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Connexion à la base de données
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# Fonction pour générer une clé AES
def generate_aes_key():
    return Fernet.generate_key()

# Fonction pour chiffrer un mot de passe avec AES
def encrypt_password_aes(password, key):
    return key.encrypt(password.encode())

# Fonction pour déchiffrer un mot de passe avec AES
def decrypt_password_aes(encrypted_password, key):
    return key.decrypt(encrypted_password).decode()

# Fonction pour générer une clé RSA
def generate_rsa_key():
    return RSA.generate(2048)

# Fonction pour chiffrer un mot de passe avec RSA
def encrypt_password_rsa(password, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(password.encode())

# Fonction pour déchiffrer un mot de passe avec RSA
def decrypt_password_rsa(encrypted_password, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(encrypted_password).decode()

# Fonction pour générer une clé PGP
def generate_pgp_keypair():
    private_key = RSA.generate(2048)
    public_key = private_key.public_key()
    return private_key, public_key

# Fonction pour chiffrer un mot de passe avec PGP
def encrypt_password_pgp(password, public_key):
    cipher = PGP.encrypt(password.encode(), public_key)
    return cipher

# Fonction pour déchiffrer un mot de passe avec PGP
def decrypt_password_pgp(encrypted_password, private_key):
    cipher = PGP.decrypt(encrypted_password, private_key)
    return cipher.decode()

# Fonction pour afficher les résultats
def show_results(algorithm, encrypted_password, decrypted_password):
    st.write("Algorithme :", algorithm)
    st.write("Mot de passe chiffré :", encrypted_password)
    st.write("Mot de passe déchiffré :", decrypted_password)

# Interface utilisateur
st.title("Chiffrement de mot de passe")

# Saisie du mot de passe
password = st.text_input("Mot de passe")

# Choix de l'algorithme
algorithm = st.selectbox("Algorithme", ["AES", "RSA", "PGP"])

# Génération de la clé
if algorithm == "AES":
    key = generate_aes_key()
elif algorithm == "RSA":
    public_key, private_key = generate_rsa_key()
elif algorithm == "PGP":
    private_key, public_key = generate_pgp_keypair()

# Chiffrement du mot de passe
encrypted_password = encrypt_password_aes(password, key) if algorithm == "AES" else encrypt_password_rsa(password, public_key) if algorithm == "RSA" else encrypt_password_pgp(password, public_key)

# Déchiffrement du mot de passe
decrypted_password = decrypt_password_aes(encrypted_password, key) if algorithm == "AES" else decrypt_password_rsa(encrypted_password, private_key) if algorithm == "RSA" else decrypt_password_pgp(encrypted_password, private_key)

# Affichage des résultats
show_results(algorithm, encrypted_password, decrypted_password)

# Enregistrement des données
if st.button("Enregistrer les données"):
    cursor.execute("INSERT INTO passwords (algorithm, encrypted_password, decrypted_password) VALUES (?, ?, ?)", (algorithm, encrypted_password, decrypted_password))
    connection.commit()
