"""
Script per caricare automaticamente le immagini su Imgur
e aggiornare il file Markdown con i link corretti.

Requisiti:
    pip install requests

Uso:
    python upload_immagini_imgur.py
"""

import requests
import os
import re
from pathlib import Path

# CONFIGURAZIONE
CLIENT_ID = "TUA_CLIENT_ID_QUI"  # Ottieni da: https://api.imgur.com/oauth2/addclient
MARKDOWN_FILE = "la_festa_del_raccolto_maledetto.md"
IMG_DIR = "img"

# Immagini da caricare
IMAGES = {
    "PLACEHOLDER.png": "scena_1_gancio_piazza.png",
    "PLACEHOLDER2.png": "scena_3_cantina_allagata.png", 
    "PLACEHOLDER3.png": "antagonista_snik_orecchiatagliata.png"
}

def upload_to_imgur(image_path, client_id):
    """Carica un'immagine su Imgur e restituisce l'URL."""
    
    print(f"Caricando {image_path}...")
    
    url = "https://api.imgur.com/3/image"
    headers = {"Authorization": f"Client-ID {client_id}"}
    
    with open(image_path, 'rb') as f:
        files = {'image': f}
        response = requests.post(url, headers=headers, files=files)
    
    if response.status_code == 200:
        data = response.json()
        link = data['data']['link']
        print(f"✅ Caricata con successo: {link}")
        return link
    else:
        print(f"❌ Errore {response.status_code}: {response.text}")
        return None

def update_markdown(markdown_file, replacements):
    """Aggiorna il file Markdown sostituendo i placeholder con i link reali."""
    
    print(f"\nAggiornando {markdown_file}...")
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for placeholder, real_link in replacements.items():
        pattern = f"https://i.imgur.com/{placeholder}"
        content = content.replace(pattern, real_link)
        print(f"✅ Sostituito {placeholder} con link reale")
    
    with open(markdown_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ File {markdown_file} aggiornato con successo!")

def main():
    print("=" * 60)
    print("UPLOAD AUTOMATICO IMMAGINI SU IMGUR")
    print("=" * 60)
    
    # Verifica CLIENT_ID
    if CLIENT_ID == "TUA_CLIENT_ID_QUI":
        print("\n❌ ERRORE: Devi configurare CLIENT_ID!")
        print("\n📋 Come ottenere CLIENT_ID:")
        print("1. Vai su: https://api.imgur.com/oauth2/addclient")
        print("2. Registra un'applicazione (tipo: OAuth without callback)")
        print("3. Copia il 'Client ID'")
        print("4. Incollalo nella variabile CLIENT_ID in questo script")
        return
    
    # Verifica che le immagini esistano
    img_dir = Path(IMG_DIR)
    if not img_dir.exists():
        print(f"\n❌ ERRORE: Directory {IMG_DIR} non trovata!")
        return
    
    # Upload immagini
    replacements = {}
    
    for placeholder, filename in IMAGES.items():
        img_path = img_dir / filename
        
        if not img_path.exists():
            print(f"⚠️ ATTENZIONE: {img_path} non trovato, salto...")
            continue
        
        imgur_link = upload_to_imgur(img_path, CLIENT_ID)
        
        if imgur_link:
            replacements[placeholder] = imgur_link
    
    if not replacements:
        print("\n❌ Nessuna immagine caricata con successo!")
        return
    
    # Aggiorna Markdown
    update_markdown(MARKDOWN_FILE, replacements)
    
    print("\n" + "=" * 60)
    print("✅ COMPLETATO!")
    print("=" * 60)
    print("\nOra puoi:")
    print("1. Aprire il file Markdown aggiornato")
    print("2. Copiare tutto il contenuto")
    print("3. Incollarlo su https://homebrewery.naturalcrit.com/")
    print("\nLe immagini sono ora ospitate su Imgur e si vedranno correttamente!")

if __name__ == "__main__":
    # Verifica dipendenze
    try:
        import requests
    except ImportError:
        print("❌ ERRORE: Modulo 'requests' non installato!")
        print("\nInstallalo con: pip install requests")
        exit(1)
    
    main()

