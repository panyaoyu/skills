"""仅准备被测输入；不运行模型，也不判定行为通过。只使用 Python 标准库。"""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def main():
    suite = json.loads((HERE / "cases.json").read_text(encoding="utf-8"))
    cases = {case["id"]: case for case in suite["cases"]}
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=sorted(cases))
    parser.add_argument("destination", type=Path, help="新的输入目录，必须尚不存在")
    parser.add_argument("--skill", type=Path, default=ROOT / "skills/read-paper/SKILL.md")
    args = parser.parse_args()
    case = cases[args.case]
    fixture = HERE / "fixtures" / case["fixture"]
    skill = args.skill.read_bytes()
    if args.destination.exists():
        parser.error("输入目录已存在；请使用新目录，避免混入旧输出或评分标准")

    args.destination.mkdir(parents=True)
    (args.destination / "SKILL.md").write_bytes(skill)
    shutil.copyfile(fixture / "paper.md", args.destination / "paper.md")
    shutil.copytree(fixture / "sources", args.destination / "sources")
    if "supplement" in case:
        shutil.copyfile(fixture / case["supplement"], args.destination / "supplement.md")
    (args.destination / "request.md").write_text(
        suite["common_request"] + "\n\n" + case["request_suffix"] + "\n",
        encoding="utf-8",
    )
    # 环境配置和版本信息交给执行者；不要作为提示词喂给被测模型。
    print(json.dumps({
        "case": args.case,
        "input_dir": str(args.destination.resolve()),
        "delegation": case["delegation"],
        "skill_sha256": hashlib.sha256(skill).hexdigest(),
        "status": "PREPARED_NOT_RUN",
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
