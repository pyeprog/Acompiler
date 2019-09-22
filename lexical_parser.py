import re
from .state_machine import State, StateMachine
from .keyword_prefix_tree import make_prefix_tree_from_list

tokens = []
cur_token = ""


class LexicalParser(StateMachine):
    KEYWORDS = {
        "Truthy",
        "Falsy",
        "Is",
        "And",
        "Or",
        "Not",
        "In",
        "NotIn",
        "GtCompare",
        "GtEqCompare",
        "LtCompare",
        "LtEqCompare",
        "Exist",
        "Eq",
        "NotEq",
        "Lt",
        "LE",
        "Gt",
        "GE",
        "RegexMatch",
        "StartsWith",
        "EndsWith",
        "Contains",
        "StrEq",
    }



    def __init__(self, start_state: str, **states: type):
        super().__init__(start_state, **states)


class Token(State):
    def next(self, input: str):
        if re.match(r"[0-9a-zA-Z]", input[0]):
            global cur_token
            cur_token += input[0]
            return self
        tokens.append(cur_token)
        cur_token = ""
        return self.state_machine.idle


class Idle(State):
    def next(self, input: str):
        if re.match(r"[0-9a-zA-Z]", input[0]):
            global cur_token
            cur_token += input[0]
            return self.state_machine.token
        return self


if __name__ == "__main__":
    eg_str = "I am a happy old fox\n"
    parser = StateMachine(start_state="idle", idle=Idle, token=Token)
    for char in eg_str:
        parser.run(char)
    print(tokens)
