# Deployment Guide

## Repository Setup

### 1. Profile README
1. Go to `https://github.com/new`
2. Repository name: **`raghunath485`** (must match your username)
3. Make it **public**
4. Click **Create repository**
5. Copy `README.md` to the root of this repo
6. Push to GitHub — your profile README will appear automatically

### 2. Portfolio Site
1. Create a new repo: **`raghunath485.github.io`**
2. Push the contents of `portfolio/docs/` to that repo
3. GitHub Pages will auto-build from the `gh-pages` branch
4. Or use the existing workflows (`.github/workflows/deploy-portfolio.yml`)

### 3. Project Template
```bash
git clone https://github.com/raghunath485/ml-project-template
cd ml-project-template
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows
pip install -r requirements.txt
python main.py
pytest
```

## GitHub Actions Workflows

| Workflow     | Trigger                        |
|--------------|--------------------------------|
| Python CI    | push/PR to main                |
| Code Quality | PR to main                     |
| Deploy Site  | push to gh-pages               |

## Custom Domain (Optional)
1. Buy a domain or use a free one
2. Create a `CNAME` file in `portfolio/docs/` with your domain
3. Add a CNAME record at your DNS provider pointing to `yourusername.github.io`
