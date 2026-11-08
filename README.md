# SLIIT KandyUni Research Publications

Staff research publication portal for SLIIT Kandy University, powered by [OpenAlex](https://openalex.org).

## Pages

| Page | Description |
|------|-------------|
| `index.html` | Staff member list with publication stats |
| `member.html?id=<id>` | Individual staff member publications |
| `department.html` | Department of Computing — all publications |
| `bm-department.html` | Department of Business Management — all publications |
| `admin.html` | Admin panel (password protected) |

## Features

- 📚 Browse publications by staff member or department
- 📅 Filter by year range (From Year → To Year)
- 📄 Separate views for Journal articles and Conference papers
- 📤 Export in BibTeX, APA, IEEE, CSV formats
- 🔄 Auto-sync daily via GitHub Actions (12:40 AM Sri Lanka time)
- 🔒 Admin panel with GitHub token integration
- ⚡ localStorage caching (24h) for fast repeat visits

## Setup

1. Fork or clone this repository
2. Go to **Settings → Pages → Source: Deploy from branch (main, / root)**
3. Site will be live at `https://<username>.github.io/<repo>/`

## Adding Staff Members

1. Go to `admin.html` on your live site
2. Login with the admin password
3. Click **"Setup Token"** and enter:
   - Your GitHub repository (`username/repo-name`)
   - A GitHub Personal Access Token (with `repo` scope)
4. Use the **Add Staff Member** form — changes save automatically to GitHub

## Auto-Sync

GitHub Actions runs daily at **12:40 AM Sri Lanka time** to refresh:
- `works_count` — total publications
- `cited_by_count` — total citations
- `h_index` — h-index

Manual trigger: **Actions tab → Sync OpenAlex Publications → Run workflow**

## Data Files

| File | Description |
|------|-------------|
| `data/members.json` | Staff member list with OpenAlex IDs and stats |
| `data/sync_meta.json` | Last auto-sync timestamp |
| `.github/workflows/sync.yml` | GitHub Actions sync workflow |

## Tech Stack

- Pure HTML / CSS / JavaScript — no build step required
- [OpenAlex API](https://openalex.org) — free, open research data
- GitHub Pages — free hosting
- GitHub Actions — free scheduled sync
