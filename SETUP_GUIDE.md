# Setup & Migration Guide

## What You're Getting

✅ **New main `index.html`** — Hero section + 7-app grid + services + footer  
✅ **apps.json** — All product data in one place  
✅ **generate_apps.py** — Auto-generates 7 individual app landing pages  
✅ **7 app folders** — `apps/secondly/`, `apps/katacopy/`, etc., each with its own `index.html`  
✅ **README_NEW_SITE.md** — Full documentation  

---

## Step 1: Replace Your Current Files

1. **Backup your current repo** (just in case)
   ```bash
   git branch backup-current
   ```

2. **Copy these files into your repo root**:
   - `index.html` ← NEW (replaces old one)
   - `apps.json` ← NEW
   - `generate_apps.py` ← NEW
   - Keep: `blog.html`, `blog.json`, `privacy.html`, `posts.json`, `CNAME`, `.gitignore`, etc.

3. **Copy the `apps/` folder** into your repo (has 7 subfolders with app landing pages)

4. **Keep these unchanged**:
   - `blog.html` and `blog.json` (your blog still works)
   - `privacy.html` (privacy policy)
   - `posts.json` (blog posts)
   - `generate_blog.py` (blog generator)
   - `CNAME` (your custom domain)
   - `LICENSE`, `.gitignore`, etc.

---

## Step 2: Commit & Push

```bash
# Stage all changes
git add .

# Commit
git commit -m "Rebuild website with data-driven app portal

- Add modular apps.json for all 7 products
- Create auto-generating Python script for app pages
- Redesign index.html with hero, app grid, and services section
- Add dedicated landing page for each app
- Maintain blog, privacy, and existing content"

# Push to main (site updates automatically)
git push origin main
```

Your site goes live in seconds. GitHub Actions auto-deploys.

---

## Step 3: Verify It Looks Good

Visit your site at **https://structuralsensei.cc**

You should see:
- ✅ New hero with blue gradient accent
- ✅ App grid with 7 cards (Secondly, KataCopy, etc.)
- ✅ Services section highlighting custom automation work
- ✅ Footer with links to YouTube, Upwork, Gumroad
- ✅ Responsive on mobile

Click one app card → should see a full landing page with features, FAQ, and "Get [App] — $X" button.

---

## How to Update Apps Later

### Scenario 1: Change an app's price or description

1. Edit `apps.json`:
   ```json
   {
     "id": "secondly",
     "name": "Secondly",
     "price": 12.00,  // ← Changed
     "description": "New description...", // ← Changed
     ...
   }
   ```

2. Regenerate pages:
   ```bash
   python generate_apps.py
   ```

3. Commit:
   ```bash
   git add apps.json apps/
   git commit -m "Update Secondly pricing and description"
   git push
   ```

### Scenario 2: Add a brand new app

1. Add entry to `apps.json`:
   ```json
   {
     "id": "new-app",
     "name": "New App",
     "tagline": "Short pitch",
     "description": "Longer description...",
     "price": 5.99,
     "currency": "USD",
     "gumroad": "https://wico.gumroad.com/l/...",
     "category": "utilities",
     "features": [...],
     "faq": [...]
   }
   ```

2. Regenerate:
   ```bash
   python generate_apps.py
   ```

3. **Edit `index.html`** manually to add a card in the apps grid:
   ```html
   <a href="/apps/new-app/" class="card-hover bg-gray-900 border border-gray-800 rounded-xl p-6 flex flex-col">
     <div class="w-12 h-12 rounded-lg bg-[COLOR] flex items-center justify-center mb-4">
       <span class="text-white font-bold">[EMOJI]</span>
     </div>
     <h3 class="text-xl font-bold text-white mb-2">New App</h3>
     <p class="text-gray-400 text-sm mb-4 flex-grow">Short pitch here.</p>
     <div class="flex items-center justify-between pt-4 border-t border-gray-800">
       <span class="text-blue-400 font-semibold">$5.99</span>
       <span class="text-gray-500 text-sm">→</span>
     </div>
   </a>
   ```

4. Commit:
   ```bash
   git add apps.json index.html apps/
   git commit -m "Add new app: New App"
   git push
   ```

---

## File Sizes & Performance

- **index.html**: ~15 KB (fast)
- **Each app page**: ~12 KB (fast)
- **apps.json**: ~5 KB (fast)
- **Total**: Everything is static HTML—no JavaScript, no databases, no external APIs

→ Site loads instantly, works offline, scales indefinitely.

---

## Troubleshooting

**Q: Pages aren't updating after I push**
- GitHub Pages caches for up to 5 minutes. Wait, then hard-refresh (`Ctrl+Shift+R` or `Cmd+Shift+R`).
- If still old, check that `git push` succeeded.

**Q: `python generate_apps.py` fails**
- Ensure you're in the repo directory: `cd /path/to/repo`
- Ensure Python 3 is installed: `python --version`
- Ensure `apps.json` is in the same folder as the script.

**Q: I accidentally deleted an app page folder**
- Run `python generate_apps.py` to regenerate all pages.

**Q: The blog still works, right?**
- Yes! `blog.html`, `posts.json`, and `generate_blog.py` are untouched.

---

## Next Steps (Optional)

1. **Add custom assets** to the `assets/` folder (images, videos, PDFs).
2. **Update the hero image** by adding a background image to the hero section.
3. **Add YouTube/demo videos** to individual app pages (embed in the hero or features section).
4. **Set up analytics** (add Google Analytics or similar to the `<head>`).
5. **Add a blog post** about one of your apps (use the existing `generate_blog.py`).

---

## Questions?

Check `README_NEW_SITE.md` for full documentation, or email: **wico.pydev@gmail.com**

---

**Congratulations!** Your website is now a production-grade app portal. 🚀
