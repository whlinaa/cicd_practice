# CI/CD Demo with GitHub Actions

This repository is a minimal Python demo for:

- **CI**: lint + test on every push and pull request to `main`
- **CD**: auto-deploy a small static page to **GitHub Pages** when code is pushed to `main`

## Project structure

```
.
├── .github/workflows/ci-cd.yml
├── scripts/generate_site.py
├── src/cicd_demo/calculator.py
├── tests/test_calculator.py
├── requirements.txt
└── requirements-dev.txt
```

## What the pipeline does

### CI job

1. Checks out code
2. Sets up Python 3.12
3. Installs dev dependencies
4. Runs lint: `ruff check .`
5. Runs tests: `pytest -q`

### CD job

Runs only on push to `main` after CI passes:

1. Generates a static site into `site/`
2. Uploads `site/` as GitHub Pages artifact
3. Deploys to GitHub Pages

## Local run

```bash
python -m pip install -r requirements-dev.txt
export PYTHONPATH=src
ruff check .
pytest -q
python scripts/generate_site.py
```

Open `site/index.html` to preview the generated deployment page.

## Enable GitHub Pages deployment

In GitHub repo settings:

1. Go to **Settings → Pages**
2. Under **Build and deployment**, choose **Source: GitHub Actions**

After this, every push to `main` will run CI and then deploy.

## Trigger the demo

```bash
git add .
git commit -m "Add GitHub Actions CI/CD demo"
git push origin main
```

Then check:

- **Actions** tab for workflow status
- **Pages** URL for deployment output
