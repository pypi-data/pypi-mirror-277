from pydantic import BaseModel
from typing import Any, Optional, Callable, Dict


class Story(BaseModel):
    name: str
    func: Callable[[Any], Any]
    meta: Optional[Dict[str, Any]]
    parent: str
    kwargs: Optional[Dict[str, Any]]
