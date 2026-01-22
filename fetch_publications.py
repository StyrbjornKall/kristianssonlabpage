import requests
from bs4 import BeautifulSoup
import json
import time
import random

# URL of the Google Scholar profile
SCHOLAR_URL = "https://scholar.google.se/citations?hl=sv&user=WauDzPUAAAAJ&view_op=list_works&sortby=pubdate"

def get_random_user_agent():
    """Return a random user agent to avoid detection"""
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15"
    ]
    return random.choice(user_agents)

def fetch_publication_details(pub_url, retry_count=0, max_retries=3):
    """Fetch detailed information from individual publication page with retry logic"""
    try:
        # Add exponential backoff delay
        delay = (2 ** retry_count) + random.uniform(0, 1)
        time.sleep(delay)
        
        headers = {
            "User-Agent": get_random_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        
        response = requests.get(pub_url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"  ⚠️  HTTP {response.status_code} for publication details")
            if retry_count < max_retries:
                print(f"  🔄 Retrying... (attempt {retry_count + 1}/{max_retries})")
                return fetch_publication_details(pub_url, retry_count + 1, max_retries)
            return get_default_details()
        
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
    except requests.exceptions.RequestException as e:
        print(f"  ⚠️  Network error: {str(e)}")
        if retry_count < max_retries:
            print(f"  🔄 Retrying... (attempt {retry_count + 1}/{max_retries})")
            return fetch_publication_details(pub_url, retry_count + 1, max_retries)
        return get_default_details()
    except Exception as e:
        print(f"  ⚠️  Error fetching details: {str(e)}")
        return get_default_details()

def get_default_details():
    """Return default details when fetching fails"""
    return {
        "authors": "Unknown",
        "journal": "Unknown",
        "abstract": "No abstract available",
        "year": "Unknown"
    }

def main():
    print("🔍 Fetching publications list from Google Scholar...")
    print(f"📍 URL: {SCHOLAR_URL}")
    
    # Enhanced headers to appear more like a real browser
    headers = {
        "User-Agent": get_random_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none"
    }
    
    try:
        response = requests.get(SCHOLAR_URL, headers=headers, timeout=10)
        
        # Debug information
        print(f"📊 Response Status: {response.status_code}")
        print(f"📊 Response Length: {len(response.text)} characters")
        
        if response.status_code != 200:
            print(f"❌ HTTP Error {response.status_code}")
            print(f"🔍 Response preview:\n{response.text[:500]}\n")
            # Try to load existing publications.json if request fails
            try:
                with open("publications.json", "r", encoding="utf-8") as f:
                    existing_pubs = json.load(f)
                    print(f"⚠️  Using existing publications.json with {len(existing_pubs)} publications")
                    return
            except FileNotFoundError:
                print("❌ No existing publications.json found. Creating empty file.")
                with open("publications.json", "w", encoding="utf-8") as f:
                    json.dump([], f, ensure_ascii=False, indent=4)
                return
        
        html = response.text
        
        # Check if we got a CAPTCHA or block page
        if "captcha" in html.lower() or "unusual traffic" in html.lower():
            print("❌ Google Scholar has detected bot traffic and returned a CAPTCHA page!")
            print("🔍 Using existing publications.json (if available)")
            try:
                with open("publications.json", "r", encoding="utf-8") as f:
                    existing_pubs = json.load(f)
                    print(f"✅ Loaded {len(existing_pubs)} publications from existing file")
                    return
            except FileNotFoundError:
                print("❌ No existing publications.json found.")
                return
        
        # Parse the HTML
        soup = BeautifulSoup(html, "html.parser")
        
        # Extract publication data
        publications = []
        publication_rows = soup.select(".gsc_a_tr")
        total_pubs = len(publication_rows)
        
        print(f"📚 Found {total_pubs} publications")
        
        if total_pubs == 0:
            print("⚠️  No publications found! Saving debug information...")
            with open("debug_response.html", "w", encoding="utf-8") as f:
                f.write(html)
            print("🔍 HTML response saved to debug_response.html for inspection")
            
            # Try to use existing publications.json
            try:
                with open("publications.json", "r", encoding="utf-8") as f:
                    existing_pubs = json.load(f)
                    print(f"✅ Using existing publications.json with {len(existing_pubs)} publications")
                    return
            except FileNotFoundError:
                print("❌ No existing publications.json found. Creating empty file.")
                with open("publications.json", "w", encoding="utf-8") as f:
                    json.dump([], f, ensure_ascii=False, indent=4)
                return
        
        print(f"⏳ Fetching details for each publication...\n")
        
        for idx, row in enumerate(publication_rows, 1):
            title_element = row.select_one(".gsc_a_at")
            if not title_element:
                print(f"[{idx}/{total_pubs}] ⚠️  Skipping row - no title found")
                continue
                
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
        
        # Save the data to a JSON file
        print(f"\n💾 Saving {len(publications)} publications to publications.json...")
        with open("publications.json", "w", encoding="utf-8") as f:
            json.dump(publications, f, ensure_ascii=False, indent=4)
        
        print("✅ Publications JSON file updated successfully!")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {str(e)}")
        print("⚠️  Attempting to use existing publications.json")
        try:
            with open("publications.json", "r", encoding="utf-8") as f:
                existing_pubs = json.load(f)
                print(f"✅ Using existing file with {len(existing_pubs)} publications")
        except FileNotFoundError:
            print("❌ No existing publications.json found")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        raise

if __name__ == "__main__":
    main()