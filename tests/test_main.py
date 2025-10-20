from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from main import main


def test_main_returns_none():
    assert main() is None


def test_placeholder_lines_present():
    main_file = Path(__file__).resolve().parents[1] / "src" / "main.py"
    content = main_file.read_text(encoding="utf-8")

    assert "# ----- Espacio para programar -----" in content
    for number in range(1, 11):
        assert f"# {number}." in content
