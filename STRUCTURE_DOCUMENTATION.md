# Kristiansson Research Group Website - Structure Documentation

## Overview
This is a research group website for the Kristiansson Research Group at Chalmers University of Technology, built using the **Helios template** from HTML5 UP. The website focuses on bioinformatics, AI, and cheminformatics research, specifically around antibiotic resistance.

**Repository**: kristianssonlabofwonders (Owner: StyrbjornKall)  
**Branch**: main  
**Template**: Helios by HTML5 UP (CCA 3.0 license)

---

## Site Architecture

### Page Structure
The website consists of **5 main HTML pages** with a consistent modular structure:

1. **index.html** - Homepage with news carousel
2. **people.html** - Team member profiles with modal biographies
3. **research.html** - Research information (currently placeholder)
4. **publications.html** - Publications list with dynamic content
5. **news.html** - News section (currently placeholder)

### Common Components (Modular Design)
All pages share these reusable components loaded via JavaScript:

- **nav.html** - Navigation header (loaded by `fetchnav.js`)
- **footer.html** - Footer with social media links (loaded by `fetchfooter.js`)
- **bios.html** - Team member biographies (loaded by `teambio.js`)

---

## Page Details

### 1. index.html (Homepage)
**Purpose**: Landing page showcasing the research group and recent news

**Key Features**:
- Hero section with group name and tagline: "Bioinformatics | AI | Cheminformatics"
- Carousel section with 5+ news articles featuring:
  - Areas of Advance prize for antibiotic resistance work
  - AI model for predicting multi-resistance in bacteria
  - Swedish Research Council funding
  - AI diagnostics for resistant bacteria
  - Swedish Radio interview feature
- Embedded navigation in header (not using modular nav.html)

**Navigation**: Contains full inline navigation menu linking to all other pages

**Content Type**: Static HTML with carousel functionality

---

### 2. people.html (POEPLE Page)
**Purpose**: Display research group members with detailed biographies

**Key Features**:
- Modular navigation (loaded from nav.html via placeholder)
- Team members organized by role:
  - **Professors/Researchers**: Erik Kristiansson, Anna Johnning, Mikael Gustavsson
  - **Postdocs**: Helga Kristín Ólafsdóttir, David Lund
  - **PhD Students**: Styrbjörn Käll (and others)
- Circular profile images (250px × 250px)
- Clickable profiles that open modal windows with full biographies
- Modal functionality powered by `teambio.js`

**JavaScript Dependencies**:
- `fetchnav.js` - Loads navigation
- `fetchfooter.js` - Loads footer
- `teambio.js` - Handles modal biography display

**Data Source**: `bios.html` (contains all biography content)

**Modal System**:
- Function: `openModal(person_id)` - Fetches and displays biography
- Function: `closeModal()` - Closes biography modal
- Biographies stored as div elements with IDs matching team member names

---

### 3. research.html (Research Page)
**Purpose**: Display research areas and projects

**Current Status**: Placeholder page with "working on it..." message and moodeng_sleeping.jpg image

**Structure**:
- Modular navigation and footer
- Content area ready for research information

**JavaScript Dependencies**:
- `fetchnav.js`
- `fetchfooter.js`

---

### 4. publications.html (Publications Page)
**Purpose**: Display research publications with key highlights and recent papers

**Key Features**:
- **Key Publications Section**: Manually curated highlight
  - 2024: "Transformers enable accurate prediction of acute and chronic chemical toxicity in aquatic organisms" (Science Advances)
  - Authors: Mikael Gustavsson, Styrbjörn Käll, et al.
- **Latest Papers Section**: Dynamically loaded from `publications.json`
- Table format displaying year, title (linked), and authors

**JavaScript Dependencies**:
- `fetchnav.js`
- `fetchfooter.js`
- `fetchpublications.js` - Fetches and renders publications from JSON

**Data Flow**:
1. `fetch_publications.py` scrapes Google Scholar profile
2. Generates `publications.json` with publication data
3. `fetchpublications.js` loads JSON and renders HTML tables

**Publications Data Structure** (publications.json):
```json
{
  "title": "Paper title",
  "link": "Google Scholar link",
  "authors": "Author list",
  "date": "Year"
}
```

---

### 5. news.html (News Page)
**Purpose**: Display news and updates

**Current Status**: Placeholder page with "working on it..." message and moodeng_sleeping.jpg image

**Structure**:
- Modular navigation and footer
- Content area ready for news items

**JavaScript Dependencies**:
- `fetchnav.js`
- `fetchfooter.js`

---

## Modular Components

### nav.html
**Purpose**: Reusable navigation header

**Structure**:
```html
<div id="header">
  <nav id="nav">
    <ul>
      <li>KRISTIANSSON RESEARCH GROUP (index.html)</li>
      <li>PEOPLE (people.html)</li>
      <li>RESEARCH (research.html)</li>
      <li>PUBLICATIONS (publications.html)</li>
      <li>NEWS (news.html)</li>
      <li>CONTACT (contact.html)</li>
    </ul>
  </nav>
</div>
```

