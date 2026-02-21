from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Union
from datetime import date
from enum import Enum
import random

app = FastAPI

class WheelColor(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"