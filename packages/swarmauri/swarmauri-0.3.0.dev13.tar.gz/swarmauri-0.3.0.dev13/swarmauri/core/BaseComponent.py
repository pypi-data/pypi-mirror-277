import hashlib
from uuid import uuid4
import inspect
from typing import Optional, List
from enum import Enum

class ResourceTypes(Enum):
    UNIVERSAL_BASE = 'BaseComponent'
    #AGENT_API = 'AgentAPI'
    AGENT = 'Agent'
    AGENT_FACTORY = 'AgentFactory'
    CHAIN = 'Chain'
    CHUNKER = 'Chunker'
    CONVERASTION = 'Conversation'
    DISTANCE = 'Distance'
    DOCUMENT_STORE = 'DocumentStore'
    DOCUMENT = 'Document'
    EXCEPTION = 'Exception'
    MESSAGE = 'Message'
    METRIC = 'Metric'
    MODEL = 'Model'
    PARSER = 'Parser'
    PROMPT = 'Prompt'
    STATE = 'State'
    SWARM = 'Swarm'
    #SWARM_API = 'SwarmAPI'
    TOOLKIT = 'Toolkit'
    TOOL = 'Tool'
    PARAMETER = 'Parameter'
    TRACE = 'Trace'
    UTIL = 'Util'
    VECTOR_STORE = 'VectorStore'
    VECTORIZER = 'Vectorizer'
    VECTOR = 'Vector'



class BaseComponent:
    version = "0.1.0"
    
    def __init__(self, id: Optional[str] = None, 
                 owner: Optional[str] = None, 
                 name: Optional[str] = "",
                 host: Optional[str] = None,
                 members: List[str] = [],
                 resource: Optional[str] = None):
        self._id = id or str(uuid4())
        self._owner = owner
        self._name = name
        self._class_name = self.__class__.__name__
        self._host = host
        self._members = members
        if not resource and self.__class__.__name__ != 'BaseComponent':
            raise ValueError('must explicitly define resource')
        self.resource = resource if resource else ResourceTypes.UNIVERSAL_BASE.value
        self._path = f"{self._host if self._host else ''}/{self._owner}/{self.resource}/{self._name}/{self._id}"
        self._class_hash = self._calculate_class_hash()

    @property
    def id(self):
        return self._id

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, str):
            raise ValueError("Owner must be a string.")
        self._owner = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def classname(self):
        return self._class_name

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        if not isinstance(value, str):
            raise ValueError("Host must be a string.")
        self._host = value

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, value: List[str]):
        if not isinstance(value, list):
            raise ValueError("Members must be a list of strings.")
        self._members = value

    @property
    def resource(self):
        return self._resource

    @resource.setter
    def resource(self, value):
        # Ensure value is string and valid ResourceType
        if not isinstance(value, str):
            raise ValueError("Resource must be a string.")
        if value not in ResourceTypes._value2member_map_:
            raise ValueError(f"Resource must be one of {[e.value for e in ResourceTypes]}.")
        self._resource = value
    
    @property
    def path(self):
        return self._path

    @property
    def is_remote(self):
        return bool(self._host)
    

    @classmethod
    def public_interfaces(cls):
        methods = []
        for attr_name in dir(cls):
            # Retrieve the attribute
            attr_value = getattr(cls, attr_name)
            # Check if it's callable or a property and not a private method
            if (callable(attr_value) and not attr_name.startswith("_")) or isinstance(attr_value, property):
                methods.append(attr_name)
        return methods

    @classmethod
    def is_method_registered(cls, method_name: str):
        """
        Checks if a public method with the given name is registered on the class.
        Args:
            method_name (str): The name of the method to check.
        Returns:
            bool: True if the method is registered, False otherwise.
        """
        return method_name in cls.public_interfaces()

    @classmethod
    def method_with_signature(cls, input_signature):
        """
        Checks if there is a method with the given signature available in the class.
        
        Args:
            input_signature (str): The string representation of the method signature to check.
        
        Returns:
            bool: True if a method with the input signature exists, False otherwise.
        """
        for method_name in cls.public_interfaces():
            method = getattr(cls, method_name)
            if callable(method):
                sig = str(inspect.signature(method))
                if sig == input_signature:
                    return True
        return False

    @classmethod
    def _calculate_class_hash(cls):
        sig_hash = hashlib.sha256()
        for attr_name in dir(cls):
            # Retrieve the attribute
            attr_value = getattr(cls, attr_name)
            if callable(attr_value) and not attr_name.startswith("_"):
                sig = inspect.signature(attr_value)
                sig_hash.update(str(sig).encode())
                print(sig_hash.hexdigest())
        return sig_hash.hexdigest()