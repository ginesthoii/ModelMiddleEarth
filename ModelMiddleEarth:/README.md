# Security

This repo treats 3D assets like code:
- Static analysis for Python tools/scripts with **Bandit**
- Minimal CI to keep Blender automation sane
- No remote code execution in scripts; everything is explicit

Run locally:
```bash
pip install -r requirements.txt
bandit -r blender



**`.github/workflows/ci.yml`**

```yaml
name: Security CI

on:
  push:
  pull_request:

jobs:
  bandit:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install tools
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Bandit scan
        run: bandit -r blender -lll