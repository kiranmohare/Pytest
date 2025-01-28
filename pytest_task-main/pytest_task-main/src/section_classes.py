import logging
import random

LOGGER = logging.getLogger(__name__)

class Animal:
    def __init__(self, name: str):
        self.name = name
        LOGGER.info("Initialized Animal")

    def make_sound(self) -> str:
        LOGGER.info("Making Animal sound")
        return "Any sound!"

    def make_move(self):
        raise NotImplementedError()

class Dog(Animal):
    def bark(self) -> str:
        LOGGER.info("Making Dog sound")
        return "A dog sound!"

    def run(self) -> str:
        LOGGER.info("Dog running")
        return "Running!"
    
    def make_move(self):
        LOGGER.info("Dog making move")
        return "Running!"
    
    def make_sound(self):
        LOGGER.info("Making Dog sound")
        return "A dog sound!"

class Cat(Animal):
    _hungry = None

    @property
    def hungry(self) -> bool:
        if self._hungry is None:
            self._hungry = random.choice([True, False])
            LOGGER.debug("Cat is hunge=%s", self._hungry)
        return self._hungry

class Horse(Animal):
    """horse class"""
    # TASK: add implementation here
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height
        LOGGER.info(f"Initialized Horse with name={name} and height={height}")

    def stand(self) -> str:
        LOGGER.info(f"{self.name} is standing")
        return "Standing!"