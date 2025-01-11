USACO Offline Judge.

Only doing USACO problems because sample test cases and correct output are readily available online, unlike codeforces.

Future plans:
- codeforces
- virtual contests
- add to homebrew

Project Structure:
offline-judge/
│── bin/
│   └── oj              # CLI entry point (executable script)
│── libexec/
│   ├── oj.py           # Main Python script handling CLI logic
│   ├── commands/
│   │   ├── __init__.py  # Makes the folder a package
│   │   ├── scrape.py    # Handles `oj scrape`
│   │   ├── submit.py    # Handles `oj submit`
│   ├── utils/
│   │   ├── __init__.py  # Utility package
│   │   ├── scraper.py   # Handles problem/test case scraping
│   │   ├── executor.py  # Handles C++ compilation & execution
│── problems/           # Stores scraped problems/test cases
│── submissions/        # Stores user submissions
│── config.json         # Configuration settings (if needed)
│── README.md           # Documentation
│── LICENSE             # License file
│── requirements.txt    # Python dependencies (if using Python)

