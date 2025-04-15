import os
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfMerger
import re
from pathlib import Path

def download_pdf(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        return True
    return False

def create_year_folders(base_path, start_year=2019, end_year=2024):
    # Create folders for all years, even if no exams available
    for year in range(start_year, end_year + 1):
        folder_path = os.path.join(base_path, str(year))
        os.makedirs(folder_path, exist_ok=True)

def process_subject(url, subject_name):
    base_path = os.path.join(os.getcwd(), subject_name)
    os.makedirs(base_path, exist_ok=True)
    create_year_folders(base_path)

    # Dictionary to map subject names to their URL patterns
    subject_patterns = {
        'catala': 'pau_llengua_catalana_i_literatura',
        'castella': 'pau_llengua_castellana_i_literatura',
        'historia': 'pau_historia',
        'filosofia': 'pau_hfil'  # Different pattern for philosophy
    }

    # Handle 2022 specially with direct URLs
    year_path = os.path.join(base_path, '2022')
    pattern = subject_patterns[subject_name]
    
    exam_url = f"https://examens.cat/wp-content/uploads/2022/07/{pattern}_2022_Juny_Enunciat.pdf"
    solution_url = f"https://examens.cat/wp-content/uploads/2022/07/{pattern}_2022_Juny_Solucio.pdf"
    
    print(f"Downloading 2022 exam for {subject_name}...")
    download_pdf(exam_url, os.path.join(year_path, 'examen_juny.pdf'))
    print(f"Downloading 2022 solution for {subject_name}...")
    download_pdf(solution_url, os.path.join(year_path, 'solucio_juny.pdf'))

    # Continue with regular processing for other years
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        
        for link in links:
            href = link.get('href')
            if href and href.endswith('.pdf'):
                text = link.get_text().lower()
                year_match = re.search(r'20\d{2}', text)
                
                if year_match:
                    year = int(year_match.group())
                    if year < 2019 or year > 2024:
                        continue
                    
                    # Handle 2020 specially
                    if year == 2020 and 'juliol' not in text:
                        continue
                    # For all other years, get June exams
                    elif year != 2020 and 'juny' not in text:
                        continue
                        
                    # Determine month (July for 2020, June for all others)
                    month = 'juliol' if year == 2020 else 'juny'
                    
                    # Skip September exams
                    if 'setembre' in text:
                        continue
                        
                    is_solution = 'solució' in text or 'solucion' in text
                    filename = f"{'solucio' if is_solution else 'examen'}_{month}.pdf"
                    save_path = os.path.join(base_path, str(year), filename)
                    
                    print(f"Downloading {filename} for {year}...")
                    download_pdf(href, save_path)

def merge_pdfs(subject_name):
    base_path = os.path.join(os.getcwd(), subject_name)
    merger = PdfMerger()
    
    # Iterate through all years
    for year in range(2019, 2025):
        year_path = os.path.join(base_path, str(year))
        if not os.path.exists(year_path):
            continue
            
        # Determine which month to look for based on year
        month = 'juliol' if year == 2020 else 'juny'
        
        exam_path = os.path.join(year_path, f"examen_{month}.pdf")
        solution_path = os.path.join(year_path, f"solucio_{month}.pdf")
        
        if os.path.exists(exam_path):
            print(f"Adding {year} exam...")
            merger.append(exam_path)
            
        if os.path.exists(solution_path):
            print(f"Adding {year} solution...")
            merger.append(solution_path)
    
    complete_pdf_path = os.path.join(base_path, f"{subject_name}_tots_els_anys.pdf")
    merger.write(complete_pdf_path)
    merger.close()
    print(f"Created complete collection: {complete_pdf_path}")

def main():
    subjects = {
        'catala': 'https://examens.cat/llengua-catalana-i-literatura/',
        'castella': 'https://examens.cat/llengua-castellana-i-literatura/',
        'historia': 'https://examens.cat/historia/',
        'filosofia': 'https://examens.cat/historia-de-la-filosofia/'
    }
    
    for subject_name, url in subjects.items():
        print(f"\nProcessing {subject_name}...")
        process_subject(url, subject_name)
        merge_pdfs(subject_name)

if __name__ == "__main__":
    main()