# GitHub Copilot Instructions for Kristiansson Research Group Website

## Project Overview

**Repository**: kristianssonlabofwonders  
**Owner**: StyrbjornKall  
**Branch**: main  
**Project Type**: Static academic research group website  
**Template**: Helios by HTML5 UP (CCA 3.0 license)  
**Research Focus**: Bioinformatics, AI, and Cheminformatics (Antibiotic Resistance)  
**Institution**: Chalmers University of Technology

## Architecture & Technology Stack

### Core Technologies
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom SCSS (compiled to CSS), Helios template base
- **JavaScript Libraries**: 
  - jQuery 3.x (DOM manipulation)
  - jquery.scrollex (scroll-based effects)
  - jquery.scrolly (smooth scrolling)
  - jquery.dropotron (dropdown menus)
- **Backend/Build**: None (static site)
- **Data Management**: JSON files for dynamic content
- **Hosting**: GitHub Pages

### Python Components
- **fetch_publications.py**: Python 3 script for web scraping
  - Uses: `requests`, `BeautifulSoup4`, `json`
  - Purpose: Scrapes Google Scholar profile for publications
  - Output: `publications.json`

## Site Structure

### Main Pages (5 total)

1. **index.html** - Homepage
   - Hero section with research group branding
   - News carousel (dynamically loaded)
   - **Unique**: Contains inline navigation (does NOT use modular nav.html)
   - Dependencies: `fetchcarousel.js`, `fetchfooter.js`

2. **people.html** - Team Members
   - Displays team profiles (Professor, Researcher, Postdoc, PhD Student)
   - Modal system for member biographies
   - Circular profile images (250px × 250px)
   - Dependencies: `fetchnav.js`, `fetchfooter.js`, `teambio.js`

3. **publications.html** - Research Publications
   - Key publications section (manually curated)
   - Latest papers section (dynamically loaded from JSON)
   - Collapsible abstracts
   - Dependencies: `fetchnav.js`, `fetchfooter.js`, `fetchpublications.js`

4. **research.html** - Research Areas
   - **Status**: Placeholder (under development)
   - Dependencies: `fetchnav.js`, `fetchfooter.js`

5. **news.html** - News & Updates
   - **Status**: Placeholder (under development)
   - Dependencies: `fetchnav.js`, `fetchfooter.js`

6. **contact.html** - Contact Information
   - Dynamically loads team contact info from bios.html
   - Organized by position hierarchy
   - Dependencies: `fetchnav.js`, `fetchfooter.js`, `fetchcontacts.js`

### Modular Components

#### nav.html
- **Purpose**: Reusable navigation header
- **Structure**: Header div with nav menu containing 6 links
- **Loaded by**: `fetchnav.js` into `<div id="nav-placeholder"></div>`
- **Used on**: All pages EXCEPT index.html
- **Menu Items**: Home, People, Research, Publications, News, Contact

#### footer.html
- **Purpose**: Reusable footer with social media and credits
- **Content**: Social media icons, copyright, HTML5 UP design credit
- **Loaded by**: `fetchfooter.js` into `<div id="footer-placeholder"></div>`
- **Used on**: All pages EXCEPT index.html

#### bios.html
- **Purpose**: Data source for team member biographies
- **Structure**: HTML div elements with class="bio" and unique IDs
- **ID Format**: lowercase name with underscores (e.g., `erik_kristiansson`)
- **Content**: Profile images, names, titles, biographies, contact info, social links
- **Used by**: `teambio.js` (modal system), `fetchcontacts.js` (contact page)

#### carousel.html
- **Purpose**: News carousel content for homepage
- **Structure**: Article elements with images, headers, and descriptions
- **Content**: Research highlights, awards, press coverage
- **Loaded by**: `fetchcarousel.js`
- **Features**: Infinite scroll, auto-advance, manual navigation

## JavaScript Architecture

### Core JavaScript Files (assets/js/)

