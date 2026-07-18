import re
import pathlib

root = pathlib.Path(r'd:\Thực Tập\FCAJ-workshop-trungthanh\content\1-Worklog')

# Update each week page weight based on its folder number
for folder in sorted(root.iterdir()):
    if not folder.is_dir():
        continue
    m = re.match(r'^1\.(\d+)-week(\d+)$', folder.name, re.IGNORECASE)
    if not m:
        continue
    week_num = int(m.group(2))
    for fname in ['_index.md', '_index.vi.md']:
        path = folder / fname
        if not path.exists():
            continue
        text = path.read_text(encoding='utf-8')
        text = re.sub(r'^(weight:\s*)(\S+)', rf'\g<1>{week_num}', text, count=1, flags=re.M)
        path.write_text(text, encoding='utf-8')

# Fix overview links to exact folder names
for fname in ['_index.md', '_index.vi.md']:
    path = root / fname
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    replacements = [
        ('1.1-week1/', '1.1-Week1/'),
        ('1.2-week2/', '1.2-Week2/'),
        ('1.3-week3/', '1.3-Week3/'),
        ('1.4-week4/', '1.4-Week4/'),
        ('1.5-week5/', '1.5-Week5/'),
        ('1.6-week6/', '1.6-Week6/'),
        ('1.7-week7/', '1.7-Week7/'),
        ('1.8-week8/', '1.8-Week8/'),
        ('1.9-week9/', '1.9-Week9/'),
        ('1.10-week10/', '1.10-Week10/'),
        ('1.11-week11/', '1.11-Week11/'),
        ('1.12-week12/', '1.12-Week12/'),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')

print('Updated worklog weights and links')
