# Structural Sensei Website Rebuild

A modern, data-driven website showcasing 7+ production apps and professional services. Built with clean architecture for easy scaling.

## 📁 New Structure

```
.
├── index.html              # Main landing page with hero + app grid
├── apps.json              # Single source of truth (all app data)
├── generate_apps.py       # Python script to auto-generate app pages
├── apps/
│   ├── secondly/
│   │   └── index.html
│   ├── katacopy/
│   │   └── index.html
│   ├── image-to-icon/
│   │   └── index.html
│   └── ...                # (7 total app folders)
├── blog.html              # Blog page (unchanged)
├── privacy.html           # Privacy policy (unchanged)
└── posts.json             # Blog posts (unchanged)
```

## 🎯 Key Features

- **Data-Driven Design**: All app data lives in `apps.json`
- **Auto-Generated Pages**: Run `python generate_apps.py` to update all app pages
- **Unified Branding**: Consistent dark theme with blue accents
- **SEO-Ready**: Meta tags, proper structure, Open Graph support
- **Responsive**: Mobile-first Tailwind CSS (no external assets)
- **CTA Optimization**: Direct Gumroad links on every page

## 📱 Adding a New App

1. **Add entry to `apps.json`**:
   ```json
   {
     "id": "app-slug",
     "name": "App Name",
     "tagline": "Short value prop",
     "description": "Longer description...",
     "price": 9.99,
     "currency": "USD",
     "gumroad": "https://wico.gumroad.com/l/...",
     "category": "utilities",
     "features": [
       "Feature 1",
       "Feature 2"
     ],
     "faq": [
       { "q": "Question?", "a": "Answer." }
     ]
   }
   ```

2. **Regenerate pages**:
   ```bash
   python generate_apps.py
   ```

3. **Update `index.html`** manually to add a card in the grid (copy/paste and modify one of the existing app cards).

4. **Commit and push**:
   ```bash
   git add apps.json index.html apps/
   git commit -m "Add new app: App Name"
   git push
   ```

## ✏️ Updating an App

Change the app's entry in `apps.json` (name, price, description, features, FAQ) and regenerate:

```bash
python generate_apps.py
```

This rebuilds all app pages with the new data, keeping design consistent.

## 🎨 Customizing Design

All styling is in the `<style>` blocks of `index.html` and the generated app pages. Common changes:

- **Colors**: Edit `--accent: #3b82f6` (blue) in the `:root` block
- **Spacing/Padding**: Modify Tailwind classes (`py-20`, `px-8`, etc.)
- **Fonts**: Adjust text sizes (`text-4xl`, `text-xl`) or add a custom font in the `<head>`

## 🚀 Deployment

Your site is already deployed via GitHub Pages. To update:

1. Edit `apps.json`, `index.html`, or other files locally
2. Run `python generate_apps.py` to regenerate app pages
3. Commit changes:
   ```bash
   git add .
   git commit -m "Update site: [description]"
   git push origin main
   ```
4. Changes go live automatically (usually within seconds)

## 📊 What Changed from Old Site

| Old | New |
|-----|-----|
| Single landing page | Hero + apps grid + services section |
| No dedicated app pages | 7 individual app landing pages |
| Manual updates | `apps.json` + auto-generation |
| Limited metadata | Full SEO, Open Graph, schema |
| Links scattered | Unified Gumroad CTAs |

## 🔧 Running Locally

```bash
# Generate pages
python generate_apps.py

# Start a local server (Python 3)
python -m http.server 8000

# Open in browser
# http://localhost:8000
```

## 📧 Contact & Support

- **Email**: wico.pydev@gmail.com
- **Upwork**: https://www.upwork.com/freelancers/~018dd551fe9dd4aa2a
- **Gumroad**: https://wico.gumroad.com

## 📝 Notes

- The `generate_apps.py` script is production-ready—run it before every commit to keep pages in sync.
- Each app page includes a FAQ section, feature list, and direct Gumroad checkout link.
- All pages are static HTML (no JavaScript dependencies) for fast, reliable performance.

---

**Built with Tailwind CSS • Deployed on GitHub Pages • Last updated: 2026**