#### 1. Modular Content Loaders

**fetchnav.js**
```javascript
// Loads nav.html into nav-placeholder
fetch('nav.html') → innerHTML → classList.remove('is-preload')
```

**fetchfooter.js**
```javascript
// Loads footer.html into footer-placeholder
fetch('footer.html') → innerHTML
```

**fetchcarousel.js**
```javascript
// Loads carousel.html and initializes carousel functionality
fetch('carousel.html') → innerHTML → initializeCarousel()
// Includes: auto-scroll, infinite loop, fade-in animation, navigation controls
```

#### 2. Dynamic Data Renderers

**fetchpublications.js**
```javascript
// Loads publications.json and renders publication tables
fetch('./publications.json') → generates HTML tables → innerHTML
// Features: linked titles, collapsible abstracts, toggleAbstract(id)
```

**fetchcontacts.js**
```javascript
// Extracts contact info from bios.html and renders contact list
fetch('bios.html') → parse DOM → extract emails → sort by position → innerHTML
// Hierarchy: Professor → Researcher → Postdoc → PhD Student
```

#### 3. Interactive Features

**teambio.js**
```javascript
// Modal system for team member biographies
openModal(person_id): fetch('bios.html') → querySelector('#' + person) → modal display
closeModal(): hide modal
```

#### 4. Template JavaScript (Helios)

- **main.js**: Core template functionality (dropdowns, scrolly, panels)
- **util.js**: Utility functions for template
- **browser.min.js**: Browser detection
- **breakpoints.min.js**: Responsive breakpoint management
- **jquery.*.js**: jQuery plugins for template features

## Data Flow & File Dependencies

### Publications Update Pipeline
```
Google Scholar Profile
    ↓ (scraped by)
fetch_publications.py
    ↓ (generates)
publications.json
    ↓ (loaded by)
fetchpublications.js
    ↓ (renders to)
publications.html
```

### Team Information Pipeline
```
bios.html (source of truth)
    ↓ (loaded by)
    ├─→ teambio.js → people.html (modal biographies)
    └─→ fetchcontacts.js → contact.html (contact list)
```

### Navigation/Footer Pipeline
```
nav.html & footer.html
    ↓ (loaded by)
fetchnav.js & fetchfooter.js
    ↓ (injected into)
All pages except index.html
```

## File Naming Conventions

### HTML Files
- Lowercase with underscores for data files: `bios.html`, `carousel.html`
- Lowercase with no separators for pages: `people.html`, `research.html`

### JavaScript Files
- Lowercase with camelCase: `fetchnav.js`, `teambio.js`
- Minified libraries: `*.min.js`

### Image Files
- Profile images: `[First Name] [Last Name].[ext]` (e.g., `Erik Kristiansson.PNG`)
- News images: Descriptive names (e.g., `water-treatment-plant-1920_1080.png`)
- Background images: `bg_bioinformatics_v2_[resolution].jpg`

### CSS/SCSS
- Main stylesheet: `main.css` (compiled from `main.scss`)
- SCSS partials: `_filename.scss` (in assets/sass/libs/)

## Coding Patterns & Best Practices

### HTML Structure Pattern
```html
<!DOCTYPE HTML>
<html>
<head>
    <title>Page Title</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="preload" as="image" href="images/bg_bioinformatics_v2_2K.jpg" />
    <link rel="stylesheet" href="assets/css/main.css" />
    <noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
</head>
<body class="[page-class] is-preload">
    <div id="page-wrapper">
        <!-- Placeholder for nav (except index.html) -->
        <div id="nav-placeholder"></div>
        
        <!-- Main content -->
        <div class="wrapper style1">
            <div class="container">
                <!-- Content here -->
            </div>
        </div>
        
        <!-- Placeholder for footer -->
        <div id="footer-placeholder"></div>
    </div>
    
    <!-- Scripts in specific order -->
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/js/jquery.dropotron.min.js"></script>
    <script src="assets/js/jquery.scrolly.min.js"></script>
    <script src="assets/js/jquery.scrollex.min.js"></script>
    <script src="assets/js/browser.min.js"></script>
    <script src="assets/js/breakpoints.min.js"></script>
    <script src="assets/js/util.js"></script>
    <script src="assets/js/main.js"></script>
    <!-- Page-specific scripts -->
</body>
</html>
```

