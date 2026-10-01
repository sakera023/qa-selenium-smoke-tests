# QA Selenium Smoke Tests

This project contains deterministic browser smoke tests using Selenium WebDriver, Chrome, Pytest, and self-contained HTML fixtures.

## Features

- Login-page element checks
- Signup-form element checks
- Headless Chrome support
- Automated tests on Python 3.11 and 3.12

## Setup

Python 3.11 or newer and Google Chrome are required.

```bash
python -m pip install -r requirements.txt
```

## Run tests

```bash
pytest -q
```

The tests load local `data:` pages, so they do not depend on a live website or network connection.