**Loading**: Fetched by `fetchnav.js` into `<div id="nav-placeholder"></div>` on all pages except index.html

---

### footer.html
**Purpose**: Reusable footer with social media links

**Structure**:
- Platform icons section (Twitter, LinkedIn)
- Copyright notice
- Design credit to HTML5 UP

**Loading**: Fetched by `fetchfooter.js` into `<div id="footer-placeholder"></div>` on all pages except index.html

---

### bios.html
**Purpose**: Store all team member biographies

**Structure**: HTML div elements with unique IDs per team member

**Format**:
```html
<div id="person_name" class="bio" style="text-align: center;">
  <img src="..." />
  <h3>Name</h3>
  <p>Title</p>
  <p>Biography text with HTML formatting</p>
  <!-- Optional social icons -->
</div>
```

**HTML Formatting Support**:
- `<br>` - Line breaks
- `<b>` - Bold text
- `<i>` - Italic text
- `<a href="">` - Links
- Icon lists for social media profiles

**Loading**: Fetched by `teambio.js` when user clicks team member profile

---

## JavaScript Files

### Core Site Scripts (HTML5 UP Template)
- **jquery.min.js** - jQuery library
- **jquery.dropotron.min.js** - Dropdown menu functionality
- **jquery.scrolly.min.js** - Smooth scrolling
- **jquery.scrollex.min.js** - Scroll-based effects
- **browser.min.js** - Browser detection
- **breakpoints.min.js** - Responsive breakpoints
- **util.js** - Utility functions
- **main.js** - Main template functionality

### Custom Site Scripts
1. **fetchnav.js**
   - Fetches `nav.html` content
   - Injects into `#nav-placeholder` div
   - Used on: people.html, research.html, publications.html, news.html

2. **fetchfooter.js**
   - Fetches `footer.html` content
   - Injects into `#footer-placeholder` div
   - Used on: people.html, research.html, publications.html, news.html

3. **fetchpublications.js**
   - Fetches `publications.json`
   - Generates HTML table for each publication
   - Renders into `#publications-list` div
   - Used on: publications.html

4. **teambio.js**
   - `openModal(person)` - Fetches bios.html, extracts specific bio by ID, displays in modal
   - `closeModal()` - Hides modal
   - Used on: people.html

---

## Data Files

### publications.json
**Purpose**: Store publication metadata for dynamic rendering

**Generated By**: `fetch_publications.py` (Python script)

**Source**: Google Scholar profile scraping
- URL: https://scholar.google.se/citations?hl=sv&user=WauDzPUAAAAJ&view_op=list_works&sortby=pubdate

**Update Process**:
1. Run `fetch_publications.py` script
2. Script uses BeautifulSoup to scrape Google Scholar
3. Extracts: title, link, authors, publication year
4. Outputs to `publications.json`

**Structure**: Array of publication objects with fields:
- `title` - Publication title
- `link` - Google Scholar citation link
- `authors` - Author list
- `date` - Publication year

---

## CSS/Styling

### Main Stylesheets
- **main.css** - Primary styles compiled from SASS
- **fontawesome-all.min.css** - Icon font
- **noscript.css** - Fallback styles when JavaScript disabled

