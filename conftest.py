import sys
from pathlib import Path

# Добавляем папку src в sys.path, чтобы Python видел модули из src
src_path = Path(__file__).resolve().parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))
