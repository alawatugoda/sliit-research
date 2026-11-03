# SLIIT KandyUni Research Publications

Staff research publication portal powered by [OpenAlex](https://openalex.org).

## Features
- 📚 Browse staff publications with year filter
- 📤 Export in BibTeX, APA, MLA, IEEE
- 🔄 Auto-sync daily via GitHub Actions
- 🔒 Admin panel (password protected)
- 🔗 Shareable per-person links

## Setup

1. **Fork / clone** this repository
2. Go to **Settings → Pages → Source: Deploy from branch (main, /root)**
3. Your site will be live at `https://<username>.github.io/<repo>/`

## Adding staff members

1. Go to `<your-site>/admin.html`
2. Login with your admin password
3. Enter staff name + their OpenAlex ID (from `openalex.org/authors/Axxxxxxx`)
4. Click "Add Member & Sync"
5. Download the updated `members.json` and commit it to `data/members.json` in the repo

## Auto-sync

GitHub Actions runs `scripts/sync.py` daily at 2am UTC to refresh publication counts.
You can also trigger it manually from the **Actions** tab.

## Changing admin password

1. Generate SHA-256 hash of your new password:
   ```bash
   echo -n "yournewpassword" | sha256sum
   ```
2. Update the `PASS_HASH` constant in `admin.html`
3. Commit the change

## Tech stack
- Pure HTML/CSS/JS — no build step
- OpenAlex API (free, no key required)
- GitHub Pages (free hosting)
- GitHub Actions (free sync)