### JavaScript Fetch Pattern
```javascript
fetch('filename.html')
    .then(response => response.text())
    .then(data => {
        document.getElementById('placeholder-id').innerHTML = data;
        // Optional: remove preload class or initialize features
        document.body.classList.remove('is-preload');
    })
    .catch(error => console.error('Error loading:', error));
```

### Modal Pattern (Team Biographies)
```javascript
function openModal(person_id) {
    // Fetch bios.html
    // Parse HTML into temp div
    // querySelector('#' + person_id)
    // Set modal content and display
}

function closeModal() {
    // Hide modal
}
```

### Profile Image Pattern
```html
<div class="col-4 col-12-mobile special" style="flex: 0 0 250px; margin: 1em;">
    <a href="#" class="image fit" onclick="event.preventDefault(); openModal('person_id')">
        <img src="images/Name.ext" alt="Name" 
             style="border-radius: 50%; width: 250px; height: 250px;" />
        <h3><b>Person Name</b></h3>
    </a>
    <p>Position</p>
</div>
```

## Development Workflow

### Local Development Setup
1. Clone repository: `git clone <repository-url>`
2. Pull latest changes: `git pull origin main`
3. Start local server: `python -m http.server` or `php -S localhost:8000`
4. Preview at: `http://localhost:8000`

### Making Changes
1. **HTML Pages**: Edit directly in root directory
2. **Styles**: Edit SCSS files in `assets/sass/`, compile to CSS
3. **JavaScript**: Edit JS files in `assets/js/`
4. **Team Members**: Update `bios.html` and add profile images to `images/`
5. **Publications**: Run `python fetch_publications.py` to regenerate JSON

### Commit & Deploy
```bash
git add .
git commit -m "Descriptive message"
git push origin main
```
- Changes automatically deploy to GitHub Pages
- URL format: `https://[username].github.io/[repository-name]/`

## Common Development Tasks

### Adding a New Team Member
1. Add profile image to `images/` (250×250px recommended)
2. Add biography div to `bios.html`:
   ```html
   <div id="firstname_lastname" class="bio" style="text-align: center;">
       <img src="images/Name.jpg" />
       <h3>Full Name</h3>
       <p>Position</p>
       <p>Biography text...</p>
       <a href="mailto:email@example.com">email@example.com</a>
   </div>
   ```
3. Add profile card to `people.html` in appropriate section
4. Contact info will automatically appear on contact page

### Adding a News Article to Carousel
1. Edit `carousel.html`
2. Add new `<article>` element:
   ```html
   <article>
       <a href="[url]" class="image featured"><img src="images/[image]" alt="" /></a>
       <header>
           <h3><a href="[url]">Article Title</a></h3>
       </header>
       <p>Article description...</p>
   </article>
   ```
3. Add news image to `images/` directory
4. Carousel automatically handles new articles

### Updating Publications
1. Ensure Python dependencies installed: `pip install requests beautifulsoup4`
2. Run scraper: `python fetch_publications.py`
3. Verify `publications.json` updated
4. Commit both script and JSON file if needed
5. Publications automatically render on page load

### Modifying Navigation
1. Edit `nav.html` for structure changes
2. Changes apply to all pages except index.html
3. For index.html navigation: edit inline nav in index.html

### Styling Changes
1. Edit SCSS files in `assets/sass/`
2. Compile to CSS: `sass assets/sass/main.scss assets/css/main.css`
3. Or edit `main.css` directly for quick changes
4. Respect Helios template structure for consistency

