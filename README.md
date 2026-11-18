# Pink Morsel Sales Visualiser

A Python Dash dashboard that plots sales over time and lets users filter by region.

## Features

- Interactive sales line chart using Plotly
- Region selection: All, North, East, South or West
- Data loaded from `processed_sales.csv`

## Technology

Python, Pandas, Dash and Plotly Express.

## Run locally

```bash
python -m venv .venv
# Activate the virtual environment for your operating system
pip install -r requirements.txt
python app.py
```

The application starts a local Dash development server. Check the console for its URL. Do not use the debug server for production deployment.

## Repository layout

- `app.py`: Dash layout and region-filtering callback
- `processed_sales.csv`: prepared input data
- `data/`: supporting data
- `requirements.txt`: environment dependencies
- `test_app.py`: currently contains a placeholder test, not meaningful test coverage

## Known limitations and next steps

- [ ] Replace the placeholder test with tests for the region-filtering callback.
- [ ] Add a screenshot of the dashboard.
- [ ] Explain data provenance and how `processed_sales.csv` was prepared.
- [ ] Review dependency versions and create a reproducible environment.
- [ ] Document any work based on a supplied starter exercise.

## Attribution

This repository began from a Quantium starter exercise. Clearly distinguish starter materials from original implementation when describing it on a CV.
