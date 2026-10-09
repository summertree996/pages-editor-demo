import html
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
content = json.loads((root / 'data/content.json').read_text(encoding='utf-8'))
template = (root / 'template.html').read_text(encoding='utf-8')
page = template.replace('<!-- CONTENT -->', html.escape(content['text']))
page = page.replace('<!-- UPDATED -->', html.escape(content['updated_at'] or '初始版本'))
destination = root / 'dist'
destination.mkdir(exist_ok=True)
(destination / 'index.html').write_text(page, encoding='utf-8')
print('Built dist/index.html')
