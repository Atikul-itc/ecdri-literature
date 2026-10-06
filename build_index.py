import csv
import re
from pathlib import Path

import pymupdf
import pymupdf4llm

pdf_dir, txt_dir = Path("pdfs"), Path("text")
txt_dir.mkdir(exist_ok=True)
doi_re = re.compile(r"10\.\d{4,9}/[^\s\"<>]+", re.I)

rows = []
for pdf in sorted(pdf_dir.glob("*.pdf")):
    try:
        doc = pymupdf.open(pdf)
        md = pymupdf4llm.to_markdown(doc)
        first_pages = "".join(doc[i].get_text() for i in range(min(2, len(doc))))
        m = doi_re.search(first_pages)
        doi = m.group(0).rstrip(".,;)") if m else ""
        title = (doc.metadata or {}).get("title", "") or ""
        (txt_dir / f"{pdf.stem}.md").write_text(md, encoding="utf-8")
        rows.append({"file": pdf.name, "title": title, "doi": doi,
                     "pages": len(doc), "chars": len(md)})
    except Exception as e:
        rows.append({"file": pdf.name, "title": "", "doi": "",
                     "pages": 0, "chars": 0})
        print(f"Failed: {pdf.name} ({e})")

with open("index.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["file", "title", "doi", "pages", "chars"])
    w.writeheader()
    w.writerows(rows)

print(f"Processed {len(rows)} files")