"""Minimal Aspen Plus COM helper: convert (.inp/.bkp/.apw/.apwz), run, export (.his/.rep)."""

import argparse
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path

import win32com.client as win32

HAPEXP_REPORT = 2
HAPEXP_INPUT = 4
HAPEXP_HISTORY = 13
SAVEAS_EXTS = {".bkp", ".apw", ".apwz"}
ALL_EXTS = SAVEAS_EXTS | {".inp"}


@contextmanager
def open_aspen(src: Path):
    src = src.resolve()
    if not src.exists():
        raise FileNotFoundError(f"Input file not found: {src}")
    with tempfile.TemporaryDirectory(prefix="aspen_ops_", ignore_cleanup_errors=True) as workdir:
        aspen = win32.Dispatch("Apwn.Document")
        try:
            aspen.InitFromFile2(str(src), True, 0, "", "", "", workdir, 1)
            aspen.Visible = False
            aspen.SuppressDialogs = 1
            yield aspen
        finally:
            try:
                aspen.Quit()
            except Exception:
                try:
                    aspen.Close()
                except Exception:
                    pass


def save_model(aspen, dst: Path):
    dst = dst.resolve()
    dst.parent.mkdir(parents=True, exist_ok=True)
    ext = dst.suffix.lower()
    if ext in SAVEAS_EXTS:
        aspen.SaveAs(str(dst), True)
    elif ext == ".inp":
        aspen.Export(HAPEXP_INPUT, str(dst))
    else:
        raise ValueError(f"Unsupported target format: {ext} (supported: {sorted(ALL_EXTS)})")
    if not dst.exists():
        raise RuntimeError(f"Failed to produce output file: {dst}")


def export_file(aspen, exp_type: int, dst: Path, label: str):
    dst = dst.resolve()
    dst.parent.mkdir(parents=True, exist_ok=True)
    aspen.Export(exp_type, str(dst))
    if not dst.exists() or dst.stat().st_size == 0:
        raise RuntimeError(f"Failed to export {label} (model may need --run first): {dst}")


def cmd_convert(args):
    with open_aspen(Path(args.src)) as aspen:
        save_model(aspen, Path(args.dst))
    print(f"OK: {args.src} -> {args.dst}")


def cmd_run(args):
    with open_aspen(Path(args.src)) as aspen:
        aspen.Engine.Run2()
        info_node = aspen.Tree.FindNode(r"\Data\Results Summary\Run-Status\Output\PER_ERROR")
        per_error = info_node.Value if info_node is not None else None
        if args.save:
            save_model(aspen, Path(args.save))
        if args.his:
            export_file(aspen, HAPEXP_HISTORY, Path(args.his), ".his")
        if args.rep:
            export_file(aspen, HAPEXP_REPORT, Path(args.rep), ".rep")
    print(f"RUN PER_ERROR={per_error}")


def cmd_export(args):
    if not args.his and not args.rep:
        raise ValueError("Specify at least one of --his or --rep")
    with open_aspen(Path(args.src)) as aspen:
        if args.run:
            aspen.Engine.Run2()
        if args.his:
            export_file(aspen, HAPEXP_HISTORY, Path(args.his), ".his")
        if args.rep:
            export_file(aspen, HAPEXP_REPORT, Path(args.rep), ".rep")
    outputs = [p for p in (args.his, args.rep) if p]
    print("OK: " + ", ".join(outputs))


def main():
    parser = argparse.ArgumentParser(description="Aspen Plus basic COM operations")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_conv = sub.add_parser("convert", help="Convert between .inp, .bkp, .apw, .apwz")
    p_conv.add_argument("src", help="Source file")
    p_conv.add_argument("dst", help="Target file")
    p_conv.set_defaults(func=cmd_convert)

    p_run = sub.add_parser("run", help="Run simulation and optionally save/export")
    p_run.add_argument("src", help="Source file (.inp/.bkp/.apw/.apwz)")
    p_run.add_argument("--save", help="Save result model to path (.inp/.bkp/.apw/.apwz)")
    p_run.add_argument("--his", help="Export .his history file to path")
    p_run.add_argument("--rep", help="Export .rep report file to path")
    p_run.set_defaults(func=cmd_run)

    p_exp = sub.add_parser("export", help="Export .his and/or .rep")
    p_exp.add_argument("src", help="Source file (.inp/.bkp/.apw/.apwz)")
    p_exp.add_argument("--his", help="Output .his path")
    p_exp.add_argument("--rep", help="Output .rep path")
    p_exp.add_argument("--run", action="store_true", help="Run simulation before exporting")
    p_exp.set_defaults(func=cmd_export)

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
