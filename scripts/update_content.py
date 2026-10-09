import json
import os
from pathlib import Path

event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text(encoding='utf-8'))
issue = event['issue']
text = issue['body'].split('### 主页文字\n\n', 1)[1].strip()
content = {'text': text, 'updated_at': issue['updated_at']}
root = Path(__file__).resolve().parents[1]
(root / 'data/content.json').write_text(json.dumps(content, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f"Updated homepage from issue #{issue['number']}")
