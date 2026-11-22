---
name: aspen-basis
description: Aspen Plus 基础文件操作：转换 .inp/.bkp/.apw/.apwz 格式、运行模拟、导出 .his/.rep 报告。
---

`convert`、`run`、`export` 一律直接在宿主机上执行，跳过沙盒试运行，否则会有许可证问题。

使用 [scripts/aspen_ops.py](scripts/aspen_ops.py)（依赖 `pywin32`）：

```bash
python scripts/aspen_ops.py convert <src> <dst>
python scripts/aspen_ops.py run <src> [--save <dst>] [--his <out.his>] [--rep <out.rep>]
python scripts/aspen_ops.py export <src> [--his <out.his>] [--rep <out.rep>] [--run]
```

其他 Aspen Plus COM 接口与枚举常量查 [references/aspen_com_api.txt](references/aspen_com_api.txt)。
