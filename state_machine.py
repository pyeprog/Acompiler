from abc import ABC


class State(ABC):
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def next(self, input):
        raise NotImplementedError("This method is not implemented")


class StateMachine:
    def __init__(self, start_state: str, **states: type):
        for state_name, state_cls in states.items():
            setattr(self, state_name, state_cls(self))
        self.state = self.__dict__[start_state]

    def run(self, input: str):
        self.state = self.state.next(input)
