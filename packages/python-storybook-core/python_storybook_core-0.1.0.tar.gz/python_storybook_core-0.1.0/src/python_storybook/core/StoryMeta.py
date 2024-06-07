from pydantic import BaseModel
from typing import Optional,  Dict

class StoryMeta(BaseModel):
    title: str
    name: str
    func_name: str
    docs: Optional[str]
    type_hints: Optional[Dict[str, str]]
    result: Optional[str] = None
