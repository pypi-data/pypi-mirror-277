from typing import Optional, Union, List
from swarmauri.core.messages.IMessage import IMessage
from swarmauri.core.conversations.IMaxSize import IMaxSize
from swarmauri.standard.conversations.base.SystemContextBase import SystemContextBase
from swarmauri.standard.messages.concrete import SystemMessage, AgentMessage, HumanMessage
from swarmauri.standard.exceptions.concrete import IndexErrorWithContext

class MaxSystemContextConversation(SystemContextBase, IMaxSize):
    def __init__(self, max_size: int, system_message_content: Optional[SystemMessage] = None):
        """
        Initializes the conversation with a system context message and a maximum history size.
        
        Parameters:
            max_size (int): The maximum number of messages allowed in the conversation history.
            system_message_content (Optional[str], optional): The initial system message content. Can be a string.
        """
        SystemContextBase.__init__(self, system_message_content=system_message_content if system_message_content else "")  # Initialize SystemContext with a SystemMessage
        self._max_size = max_size  # Set the maximum size
    
    @property
    def history(self) -> List[IMessage]:
        """
        Get the conversation history, ensuring it starts with a 'user' message and alternates correctly between 'user' and 'assistant' roles.
        The maximum number of messages returned does not exceed max_size + 1.
        """
        res = []  # Start with an empty list to build the proper history

        # Attempt to find the first 'user' message in the history.
        user_start_index = -1
        for index, message in enumerate(self._history):
            if isinstance(message, HumanMessage):  # Identify user message
                user_start_index = index
                break

        # If no 'user' message is found, just return the system context.
        if user_start_index == -1:
            return [self.system_context]

        # Build history from the first 'user' message ensuring alternating roles.
        res.append(self.system_context)
        alternating = True
        count = 0 
        for message in self._history[user_start_index:]:
            if count >= self._max_size: # max size
                break
            if alternating and isinstance(message, HumanMessage) or not alternating and isinstance(message, AgentMessage):
                res.append(message)
                alternating = not alternating
                count += 1
            elif not alternating and isinstance(message, HumanMessage):
                # If we find two 'user' messages in a row when expecting an 'assistant' message, we skip this 'user' message.
                continue
            else:
                # If there is no valid alternate message to append, break the loop
                break

        return res
        
    @property
    def max_size(self) -> int:
        """
        Provides access to the max_size property.
        """
        return self._max_size
    
    @max_size.setter
    def max_size(self, new_max_size: int) -> None:
        """
        Sets a new maximum size for the conversation history.
        """
        if new_max_size <= 0:
            raise ValueError("max_size must be greater than 0.")
        self._max_size = new_max_size

    def add_message(self, message: IMessage):
        """
        Adds a message to the conversation history and ensures history does not exceed the max size.
        """
        if isinstance(message, SystemMessage):
            raise ValueError(f"System context cannot be set through this method on {self.__class_name__}.")
        else:
            super().add_message(message)
        self._enforce_max_size_limit()
        
    def _enforce_max_size_limit(self):
        """
        Remove messages from the beginning of the conversation history if the limit is exceeded.
        We add one to max_size to account for the system context message
        """
        try:
            while len(self._history) > self._max_size + 1:
                self._history.pop(0)
                self._history.pop(0)
        except IndexError as e:
            raise IndexErrorWithContext(e)


    @property
    def system_context(self) -> Union[SystemMessage, None]:
        """Get the system context message. Raises an error if it's not set."""
        if self._system_context is None:
            raise ValueError("System context has not been set.")
        return self._system_context


    @system_context.setter
    def system_context(self, new_system_message: Union[SystemMessage, str]) -> None:
        """
        Set a new system context message. The new system message can be a string or 
        an instance of SystemMessage. If it's a string, it converts it to a SystemMessage.
        """
        if isinstance(new_system_message, SystemMessage):
            self._system_context = new_system_message
        elif isinstance(new_system_message, str):
            self._system_context = SystemMessage(new_system_message)
        else:
            raise ValueError("System context must be a string or a SystemMessage instance.")
            