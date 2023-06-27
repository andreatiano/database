import streamlit as st
import sqlite3

# Connessione al database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Creazione della tabella se non esiste già
c.execute('''CREATE TABLE IF NOT EXISTS dati
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              nome TEXT,
              cognome TEXT,
              email TEXT)''')

# Funzione per l'inserimento dei dati nel database
def inserisci_dati(nome, cognome, email):
    c.execute("INSERT INTO dati (nome, cognome, email) VALUES (?, ?, ?)", (nome, cognome, email))
    conn.commit()

# Interfaccia utente con Streamlit
st.title('Inserimento dati nel database')

# Form per l'inserimento dei dati
nome = st.text_input('Nome')
cognome = st.text_input('Cognome')
email = st.text_input('Email')

# Bottone per l'inserimento dei dati
if st.button('Inserisci dati'):
    inserisci_dati(nome, cognome, email)
    st.success('Dati inseriti correttamente nel database!')
