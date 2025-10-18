# Prompt Immagini - La Consegna del Formaggio

Questo file documenta tutti i prompt utilizzati per generare le immagini dell'avventura con Magic Hour AI.

## Immagini Generate

### 1. Copertina - Negozio di Formaggi
**File:** `copertina_negozio_formaggi.png`  
**Prompt (EN):** 
```
A cozy cheese shop in a medieval fantasy village, warm atmosphere, wooden shelves filled with wheels of cheese, D&D illustration style, fantasy art
```
**Scopo:** Immagine di copertina dell'avventura, mostra l'ambientazione iniziale della Casera di Elsa

---

### 2. Scena 2 - Villaggio di Phandalin  
**File:** `scena_1_phandalin.png`  
**Prompt (EN):**
```
Medieval fantasy village of Phandalin at morning, cobblestone streets, small wooden houses, peaceful atmosphere, D&D illustration style, fantasy town setting
```
**Scopo:** Rappresenta il villaggio di Phandalin durante la partenza dei PG

---

### 3. Scena 3 - Carro Rovesciato
**File:** `scena_3_carro_rovesciato.png`  
**Prompt (EN):**
```
Overturned wooden cart on forest road, scattered cheese wheels on ground, broken crates, mysterious small footprints, D&D adventure scene, fantasy illustration, afternoon forest light
```
**Scopo:** Mostra la scena dell'investigazione con il carro assaltato dai kobold

---

### 4. Scena 4 - Tana dei Kobold
**File:** `scena_4_tana_kobold.png`  
**Prompt (EN):**
```
Dark cave entrance in rocky outcrop, mysterious opening between rocks, forest setting, ominous atmosphere, D&D dungeon entrance, fantasy illustration, shadowy and foreboding
```
**Scopo:** Rappresenta l'ingresso della grotta dove si nascondono i kobold

---

### 5. Scena 5 - Combattimento con i Kobold
**File:** `scena_5_combattimento_kobold.png`  
**Prompt (EN):**
```
Kobolds in dark cave chamber surrounded by cheese wheels, small reptilian creatures arguing over food, torchlight illumination, D&D monster encounter, fantasy battle scene, underground dungeon
```
**Scopo:** Mostra i kobold nella loro tana con i formaggi rubati

---

## Strumento Utilizzato

**Generatore:** Magic Hour AI - DND AI Art Generator  
**Script:** `sources/img/magic_hour_imgen.py`  
**Stile:** Fantasy art, D&D illustration style  
**Orientamento:** Landscape (orizzontale)  

## Comando per Generare

```bash
python sources/img/magic_hour_imgen.py "prompt_in_inglese"
```

## Note

- Tutti i prompt sono stati scritti in inglese per ottenere risultati migliori
- Le immagini sono state generate con lo stile "dnd-ai-art-generator" di Magic Hour
- Ogni immagine è stata rinominata e spostata nella cartella `img/` dell'avventura
- Le immagini sono integrate sia nel file .md che .html per facilitare la stampa

---

**Data creazione:** Ottobre 2025  
**Tool:** Magic Hour AI API v1

