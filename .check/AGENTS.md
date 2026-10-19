## 每个检查脚本的作用

- [skill_frontmatter.py](skill_frontmatter.py)：检查每个技能目录都有 `SKILL.md`，且其 frontmatter 含非空的 `name` 和 `description`，`name` 与目录名一致。
- [readme_index.py](readme_index.py)：检查 `README.md` 的技能索引与 `skills/` 下的技能一一对应，且每个技能名都链接到对应的 `SKILL.md`。

## 检查脚本相关

当修改检查脚本时，需要同步修改 `.github/workflows/check.yml`。同时检查 `.git/hooks/` 的脚本，如果存在相关的检查也要一起修改。