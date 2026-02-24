from datetime import datetime, timezone
from pathlib import Path

from cicd_demo.calculator import add, multiply


def build_html() -> str:
    build_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    sample_sum = add(20, 22)
    sample_product = multiply(6, 7)

    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>GitHub Actions CI/CD Demo</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif; margin: 2rem; line-height: 1.5; }}
    .card {{ max-width: 700px; border: 1px solid #ddd; border-radius: 8px; padding: 1rem 1.25rem; }}
    code {{ background: #f4f4f4; padding: 0.15rem 0.3rem; border-radius: 4px; }}
  </style>
</head>
<body>
  <div class=\"card\">
    <h1>CI/CD Demo deployed by GitHub Actions</h1>
    <p>This page is generated during the <strong>CD</strong> job.</p>
    <p>testing</p>
    <ul>
      <li>Build time: <code>{build_time}</code></li>
      <li>Sample calculation: <code>20 + 22 = {sample_sum}</code></li>
      <li>Sample calculation: <code>6 × 7 = {sample_product}</code></li>
    </ul>
  </div>
</body>
</html>
"""


def main() -> None:
    site_dir = Path("site")
    site_dir.mkdir(exist_ok=True)
    (site_dir / "index.html").write_text(build_html(), encoding="utf-8")
    print("Generated site/index.html")


if __name__ == "__main__":
    main()
