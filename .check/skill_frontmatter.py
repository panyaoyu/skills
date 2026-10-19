import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

problems = []
for skill_dir in sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir()):
    name = skill_dir.name
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        problems.append(f"skills/{name}/ 缺少 SKILL.md")
        continue

    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        problems.append(f"skills/{name}/SKILL.md 缺少 frontmatter：文件应以 --- 开头，并以 --- 结束 frontmatter")
        continue

    frontmatter = {}
    for line in lines[1:lines.index("---", 1)]:
        key, _, value = line.partition(":")
        frontmatter[key.strip()] = value.strip()

    for key in ("name", "description"):
        if not frontmatter.get(key):
            problems.append(f"skills/{name}/SKILL.md 的 frontmatter 缺少 {key}")
    if frontmatter.get("name") and frontmatter["name"] != name:
        problems.append(f"skills/{name}/SKILL.md 的 name 应为 {name}，实际为 {frontmatter['name']}")

for problem in problems:
    print(problem)
sys.exit(1 if problems else 0)
