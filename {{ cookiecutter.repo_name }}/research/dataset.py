from pathlib import Path
from config import PROCESSED_DATA_DIR, RAW_DATA_DIR



input_path: Path = RAW_DATA_DIR / "dataset.csv"
output_path: Path = PROCESSED_DATA_DIR / "dataset.csv"

