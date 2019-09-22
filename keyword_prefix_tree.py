from typing import Dict, List


class PrefixTreeNode:
    def __init__(self, val, is_terminal_node=False):
        self.val = val
        self.next = {}
        self.is_terminal_node = is_terminal_node

    def has(self, value):
        return value in self.next

    def next_node(self, key):
        if not self.has(key):
            raise ValueError("This node has no child of key {}".format(key))
        return self.next[key]

    def add_next(self, key, treenode):
        self.next[key] = treenode

    def is_matching(self, string) -> bool:
        if len(string) > 0:
            if len(string) > 1:
                return (
                    string[0] == self.val
                    and self.has(string[1])
                    and self.next_node(string[1]).is_matching(string[1:])
                )
            return string[0] == self.val and self.is_terminal_node
        return False


def make_prefix_tree(string: str, root: PrefixTreeNode = None) -> PrefixTreeNode:
    if len(string) == 0:
        raise ValueError("input string should not be empty")

    for i, char in enumerate(keyword):
        if i == 0:
            if root:
                if root.val != char:
                    raise ValueError("root char is not matching string {}".format(string))
            else:
                root = PrefixTreeNode(char, i == len(keyword) - 1)
            cur = root
        else:
            if not cur.has(char):
                next_node = PrefixTreeNode(char, i == len(keyword) - 1)
                cur.add_next(char, next_node)
            cur = cur.next_node(char)
    return root


def make_prefix_tree_from_list(strings: List[str]) -> Dict[str, PrefixTreeNode]:
    result = {}
    for string in strings:
        result[string[0]] = make_prefix_tree(string, result.get(string, None))
    return result


if __name__ == "__main__":
    keywords = {"EndsWith", "Exist"}

    root = {}
    for keyword in keywords:
        root[keyword] = make_prefix_tree(keyword)

    assert root["EndsWith"].is_matching("EndsWith")
    assert root["Exist"].is_matching("Exist")
    assert not root["Exist"].is_matching("Ex")
    assert not root["Exist"].is_matching("Exists")
