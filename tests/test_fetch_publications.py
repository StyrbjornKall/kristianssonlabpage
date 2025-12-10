import requests
from bs4 import BeautifulSoup
import json
import time

# URL of the Google Scholar profile
SCHOLAR_URL = "https://scholar.google.se/citations?hl=sv&user=WauDzPUAAAAJ&view_op=list_works&sortby=pubdate"

def fetch_publication_details(pub_url):
    """Fetch detailed information from individual publication page"""
    try:
        # Add a small delay to be respectful to the server
        time.sleep(1)
        
        response = requests.get(pub_url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract all field-value pairs
        fields = soup.select(".gsc_oci_field")
        values = soup.select(".gsc_oci_value")
        
        # Create a dictionary of field-value pairs
        data = {}
        for field, value in zip(fields, values):
            field_name = field.text.strip()
            field_value = value.text.strip()
            data[field_name] = field_value
        
        # Extract specific fields (Swedish field names from Google Scholar)
        authors = data.get("Författare", data.get("Authors", "Unknown"))
        # Try multiple field names for journal/source
        journal = data.get("Tidskrift", data.get("Källa", data.get("Journal", data.get("Conference", data.get("Book", "Unknown")))))
        
        # Extract year from publication date (format: YYYY/MM/DD or YYYY/MM or YYYY)
        pub_date = data.get("Publiceringsdatum", data.get("Publication date", "Unknown"))
        year = pub_date.split('/')[0] if '/' in pub_date else pub_date
        
        # Extract abstract/description
        abstract_element = soup.select_one("#gsc_oci_descr")
        abstract = abstract_element.text.strip() if abstract_element else "No abstract available"
        
        return {
            "authors": authors,
            "journal": journal,
            "abstract": abstract,
            "year": year
        }
    except Exception as e:
        print(f"  ⚠️  Error fetching details: {str(e)}")
        return {
            "authors": "Unknown",
            "journal": "Unknown",
            "abstract": "No abstract available",
            "year": "Unknown"
        }

print("🔍 Fetching publications from Google Scholar...")
print(f"URL: {SCHOLAR_URL}\n")

# Fetch the webpage content
response = requests.get(SCHOLAR_URL, headers={"User-Agent": "Mozilla/5.0"})
html = response.text

# Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Extract publication data - TEST ONLY FIRST 2 to save time
publications = []
publication_rows = soup.select(".gsc_a_tr")[:2]  # Only test first 2 publications
total_pubs = len(publication_rows)

print(f"🧪 TEST MODE: Fetching details for first {total_pubs} publications...\n")

for idx, row in enumerate(publication_rows, 1):
    title_element = row.select_one(".gsc_a_at")
    title = title_element.text.strip()
    link = "https://scholar.google.se" + title_element["href"]
    
    print(f"[{idx}/{total_pubs}] Processing: {title[:60]}...")
    
    # Fetch detailed information from the publication page
    details = fetch_publication_details(link)

    publications.append({
        "title": title,
        "link": link,
        "authors": details["authors"],
        "journal": details["journal"],
        "abstract": details["abstract"],
        "date": details["year"]
    })

print(f"\n✅ Successfully extracted {len(publications)} publications\n")
print("=" * 80)
print("DETAILED OUTPUT:")
print("=" * 80)

# Display publications in detail
for i, pub in enumerate(publications, 1):
    print(f"\n📄 Publication {i}:")
    print(f"   Title:    {pub['title']}")
    print(f"   Authors:  {pub['authors']}")
    print(f"   Journal:  {pub['journal']}")
    print(f"   Year:     {pub['date']}")
    print(f"   Abstract: {pub['abstract'][:200]}..." if len(pub['abstract']) > 200 else f"   Abstract: {pub['abstract']}")
    print(f"   Link:     {pub['link'][:80]}...")

print("\n" + "=" * 80)
print("FULL JSON OUTPUT:")
print("=" * 80)
print(json.dumps(publications, indent=2, ensure_ascii=False))

print("\n" + "=" * 80)
print(f"✅ Test completed! Verified {len(publications)} publications with full details.")
print("=" * 80)
