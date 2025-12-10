import requests
from bs4 import BeautifulSoup

# Test URL - second publication
TEST_URL = "https://scholar.google.se/citations?view_op=view_citation&hl=sv&user=WauDzPUAAAAJ&sortby=pubdate&citation_for_view=WauDzPUAAAAJ:9c2xU6iGI7YC"

print("🔍 Debugging Scholar page structure...")
print(f"URL: {TEST_URL}\n")

response = requests.get(TEST_URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

print("=" * 80)
print("ALL FIELD-VALUE PAIRS:")
print("=" * 80)

fields = soup.select(".gsc_oci_field")
values = soup.select(".gsc_oci_value")

for i, (field, value) in enumerate(zip(fields, values), 1):
    field_name = field.text.strip()
    field_value = value.text.strip()
    print(f"{i}. Field: '{field_name}'")
    print(f"   Value: '{field_value[:100]}...'") if len(field_value) > 100 else print(f"   Value: '{field_value}'")
    print()

print("=" * 80)
print("ABSTRACT SECTION:")
print("=" * 80)
abstract = soup.select_one("#gsc_oci_descr")
if abstract:
    print(abstract.text.strip()[:300] + "...")
else:
    print("No abstract found")
