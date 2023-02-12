"""Class to parse the output of an LLM call."""
from abc import ABC, abstractmethod
from typing import Any, Dict, List

from pydantic import BaseModel


class BaseOutputParser(BaseModel, ABC):
    """Class to parse the output of an LLM call."""

    @abstractmethod
    def parse(self, text: str) -> Any:
        """Parse the output of an LLM call."""

    @property
    def _type(self) -> str:
        """Return the type key."""
        raise NotImplementedError

    def dict(self, **kwargs: Any) -> Dict:
        """Return dictionary representation of output parser."""
        output_parser_dict = super().dict()
        output_parser_dict["_type"] = self._type
        return output_parser_dict


class ListOutputParser(BaseOutputParser):
    """Class to parse the output of an LLM call to a list."""

    @abstractmethod
    def parse(self, text: str) -> List[str]:
        """Parse the output of an LLM call."""
