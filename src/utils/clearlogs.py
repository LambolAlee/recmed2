from pathlib import Path
from os import remove



logDir = Path(__file__).parent.parent.parent / "logs"

try:
    for file in logDir.glob("*.log"):
        remove(file)
except Exception as e:
    print(e)
