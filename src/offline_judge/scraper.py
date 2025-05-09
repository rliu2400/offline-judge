import requests
from bs4 import BeautifulSoup
from pathlib import Path
from tqdm import tqdm
import zipfile, io

BASE_PAGE = "https://usaco.org/index.php?page=viewproblem2&cpid={}"
BASE_DATA = "https://usaco.org/current/data/{}"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"


def scrape_problem(cpid: int):
    out = DATA_DIR / f"problem-{cpid}"
    out.mkdir(parents=True, exist_ok=True)

    url = BASE_PAGE.format(cpid)
    print(f"Fetching {url}")
    resp = requests.get(url)
    resp.raise_for_status()
    html = resp.text

    # 1) write the raw HTML to disk
    (out / "page.html").write_text(html, encoding="utf-8")
    print(f"✓ Wrote raw HTML to {out/'page.html'}")


def scrape_contest(code: str, out_dir: str):
    # download zip
    zipname = f"prob1_platinum_{code}.zip"
    dest = Path(out_dir) / "contests" / code / zipname
    dest.parent.mkdir(parents=True, exist_ok=True)

    resp = requests.get(BASE_DATA.format(zipname), stream=True)
    resp.raise_for_status()

    total = int(resp.headers.get("Content-Length", 0))
    buf = io.BytesIO()
    for chunk in tqdm(resp.iter_content(1024), total=total // 1024, unit="KB"):
        buf.write(chunk)

    # save & unzip
    buf.seek(0)
    dest.write_bytes(buf.getvalue())
    with zipfile.ZipFile(buf) as z:
        z.extractall(dest.parent)
