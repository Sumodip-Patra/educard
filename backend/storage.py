import json
import os
from typing import List, Optional
from backend.models import Deck, Material, Card

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DECKS_FILE = os.path.join(DATA_DIR, "decks.json")
MATERIALS_FILE = os.path.join(DATA_DIR, "materials.json")

def _ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def load_decks() -> List[Deck]:
    _ensure_data_dir()
    if not os.path.exists(DECKS_FILE):
        return []
    try:
        with open(DECKS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Deck(**item) for item in data]
    except Exception:
        return []

def save_decks(decks: List[Deck]):
    _ensure_data_dir()
    with open(DECKS_FILE, "w", encoding="utf-8") as f:
        json.dump([d.model_dump() for d in decks], f, indent=2, default=str)

def load_materials() -> List[Material]:
    _ensure_data_dir()
    if not os.path.exists(MATERIALS_FILE):
        return []
    try:
        with open(MATERIALS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Material(**item) for item in data]
    except Exception:
        return []

def save_materials(materials: List[Material]):
    _ensure_data_dir()
    with open(MATERIALS_FILE, "w", encoding="utf-8") as f:
        json.dump([m.model_dump() for m in materials], f, indent=2, default=str)
