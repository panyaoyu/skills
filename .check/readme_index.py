import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_LINE = re.compile(r"^- \[(?P<name>[^\]]+)\]\((?P<link>[^)]+)\): (?P<description>.+)$")

skills = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}

indexed = {}
for line in (ROOT / "README.md").read_text(encoding="utf-8").splitlines():
    match = INDEX_LINE.match(line)
    if match:
        indexed[match["name"]] = match["link"]

problems = []
for name in sorted(skills - indexed.keys()):
    problems.append(f"README.md 缺少技能 {name} 的索引行，格式：- [{name}](skills/{name}/SKILL.md): <description>")
for name in sorted(indexed.keys() - skills):
    problems.append(f"README.md 索引了不存在的技能：{name}")
for name in sorted(indexed.keys() & skills):
    if indexed[name] != f"skills/{name}/SKILL.md":
        problems.append(f"README.md 中 {name} 的链接应为 skills/{name}/SKILL.md，实际为 {indexed[name]}")

for problem in problems:
    print(problem)
sys.exit(1 if problems else 0)
