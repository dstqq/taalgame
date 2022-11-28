import os
from dotenv import load_dotenv
from typing import Final
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
dotenv_path = os.path.join(BASE_DIR, 'misc.env')
load_dotenv(dotenv_path=dotenv_path)

class TgKeys:
    TOKEN: Final = os.getenv('TOKEN', 'define me!')
