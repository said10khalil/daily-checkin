name: Daily Checkin
on:
  schedule:
    - cron: '55 5 * * 0,1,2,3,6'
  workflow_dispatch:
jobs:
  checkin:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install playwright && playwright install chromium
      - run: python checkin.py
        env:
          EMAIL: ${{ secrets.EMAIL }}
          PASSWORD: ${{ secrets.PASSWORD }}
