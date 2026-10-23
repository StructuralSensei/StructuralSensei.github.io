# Demo GIF Setup Guide

Each app landing page now has a **"See It in Action"** section with a demo GIF placeholder. This guide shows you how to capture demo videos and add them to your site.

---

## Step 1: Download ScreenToGif

1. **Visit**: https://www.screentogif.com/
2. **Download** the Windows version (it's free)
3. **Install** and launch the app

---

## Step 2: Record Your Demo

### For Each App:

1. **Open ScreenToGif** → Click "Recorder"
2. **Position the window** to show your app in action
3. **Click "Record"** (red button)
4. **Demonstrate the key features** (15-30 seconds is ideal)
   - **Secondly**: Show opening timer, selecting preset, alert triggering
   - **KataCopy**: Show opening, selecting files, transfer progress
   - **Image to Icon**: Show opening, selecting image, converting, result
   - etc.
5. **Click "Stop"** when done

### Recording Tips:
- Keep it **short**: 15-30 seconds max
- Show **one workflow** per GIF
- **Highlight the main feature** (not every button)
- **Use cursor movements** to guide viewer's attention
- Keep **UI clear and readable** (not too small)

---

## Step 3: Export as GIF

1. In ScreenToGif, after recording, click **"Edit"** (optional, for trimming)
2. Click **"File"** → **"Export"** → **"Gif"**
3. **Choose settings**:
   - Width: `1200` (or leave default)
   - Height: Auto (maintains aspect ratio)
   - Frames per second: `10-15` (slower = smaller file)
   - Quality: `High`
4. **Save as**: `{app-name}-demo.gif` (e.g., `secondly-demo.gif`)

**File size target**: 2-5 MB (keep it reasonable)

---

## Step 4: Add GIF to Your Website

### Option A: Simple (Recommended First Time)

1. **Copy your GIF** to your computer
2. **Open your repo** on GitHub
3. **Create folder**: `assets/` (if not exists)
4. **Upload files** → `assets/` folder
   - `secondly-demo.gif`
   - `katacopy-demo.gif`
   - etc.
5. **Edit `apps.json`**:
   ```json
   {
     "id": "secondly",
     ...
     "demo_gif": "/assets/secondly-demo.gif"  // ← Add this line
   }
   ```
6. **Regenerate**:
   ```bash
   python generate_apps.py
   ```
7. **Commit and push**:
   ```bash
   git add assets/ apps.json apps/
   git commit -m "Add demo GIFs for apps"
   git push
   ```

### Option B: Direct GitHub Upload

1. Go to your GitHub repo: `https://github.com/StructuralSensei/StructuralSensei.github.io`
2. Click **"Add file"** → **"Upload files"**
3. **Create a new folder first**:
   - Click "Add file" → "Create new file"
   - Type: `assets/.gitkeep`
   - Commit this
4. Then upload GIFs into `assets/` folder
5. Update `apps.json` with paths
6. Run `python generate_apps.py`
7. Commit changes

---

## Step 5: Verify on Your Site

1. **Wait 10 seconds** for GitHub Pages to update
2. **Visit**: `https://structuralsensei.cc/apps/secondly/`
3. **Scroll down** to "See It in Action"
4. **Your GIF should appear** in the demo section
5. **Test all app pages** to confirm GIFs load

---

## What Each App Should Show

| App | Demo Content | Duration |
|-----|--------------|----------|
| **Secondly** | Open app → Set timer → Show alert triggering | 20s |
| **KataCopy** | Open app → Select files → Show transfer progress | 15s |
| **Image to Icon** | Open app → Select image → Show conversion result | 15s |
| **Black Belt Budget** | Preview of document/guide (or skip GIF) | N/A |
| **Efficiency Memo** | Preview of document/guide (or skip GIF) | N/A |
| **Junior to Sensei** | Preview of document/guide (or skip GIF) | N/A |
| **Mastering Notion** | Notion workspace walkthrough | 20s |

---

## Current GIF Status in apps.json

| App | GIF Added | Path |
|-----|-----------|------|
| ✅ Secondly | Yes | `/assets/secondly-demo.gif` |
| ✅ KataCopy | Yes | `/assets/katacopy-demo.gif` |
| ❌ Black Belt Budget | No | (Empty - document, skip GIF) |
| ❌ Efficiency Memo | No | (Empty - document, skip GIF) |
| ❌ Junior to Sensei | No | (Empty - document, skip GIF) |
| ✅ Mastering Notion | Yes (optional) | `/assets/mastering-notion-demo.gif` |
| ✅ Image to Icon | Yes | `/assets/image-to-icon-demo.gif` |

---

## Placeholder Behavior

If a GIF is **not added** to `apps.json` (empty string or no path):

The page shows this placeholder instead:
```
┌─────────────────────────────────┐
│  Demo video coming soon         │
│  Use ScreenToGif to create...   │
│  [file size/dimensions info]    │
└─────────────────────────────────┘
```

This tells users the feature exists but GIF is pending. **You can fill these in later.**

---

## Editing an Existing GIF

If you want to re-record or update a GIF:

1. **Record new demo** with ScreenToGif
2. **Export as GIF** with same filename (overwrites old one)
3. **Upload to GitHub** (replace existing file)
4. **Hard-refresh** your site (`Ctrl+Shift+R`) to clear cache

---

## GIF Optimization Tips

If your GIF is too large (>5 MB):

1. **Trim the recording**: Remove dead time at start/end
2. **Lower FPS**: Use 8-10 instead of 15
3. **Reduce resolution**: Export at 1000x600 instead of 1200x675
4. **Use a GIF compressor**:
   - Online: https://ezgif.com/
   - Desktop: GIF Compressor (Windows Store)

Target: **2-4 MB per GIF** for fast loading.

---

## Rollout Plan (Recommended)

### Week 1: Add Desktop Apps
- [ ] Secondly GIF
- [ ] KataCopy GIF
- [ ] Image to Icon GIF

### Week 2: Add Optional GIFs
- [ ] Mastering Notion GIF (optional)

### Later: Skip for Documents
- [ ] Black Belt Budget (document—no GIF needed)
- [ ] Efficiency Memo (document—no GIF needed)
- [ ] Junior to Sensei (document—no GIF needed)

---

## Example `apps.json` Entry with GIF

```json
{
  "id": "secondly",
  "name": "Secondly",
  "tagline": "Time management redefined",
  "description": "A smart pomodoro timer...",
  "price": 10.00,
  "currency": "USD",
  "gumroad": "https://wico.gumroad.com/l/secondly",
  "category": "productivity",
  "demo_gif": "/assets/secondly-demo.gif",  // ← This path
  "features": [...],
  "faq": [...]
}
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| GIF not showing | Check path in `apps.json` matches actual filename (case-sensitive) |
| Placeholder still showing | Regenerate: `python generate_apps.py` and refresh browser |
| GIF too large/slow | Compress with ezgif.com or lower FPS |
| Can't see GIF in browser | Hard-refresh: `Ctrl+Shift+R` |
| File upload fails on GitHub | Use GitHub's web UI or drag-and-drop into `assets/` folder |

---

## Questions?

- **ScreenToGif help**: https://www.screentogif.com/
- **GIF compression**: https://ezgif.com/
- **GitHub file upload**: Right-click your repo → "Upload files"

---

**Pro Tip**: Once you have 2-3 GIFs up and running, the power of visual demos will show in your traffic. Users prefer to *see* your app working before buying. 🎬

Good luck! 🚀
