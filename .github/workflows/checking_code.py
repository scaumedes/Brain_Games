name: Python CI

on:
  - push
  - pull_request

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository code
        uses: actions/checkout@v2
      - name: Install dependencies
        run: |
          pip install poetry
          make install
      - name: Run linter
        run: |
          make lint
