# 个人智能体配置

维护个人在学术研究、软件工程和日常工作中使用的全局指令和通用技能，沉淀可复用的方法与工作流程。

## 全局指令（AGENTS.md / CLAUDE.md）

我给智能体设置的符合我个人使用习惯的全局指令。使用的时候需要把 `AGENTS-MD.md` 复制到指定的位置。

| 智能体 | 全局指令文件 |
| --- | --- |
| Claude Code | `~/.claude/CLAUDE.md` |
| Codex | `~/.codex/AGENTS.md` |

## 技能

### 支持的技能

所有技能都位于 `skills/` 目录。可以使用的skills如下所示。

- [read-paper](skills/read-paper/SKILL.md): 从领域研究者的角度阅读论文，对照领域基线区分论文的声称贡献和实际贡献。
- [feasibility-experiment](skills/feasibility-experiment/SKILL.md): 用最小、隔离的实验验证技术可行性，保留可复查的过程与证据。

