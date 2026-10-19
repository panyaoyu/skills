# AGENTS.md

本仓库维护个人使用的全局指令和通用技能（skill）。

## 目录结构

- `README.md`：面向人的仓库说明，包括全局指令的安装位置和技能索引。
- `AGENTS-MD.md`：个人全局指令的源文件。使用时复制到 `~/.claude/CLAUDE.md`（Claude Code）或 `~/.codex/AGENTS.md`（Codex）。它不是本仓库的 AGENTS.md。
- `skills/`：所有技能，每个技能一个子目录，目录名即技能名。
  - `SKILL.md`：技能入口，frontmatter 中的 `name` 和 `description` 决定技能何时被调用。
  - `references/`：可选，由 `SKILL.md` 按需指向的参考资料。

## README 技能索引

`README.md` 中每个技能占一个列表项，格式为：

```markdown
- [<skill-name>](skills/<skill-name>/SKILL.md): <description>
```

- 技能名必须链接到该技能的 `SKILL.md`。
- 新增、重命名或删除技能时，同步更新此索引。

## 提交格式

主题行格式为 `<前缀>: <改动概要>`，用中文。对于前缀，改技能用技能名，改 `AGENTS-MD.md` 用 `agents-md`，改仓库其他内容（README、AGENTS.md）用 `repo`。

正文写两段：

- 原因：为什么需要这次改动。
- 内容：改了什么。按规则或功能概括，不逐行复述 diff。
