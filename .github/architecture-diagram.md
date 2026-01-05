# Architecture Diagram for Kristiansson Research Group Website

## High-Level System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    GitHub Pages Hosting                      │
│           (Static Site, Auto-deploys from main)             │
└─────────────────────────────────────────────────────────────┘
                              ▲
                              │
                         git push
                              │
┌─────────────────────────────────────────────────────────────┐
│                  Local Development Server                    │
│              (python -m http.server:8000)                   │
└─────────────────────────────────────────────────────────────┘
```

## Page-Level Architecture

### Homepage (index.html) - Unique Structure

```
┌────────────────────────────────────────────────────────┐
│                     index.html                          │
├────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────┐     │
│  │  INLINE Navigation (not modular)              │     │
│  │  - Home, People, Research, Publications...    │     │
│  └──────────────────────────────────────────────┘     │
│                                                         │
│  ┌──────────────────────────────────────────────┐     │
│  │  Hero Section                                 │     │
│  │  "Kristiansson Research Group"                │     │
│  │  Bioinformatics | AI | Cheminformatics       │     │
│  └──────────────────────────────────────────────┘     │
│                                                         │
│  ┌──────────────────────────────────────────────┐     │
│  │  Carousel Placeholder                         │     │
│  │  <div id="carousel-placeholder"></div>        │     │
│  │         ▲                                     │     │
│  └─────────┼─────────────────────────────────────┘     │
│            │                                            │
│    ┌───────▼────────┐                                  │
│    │ fetchcarousel.js│                                 │
│    └───────┬────────┘                                  │
│            │ loads                                      │
│    ┌───────▼────────┐                                  │
│    │ carousel.html  │ (News articles)                  │
│    └────────────────┘                                  │
│                                                         │
│  ┌──────────────────────────────────────────────┐     │
│  │  Footer Placeholder                           │     │
│  │  <div id="footer-placeholder"></div>          │     │
│  │         ▲                                     │     │
│  └─────────┼─────────────────────────────────────┘     │
│            │                                            │
│    ┌───────▼────────┐                                  │
│    │ fetchfooter.js │                                  │
│    └───────┬────────┘                                  │
│            │ loads                                      │
│    ┌───────▼────────┐                                  │
│    │  footer.html   │                                  │
│    └────────────────┘                                  │
└────────────────────────────────────────────────────────┘
```

### Standard Page Architecture (All pages except index.html)

```
┌────────────────────────────────────────────────────────┐
│     people.html / publications.html / etc.             │
├────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────┐     │
│  │  Nav Placeholder                              │     │
│  │  <div id="nav-placeholder"></div>             │     │
│  │         ▲                                     │     │
│  └─────────┼─────────────────────────────────────┘     │
│            │                                            │
│    ┌───────▼────────┐                                  │
│    │  fetchnav.js   │                                  │
│    └───────┬────────┘                                  │
│            │ loads                                      │
│    ┌───────▼────────┐                                  │
│    │    nav.html    │ (Shared navigation)              │
│    └────────────────┘                                  │
│                                                         │
│  ┌──────────────────────────────────────────────┐     │
│  │  Main Content Area                            │     │
│  │  (Page-specific content + dynamic data)       │     │
│  └──────────────────────────────────────────────┘     │
│                                                         │
│  ┌──────────────────────────────────────────────┐     │
│  │  Footer Placeholder                           │     │
│  │  <div id="footer-placeholder"></div>          │     │
│  │         ▲                                     │     │
│  └─────────┼─────────────────────────────────────┘     │
│            │                                            │
│    ┌───────▼────────┐                                  │
│    │ fetchfooter.js │                                  │
│    └───────┬────────┘                                  │
│            │ loads                                      │
│    ┌───────▼────────┐                                  │
│    │  footer.html   │                                  │
│    └────────────────┘                                  │
└────────────────────────────────────────────────────────┘
```

## Data Flow Architectures

### Publications Pipeline

```
┌─────────────────────────────────────────────────────────┐
│  Google Scholar Profile                                  │
│  (https://scholar.google.se/citations?user=...)         │
└────────────────┬────────────────────────────────────────┘
                 │ Web scraping (requests + BeautifulSoup)
                 │
         ┌───────▼──────────┐
         │ fetch_publications│
         │       .py         │
         │                   │
         │ Extracts:         │
         │ - Title           │
         │ - Authors         │
         │ - Journal         │
         │ - Year            │
         │ - Abstract        │
         │ - Link            │
         └───────┬───────────┘
                 │ Generates JSON
                 │
         ┌───────▼──────────┐
         │ publications.json │
         │                   │
         │ [                 │
         │   {               │
         │     "title": "...",│
         │     "authors": ...,│
         │     "date": "...", │
         │     ...           │
         │   }               │
         │ ]                 │
         └───────┬───────────┘
                 │ Loaded by fetch()
                 │
    ┌────────────▼────────────┐
    │  fetchpublications.js    │
    │                          │
    │  - Fetches JSON          │
    │  - Generates HTML tables │
    │  - Adds abstract toggles │
    └────────────┬─────────────┘
                 │ innerHTML injection
                 │
         ┌───────▼──────────┐
         │ publications.html │
         │                   │
         │ Renders:          │
         │ - Year            │
         │ - Title (linked)  │
         │ - Authors         │
         │ - Abstract toggle │
         └───────────────────┘
```

### Team Biography System

```
┌─────────────────────────────────────────────────────────┐
│                      bios.html                           │
│                 (Single Source of Truth)                 │
│                                                          │
│  <div id="erik_kristiansson" class="bio">               │
│    <img src="images/Erik Kristiansson.PNG" />           │
│    <h3>Erik Kristiansson</h3>                           │
│    <p>Professor</p>                                     │
│    <p>Biography text...</p>                             │
│    <a href="mailto:erik@example.com">email</a>          │
│  </div>                                                 │
└──────────────┬────────────────────┬─────────────────────┘
               │                    │
               │                    │
       ┌───────▼──────┐     ┌───────▼──────┐
       │  teambio.js  │     │fetchcontacts │
       │              │     │     .js      │
       └──────┬───────┘     └──────┬───────┘
              │                    │
              │ openModal()        │ loadContactInfo()
              │                    │
              │                    │
      ┌───────▼───────┐    ┌───────▼──────────┐
      │  people.html  │    │  contact.html     │
      │               │    │                   │
      │  Modal popup  │    │  Contact list     │
      │  with full    │    │  sorted by        │
      │  biography    │    │  position         │
      └───────────────┘    └───────────────────┘
```

### Contact Information Extraction Flow

```
┌─────────────────────────────────────────────────────────┐
│                   fetchcontacts.js                       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  1. fetch('bios.html')                                  │
│           ↓                                              │
│  2. Parse HTML into temporary DOM                        │
│           ↓                                              │
│  3. querySelectorAll('.bio')                            │
│           ↓                                              │
│  4. For each bio:                                        │
│     - Extract name from <h3>                            │
│     - Extract position from first <p>                   │
│     - Extract email from <a href="mailto:...">          │
│           ↓                                              │
│  5. Sort by position hierarchy:                         │
│     - Professor (1)                                     │
│     - Researcher (2)                                    │
│     - Postdoc (3)                                       │
│     - PhD Student (4)                                   │
│           ↓                                              │
│  6. Generate HTML with grouped sections                 │
│           ↓                                              │
│  7. Inject into <div id="contact-list">                 │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Modal Biography System Flow

```
User clicks profile on people.html
         │
         ▼
┌────────────────────────┐
│ onclick="openModal(    │
│   'firstname_lastname')│
│        "               │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│   teambio.js           │
│   openModal(person_id) │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ fetch('bios.html')     │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ Parse into temp div    │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ querySelector(         │
│   '#' + person_id)     │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ Extract innerHTML      │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ Set modal content      │
│ modal.style.display    │
│   = "block"            │
└────────────────────────┘
         │
         ▼
    Modal appears
    with full bio
```

## JavaScript Dependency Chain

```
┌──────────────────────────────────────────────────────────┐
│                  Script Loading Order                     │
│              (MUST be maintained exactly)                 │
└──────────────────────────────────────────────────────────┘

1. jquery.min.js
   └─ Foundation for all jQuery plugins and custom scripts
      │
      ├─ 2. jquery.dropotron.min.js (Dropdown menus)
      │
      ├─ 3. jquery.scrolly.min.js (Smooth scrolling)
      │
      └─ 4. jquery.scrollex.min.js (Scroll-based effects)

5. browser.min.js (Browser detection)

6. breakpoints.min.js (Responsive breakpoints)

7. util.js (Utility functions)

8. main.js (Template core functionality)
   └─ Requires all above to be loaded

9. Page-specific scripts (can be in any order among themselves)
   ├─ fetchnav.js
   ├─ fetchfooter.js
   ├─ fetchcarousel.js
   ├─ fetchpublications.js
   ├─ fetchcontacts.js
   └─ teambio.js
```

## File Relationship Matrix

```
┌─────────────────┬──────────┬──────────┬───────────┬──────────┐
│                 │ nav.html │footer.html│ bios.html │carousel  │
│                 │          │           │           │  .html   │
├─────────────────┼──────────┼──────────┼───────────┼──────────┤
│ index.html      │    ✗     │    ✓     │     ✗     │    ✓     │
├─────────────────┼──────────┼──────────┼───────────┼──────────┤
│ people.html     │    ✓     │    ✓     │     ✓     │    ✗     │
├─────────────────┼──────────┼──────────┼───────────┼──────────┤
│ publications    │    ✓     │    ✓     │     ✗     │    ✗     │
│   .html         │          │          │           │          │
├─────────────────┼──────────┼──────────┼───────────┼──────────┤
│ research.html   │    ✓     │    ✓     │     ✗     │    ✗     │
├─────────────────┼──────────┼──────────┼───────────┼──────────┤
│ news.html       │    ✓     │    ✓     │     ✗     │    ✗     │
├─────────────────┼──────────┼──────────┼───────────┼──────────┤
│ contact.html    │    ✓     │    ✓     │     ✓     │    ✗     │
└─────────────────┴──────────┴──────────┴───────────┴──────────┘

✓ = Uses this modular component
✗ = Does not use (index.html has inline nav instead)
```

## Styling Architecture

```
┌──────────────────────────────────────────────────┐
│              assets/sass/main.scss                │
│         (SCSS source, compiles to CSS)            │
└────────────────┬─────────────────────────────────┘
                 │ Imports from libs/
                 │
    ┌────────────┼────────────────┬──────────────┐
    │            │                │              │
    ▼            ▼                ▼              ▼
┌─────────┐  ┌─────────┐  ┌───────────┐  ┌──────────┐
│_vars.scss│  │_mixins  │  │_functions │  │_html-grid│
│         │  │ .scss   │  │  .scss    │  │  .scss   │
│Variables│  │ Mixins  │  │ Functions │  │   Grid   │
└─────────┘  └─────────┘  └───────────┘  └──────────┘
    │            │                │              │
    └────────────┼────────────────┴──────────────┘
                 │ Compiled to
                 ▼
         ┌───────────────┐
         │ assets/css/   │
         │   main.css    │
         │               │
         │ (Loaded by    │
         │  all pages)   │
         └───────────────┘
```

## Image Asset Structure

```
images/
├── Profile Images (250x250px, circular display)
│   ├── Erik Kristiansson.PNG
│   ├── Anna Johnning.PNG
│   ├── Mikael Gustavsson.jpg
│   ├── David Lund.jpg
│   ├── Helga Kristin Olafsdottir.jpg
│   ├── Styrbjorn Kall.JPG
│   ├── Sophia Axillus.PNG
│   └── Laleh Varghaei.jpg
│
├── Background Images (Full-screen hero)
│   ├── bg_bioinformatics_v2_2K.jpg (1920x1080)
│   └── bg_bioinformatics_v2_4K.jpg (3840x2160)
│
├── News/Carousel Images
│   ├── Erik_Carolina.png
│   ├── trioprize2025.png
│   ├── water-treatment-plant-1920_1080.png
│   ├── 2miljoner_erikanna.PNG
│   ├── newdiagnosticmethodsspreadresistence.jpg
│   └── sverigesradiologga.png
│
└── Placeholder Images
    └── moodeng_sleeping.jpg (for unfinished pages)
```

## Development Workflow Diagram

```
┌─────────────────────────────────────────────────────────┐
│                   Development Cycle                      │
└─────────────────────────────────────────────────────────┘

1. git pull origin main
         │
         ▼
2. Make local changes
   ├─ Edit HTML files
   ├─ Edit JavaScript (assets/js/)
   ├─ Edit SCSS (assets/sass/) → compile to CSS
   ├─ Add/update images (images/)
   ├─ Update bios.html for team changes
   └─ Run fetch_publications.py for pub updates
         │
         ▼
3. Test locally
   python -m http.server
   http://localhost:8000
         │
         ▼
4. Verify functionality
   ├─ Check browser console
   ├─ Test navigation
   ├─ Test modals
   ├─ Test responsive design
   └─ Verify fetch() calls succeed
         │
         ▼
5. git add .
   git commit -m "Descriptive message"
   git push origin main
         │
         ▼
6. GitHub Pages auto-deploys
   (Wait 1-2 minutes)
         │
         ▼
7. Verify on live site
   https://styrbjornkall.github.io/kristianssonlabofwonders/
```

## Component Interaction Map

```
                    ┌────────────┐
                    │  Browser   │
                    │   Client   │
                    └─────┬──────┘
                          │
          ┌───────────────┼───────────────┐
          │               │               │
    ┌─────▼─────┐   ┌─────▼─────┐  ┌─────▼─────┐
    │HTML Pages │   │CSS Styles │  │JavaScript │
    │ (Static)  │   │ (Helios)  │  │ (Dynamic) │
    └─────┬─────┘   └───────────┘  └─────┬─────┘
          │                              │
          │         ┌────────────────────┼────────┐
          │         │                    │        │
    ┌─────▼─────────▼─┐         ┌────────▼───┐ ┌─▼────────┐
    │Modular Components│         │Data Sources│ │Template  │
    │- nav.html        │         │- JSON files│ │JavaScript│
    │- footer.html     │         │- bios.html │ │- jQuery  │
    │- carousel.html   │         └────────────┘ │- Plugins │
    │- bios.html       │                        └──────────┘
    └──────────────────┘
```

---

**Diagram Version**: 1.0  
**Last Updated**: January 5, 2026  
**Maintained by**: Repository collaborators