## Important Notes for AI Agents

### Critical Rules
1. **Never remove jQuery**: Template heavily depends on jQuery and plugins
2. **Script loading order matters**: jQuery must load before plugins and main.js
3. **index.html is special**: Uses inline navigation, not modular nav.html
4. **File paths are relative**: All paths assume root as working directory
5. **Modular components**: Changes to nav.html, footer.html, bios.html affect multiple pages
6. **Profile IDs**: Must be lowercase with underscores in bios.html

### When Making Changes
- **Adding pages**: Follow the HTML structure pattern, include nav/footer placeholders
- **Modifying JavaScript**: Test in local server (file:// protocol blocks fetch requests)
- **Image optimization**: Use appropriate resolutions (2K for backgrounds, 250×250 for profiles)
- **Cross-browser compatibility**: Test features in multiple browsers
- **Responsive design**: Use Helios grid system (col-*, wrapper, container classes)

### Data Sources & APIs
- **Publications**: Google Scholar profile (SCHOLAR_URL in fetch_publications.py)
- **No external APIs**: Site is fully static, no backend services
- **JSON files**: Serve as lightweight database for dynamic content

### Testing Considerations
- **Local server required**: Use `python -m http.server` for JavaScript fetch() calls
- **Browser console**: Check for fetch errors, modal issues, carousel problems
- **Mobile responsive**: Test at various breakpoints (Helios is mobile-friendly)
- **Image loading**: Verify preload optimization for background images

### Security & Performance
- **No sensitive data**: All content is public (academic research group)
- **Image optimization**: Compress images before upload
- **Lazy loading**: Consider for carousel images if performance issues arise
- **CDN**: Consider for jQuery if performance matters

## Project-Specific Quirks

1. **Swedish field names in scraper**: Google Scholar uses Swedish field names ("Författare", "Tidskrift", "Publiceringsdatum") - scraper handles both Swedish and English
2. **Carousel visibility logic**: Different behavior for carousels near top vs. further down page
3. **Modal cleanup**: Modals must be explicitly closed, no auto-close on outside click
4. **Profile image formats**: Mixed PNG/JPG extensions, not standardized
5. **Placeholder pages**: research.html and news.html show "working on it..." with moodeng_sleeping.jpg
6. **Contact extraction**: Relies on specific HTML structure in bios.html (mailto links)

## Future Development Considerations

### Planned Features (Inferred from Placeholders)
- Research page content (currently placeholder)
- News page with dynamic news feed (currently placeholder)
- Potential backend integration for publications (currently static scraping)

### Scalability Considerations
- Consider CMS integration if content updates become frequent
- Database backend for publications if scraping becomes unreliable
- Image lazy loading for performance optimization
- Build system (webpack/vite) for JavaScript bundling

### Maintenance Considerations
- Google Scholar HTML changes may break scraper
- jQuery/plugin updates may require compatibility testing
- Template updates from HTML5 UP may require careful merging
- Profile image size standardization recommended

## Helpful Commands

### Python
```bash
# Install dependencies
pip install requests beautifulsoup4

# Update publications
python fetch_publications.py

# Run tests
python -m pytest tests/
```

### Local Server
```bash
# Python server
python -m http.server

# PHP server
php -S localhost:8000
```

### Git Workflow
```bash
# Pull latest
git pull origin main

# Stage and commit
git add .
git commit -m "Description"

# Push to GitHub Pages
git push origin main
```

## Contact & Resources

- **Repository Owner**: StyrbjornKall
- **Research Group**: Kristiansson Research Group, Chalmers University of Technology
- **Template Credits**: Helios by HTML5 UP (html5up.net)
- **License**: CCA 3.0 (template), project-specific for content

## Document Version
Last Updated: January 5, 2026  
Maintainer: Repository collaborators  
Review Frequency: As needed with major changes
