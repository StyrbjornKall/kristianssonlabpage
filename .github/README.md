# GitHub Copilot Documentation

This directory contains comprehensive documentation for AI agents (GitHub Copilot, other LLMs) to understand and work with the Kristiansson Research Group website codebase.

## Documentation Files

### 1. copilot-instructions.md
**Purpose**: Complete reference guide for the entire project  
**Use when**: You need detailed information about any aspect of the project  
**Contains**:
- Project overview and technology stack
- Complete site structure and page descriptions
- JavaScript architecture and data flows
- File naming conventions
- Coding patterns and best practices
- Development workflow
- Common development tasks with code examples
- Important rules and considerations
- Troubleshooting guidance

**Best for**: Deep dives, understanding architecture, making complex changes

---

### 2. quick-reference.md
**Purpose**: Fast lookup for common tasks and patterns  
**Use when**: You need to quickly implement a common feature  
**Contains**:
- File and directory map
- Common code patterns (ready to copy/paste)
- Script loading order
- Data structure reference
- CSS class reference
- Testing checklist
- Troubleshooting guide
- Quick commands

**Best for**: Rapid development, implementing standard features, quick lookups

---

### 3. architecture-diagram.md
**Purpose**: Visual representation of system architecture  
**Use when**: You need to understand relationships and data flows  
**Contains**:
- High-level system architecture
- Page-level architecture diagrams
- Data flow diagrams (publications, biographies, contact)
- JavaScript dependency chain
- File relationship matrix
- Styling architecture
- Component interaction map

**Best for**: Understanding system design, visualizing connections, planning changes

---

## Quick Navigation Guide

### I want to...

#### Add a new team member
→ **quick-reference.md** → "Adding a Team Member (3 files to edit)"

#### Understand how publications work
→ **architecture-diagram.md** → "Publications Pipeline"  
→ **copilot-instructions.md** → "Publications Update Pipeline"

#### Add a news article to homepage
→ **quick-reference.md** → "Adding a Carousel News Item"

#### Create a new page
→ **quick-reference.md** → "Creating a New Page"  
→ **copilot-instructions.md** → "HTML Structure Pattern"

#### Understand JavaScript loading order
→ **quick-reference.md** → "Script Loading Order (Critical!)"  
→ **architecture-diagram.md** → "JavaScript Dependency Chain"

#### Fix a bug
→ **quick-reference.md** → "Troubleshooting Guide"  
→ Check browser console first!

#### Understand modular components
→ **architecture-diagram.md** → "Page-Level Architecture"  
→ **copilot-instructions.md** → "Modular Components"

#### Learn about data structures
→ **quick-reference.md** → "Data Structure Reference"

#### See coding patterns
→ **copilot-instructions.md** → "Coding Patterns & Best Practices"  
→ **quick-reference.md** → "Common Code Patterns"

---

## Reading Order for New AI Agents

### First Time Working with This Codebase?

**1. Start here**: `quick-reference.md` (15 min read)
   - Get the big picture
   - Understand file structure
   - See common patterns

**2. Then review**: `architecture-diagram.md` (10 min browse)
   - Visualize the system
   - Understand data flows
   - See component relationships

**3. Deep dive**: `copilot-instructions.md` (30 min read)
   - Complete understanding
   - All the details
   - Edge cases and quirks

**4. Keep handy**: All three files
   - Reference as needed
   - Search for specific topics
   - Follow examples

---

## Key Concepts to Understand

### Critical Rules (Read These First!)
1. **index.html is special**: Has inline navigation, not modular nav.html
2. **jQuery is essential**: Never remove it, template depends on it
3. **Script order matters**: jQuery must load before plugins
4. **Modular components**: Changes to nav/footer/bios affect multiple pages
5. **Use local server**: JavaScript fetch() requires HTTP protocol

### Important Patterns
- **Fetch-based loading**: Most content loaded dynamically via fetch()
- **Modal system**: Biographies use modal popups from bios.html
- **Data sources**: bios.html is source of truth for team data
- **Publications pipeline**: Python scraper → JSON → JavaScript renderer

---

## File Structure Reference

```
.github/
├── README.md                    ← You are here
├── copilot-instructions.md      ← Complete reference (detailed)
├── quick-reference.md           ← Fast lookup (practical)
└── architecture-diagram.md      ← Visual diagrams (conceptual)
```

---

## Document Maintenance

### When to Update These Documents

**copilot-instructions.md**:
- New pages added
- New JavaScript files created
- Architecture changes
- New dependencies added
- Major workflow changes

**quick-reference.md**:
- New common tasks emerge
- Patterns change
- Commands update
- New troubleshooting scenarios

**architecture-diagram.md**:
- Data flow changes
- New components added
- Relationships change
- System architecture evolves

### How to Update
1. Edit the relevant markdown file
2. Maintain consistent formatting
3. Update "Last Updated" date at bottom
4. Commit with descriptive message: `docs: update [file] for [reason]`

---

## Using This Documentation Effectively

### For AI Agents

**When generating code**:
1. Check `quick-reference.md` for existing patterns
2. Follow the patterns exactly
3. Verify script loading order from `quick-reference.md`
4. Test locally before committing

**When troubleshooting**:
1. Check `quick-reference.md` → "Troubleshooting Guide" first
2. Review relevant section in `copilot-instructions.md`
3. Check browser console for errors
4. Review `architecture-diagram.md` to understand data flow

**When making changes**:
1. Understand impact using `architecture-diagram.md`
2. Follow patterns from `copilot-instructions.md`
3. Use checklist from `quick-reference.md`
4. Test thoroughly before deploying

### For Developers

**Code review checklist**:
- [ ] Does it follow patterns in `copilot-instructions.md`?
- [ ] Is script loading order correct? (see `quick-reference.md`)
- [ ] Are modular components properly used?
- [ ] Does it match the architecture in `architecture-diagram.md`?
- [ ] Is it tested locally?

---

## Additional Resources

### Within Repository
- `README.md` (root) - Basic project info and setup
- `STRUCTURE_DOCUMENTATION.md` - Original detailed documentation
- `LICENSE.txt` - Template license (CCA 3.0)

### External Resources
- **Helios Template**: https://html5up.net/helios
- **jQuery Documentation**: https://jquery.com/
- **BeautifulSoup (Python)**: https://www.crummy.com/software/BeautifulSoup/

### Research Group
- **Institution**: Chalmers University of Technology
- **Focus**: Bioinformatics, AI, Cheminformatics
- **Topic**: Antibiotic Resistance Research

---

## Questions or Issues?

1. **Check documentation first**: Most answers are in these three files
2. **Check browser console**: JavaScript errors appear there
3. **Review existing code**: Look for similar implementations
4. **Test locally**: Use `python -m http.server`
5. **Check git history**: See how similar changes were made

---

## Document Metadata

**Created**: January 5, 2026  
**Last Updated**: January 5, 2026  
**Maintained by**: Repository collaborators  
**Purpose**: Guide AI agents in understanding and modifying codebase  
**Audience**: GitHub Copilot, other AI coding assistants, developers

**Documentation Version**: 1.0  
**Repository**: kristianssonlabofwonders  
**Owner**: StyrbjornKall
