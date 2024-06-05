from abc import ABC, abstractmethod
from typing import List, Union

class IParameter(ABC):
    """
    An abstract class to represent a parameter for a tool.
    """

    @property
    @abstractmethod
    def type(self) -> str:
        """
        Abstract property for getting the type of the parameter.
        """
        pass

    @type.setter
    @abstractmethod
    def type(self, value: str) -> None:
        """
        Abstract setter for setting the type of the parameter.
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Abstract property for getting the description of the parameter.
        """
        pass

    @description.setter
    @abstractmethod
    def description(self, value: str) -> None:
        """
        Abstract setter for setting the description of the parameter.
        """
        pass

    @property
    @abstractmethod
    def required(self) -> bool:
        """
        Abstract property for getting the required status of the parameter.
        """
        pass

    @required.setter
    @abstractmethod
    def required(self, value: bool)  -> None:
        """
        Abstract setter for setting the required status of the parameter.
        """
        pass

    @property
    @abstractmethod
    def enum(self) -> Union[List[str], None]:
        """
        Abstract property for getting the enum list of the parameter.
        """
        pass

    @enum.setter
    @abstractmethod
    def enum(self, value: List[str]) -> None:
        """
        Abstract setter for setting the enum list of the parameter.
        """
        pass