### SASS Source Files (assets/sass/)
- **main.scss** - Main stylesheet source
- **noscript.scss** - No-JS stylesheet source
- **libs/** - SASS library components:
  - `_breakpoints.scss` - Responsive breakpoints
  - `_functions.scss` - SASS functions
  - `_html-grid.scss` - Grid system
  - `_mixins.scss` - SASS mixins
  - `_vars.scss` - Variables (colors, fonts, spacing)
  - `_vendor.scss` - Vendor prefixes

---

## Page Interconnections

### Navigation Flow
```
index.html (Homepage)
    ├── people.html (Team)
    ├── research.html (Research) [placeholder]
    ├── publications.html (Publications)
    └── news.html (News) [placeholder]
```

### Component Loading Dependencies

**index.html**:
- Self-contained navigation (inline)
- No modular components loaded

**people.html**:
- Loads: nav.html, footer.html, bios.html (on demand)
- Dependencies: fetchnav.js, fetchfooter.js, teambio.js

**research.html**:
- Loads: nav.html, footer.html
- Dependencies: fetchnav.js, fetchfooter.js

**publications.html**:
- Loads: nav.html, footer.html, publications.json
- Dependencies: fetchnav.js, fetchfooter.js, fetchpublications.js

**news.html**:
- Loads: nav.html, footer.html
- Dependencies: fetchnav.js, fetchfooter.js

### Data Flow Diagrams

**Publications System**:
```
Google Scholar → fetch_publications.py → publications.json → fetchpublications.js → publications.html
```

**Team Bio System**:
```
bios.html ← teambio.js (openModal) ← people.html (click event)
```

**Navigation System**:
```
nav.html → fetchnav.js → all pages (except index.html)
footer.html → fetchfooter.js → all pages (except index.html)
```

---

## Development Workflow

### Local Preview
The site requires a local web server to function properly (JavaScript fetch API requires HTTP/HTTPS protocol).

**Methods**:
1. **Python**: `python -m http.server` (access at http://localhost:8000)
2. **PHP**: `php -S localhost:8000`

### Git Workflow (from README.md)
1. **Clone**: `git clone <repository-url>`
2. **Pull**: `git pull origin main`
3. **Edit**: Modify HTML/CSS/JS files
4. **Preview**: Use local server
5. **Commit**: 
   ```bash
   git add .
   git commit -m "Description"
   ```
6. **Push**: `git push origin main`

### Updating Publications
```bash
python fetch_publications.py
```
This regenerates `publications.json` from the latest Google Scholar data.

---

## Key Design Patterns

### 1. Modular Component Architecture
- **Pattern**: Shared HTML components (nav, footer, bios) stored separately
- **Loading**: JavaScript fetch API with placeholder divs
- **Benefit**: Single source of truth, easy maintenance

### 2. Dynamic Content Loading
- **Pattern**: JSON data files loaded via JavaScript
- **Use Cases**: Publications list
- **Benefit**: Separation of content from presentation

### 3. Modal Interactions
- **Pattern**: Click-triggered modals for detailed content
- **Use Cases**: Team member biographies
- **Benefit**: Clean UI with details on demand

### 4. Responsive Design
- **Pattern**: HTML5 UP template with breakpoints
- **Classes**: `col-12`, `col-4`, `col-12-mobile`
- **Benefit**: Mobile-friendly layouts

---

## File Naming Conventions

### HTML Pages
- Lowercase, descriptive: `index.html`, `people.html`, `publications.html`

### JavaScript Files
- Lowercase with descriptive names: `fetchnav.js`, `teambio.js`
- Purpose-driven naming (fetch*, team*)

### Images
- Person images: `[First Name] [Last Name].[ext]` (e.g., "Erik Kristiansson.PNG")
- Content images: Descriptive lowercase with underscores (e.g., "moodeng_sleeping.jpg")
- News images: Descriptive (e.g., "trioprize2025.png", "water-treatment-plant-1920_1080.png")

---

## Future Development Areas

### Current Placeholders
1. **research.html** - Needs research area content
2. **news.html** - Needs news article content
3. **Erik Kristiansson bio** - Currently placeholder: "Very good in terms of computer."
4. **Mikael Gustavsson bio** - Currently placeholder: "Very good in terms of computer."

### Potential Enhancements
- Move index.html to use modular nav/footer system
- Add news JSON system similar to publications
- Add filtering/search for publications
- Add research project cards with details
- Expand team bios with research interests/projects

---

## Important Notes for AI Agents

1. **Modular Loading**: Most pages (except index.html) use JavaScript to load nav and footer. Always check if changes need to be made to `nav.html` or `footer.html` rather than individual pages.

2. **Bio Updates**: Team member bios are stored in `bios.html`, NOT in `people.html`. To update a biography, edit the corresponding div in `bios.html`.

3. **Publications**: To add publications, either:
   - Run `fetch_publications.py` to scrape Google Scholar, OR
   - Manually edit `publications.json`

4. **Placeholder Pages**: `research.html` and `news.html` are currently placeholders. When developing these, follow the pattern used in `publications.html` and `people.html`.

5. **JavaScript Dependencies**: All pages require the full set of JavaScript files in the correct order (see individual page script sections).

6. **Local Server Required**: The site will not function properly when opened directly as files (file://) due to JavaScript fetch restrictions. Always use a local HTTP server for development.

7. **Template Styling**: The site uses the Helios template from HTML5 UP. Major styling changes should consider the template's grid system and design patterns.

---

## Quick Reference

### To Add a New Team Member:
1. Add photo to `/images/[Name].[ext]`
2. Add profile section in `people.html` with unique ID
3. Add biography div in `bios.html` with matching ID
4. Include onclick handler: `onclick="event.preventDefault(); openModal('person_id')"`

### To Update Publications:
```bash
python fetch_publications.py
```
Or manually edit `publications.json`

### To Add/Edit Navigation:
Edit `nav.html` (affects all pages except index.html)

### To Add/Edit Footer:
Edit `footer.html` (affects all pages except index.html)

### To Preview Locally:
```bash
python -m http.server
# Then visit http://localhost:8000
```

---

## Technical Stack Summary

- **Frontend**: HTML5, CSS3, JavaScript (vanilla + jQuery)
- **Template**: Helios by HTML5 UP
- **CSS Preprocessor**: SASS
- **Icons**: Font Awesome
- **Data**: JSON files
- **Scripting**: Python (for data scraping)
- **Version Control**: Git/GitHub
- **Hosting**: Static site (GitHub Pages compatible)

---

*This documentation was generated on December 9, 2025, to provide AI agents and developers with comprehensive context about the website structure.*
