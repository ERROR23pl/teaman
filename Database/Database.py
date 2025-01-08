from abc import ABC, abstractmethod

# Define an interface using an abstract base class
class Database(ABC):
    @abstractmethod
    def connect(self):
        """Method to make the animal speak."""
        pass

    @abstractmethod
    def move(self):
        """Method to move the animal."""
        pass