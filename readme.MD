# 📚 Selectivity Exam Downloader / Descarregador d'Exàmens de Selectivitat

## 🇪🇸 Català  

### Què és això?  
Una eina que descarrega tots els exàmens de selectivitat per fer-te un dossier amb tots els exàmens junts, així no cal anar imprimint un per un i es pot fer tot en un. Principalment l'he creada per mi ja que en res he de fer aquesta prova i m'anirà bé tenir un recull

### Característiques  
- 📥 Descarrega exàmens del 2019 al 2024  
- 📚 Suporta diverses matèries:  
  - Llengua Catalana i Literatura  
  - Llengua Castellana i Literatura  
  - Història  
  - Història de la Filosofia  
- 📂 Organitza tot per anys  
- 📎 Crea PDFs unificats amb tots els exàmens + solucions  
- 🎯 Es centra en els exàmens de juny (excepte 2020, que usa juliol)  

### Com utilitzar-ho  
1. Instal·la els requisits:  
```bash
pip install requests beautifulsoup4 PyPDF2
```

2. Executa l'script:  
```bash
python examens.py
```

3. A estudiar! (o fer veure que estudies 😉)  

### Com modificar el codi
1. **Canviar els anys**
```python
def create_year_folders(base_path, start_year=2019, end_year=2024):
```

2. **Afegir/Modificar assignatures**
```python
subjects = {
    'catala': 'https://examens.cat/llengua-catalana-i-literatura/',
    'nova_materia': 'URL_DE_LA_MATERIA'
}
```

3. **Canviar patrons URL**
```python
subject_patterns = {
    'catala': 'pau_llengua_catalana_i_literatura',
    'nova_materia': 'pau_nova_materia'
}
```

---

## 🇬🇧 English  

### What is this?  
A tool that downloads all university entrance exams and compiles them into a single dossier, so you don't have to print them one by one. I mainly created it for myself since I have to take this exam soon, and it will be helpful to have everything in one place.

### Features  
- 📥 Downloads exams from 2019 to 2024  
- 📚 Supports multiple subjects:  
  - Catalan Language & Literature  
  - Spanish Language & Literature  
  - History  
  - History of Philosophy  
- 📂 Organizes everything neatly by year  
- 📎 Creates merged PDFs with all exams + solutions  
- 🎯 Focus on June exams (except 2020, which uses July)  

### How to Use  
1. Install requirements:  
```bash
pip install requests beautifulsoup4 PyPDF2
```

2. Run the script:  
```bash
python examens.py
```

3. Study! (or pretend to 😉)  

### How to modify the code
1. **Change years range**
```python
def create_year_folders(base_path, start_year=2019, end_year=2024):
```

2. **Add/Modify subjects**
```python
subjects = {
    'catala': 'https://examens.cat/llengua-catalana-i-literatura/',
    'new_subject': 'SUBJECT_URL'
}
```

3. **Change URL patterns**
```python
subject_patterns = {
    'catala': 'pau_llengua_catalana_i_literatura',
    'new_subject': 'pau_new_subject'
}
```

---


### 📝 Note / Nota
All exams are from [examens.cat](https://examens.cat) / Tots els exàmens són de [examens.cat](https://examens.cat)