#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        return self.size == 0

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""

        result, _ = self._find_node(string)
        # result is a tuple thats why check
        # if the first item is None. Tuple itself cannot be None
        if result is not None:
            return True
        return False

    def insert(self, string):
        """Insert the given string into this prefix tree."""
# Drew's code
        if self.contains(string):
             return
        # # Insert string into tree
        curr_node = self.root
        for indx, char in enumerate(string):
            # if char DNE in tree, increase size

            # Traverse to next child in char is alread in string
            if curr_node.has_child(char):
                curr_node = curr_node.get_child(char)

            # Otherwise, add the child
            else:
                curr_node.add_child(char, PrefixTreeNode(char))
                curr_node = curr_node.get_child(char)

            # Change last node in str to terminal
            if indx == len(string) - 1:
                curr_node.terminal = True
                self.size += 1

    def _find_node(self, string):
        """Return a tuple containing the node that terminates the given string
        in this prefix tree and the node's depth, or if the given string is not
        completely found, return None and the depth of the last matching node.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:
            return self.root, 0

        # Start with the root node
        current_node = self.root

        for index, char in enumerate(string):
            if current_node.has_child(char):
                current_node = current_node.get_child(char)
                # return current_node, index + 1 # this line is fixing completions in tongue-twisters but not in the test
            else:
                return None, index + 1

        # if the last char is terminal
        if current_node.terminal is True:
            # print("current node is terminal", current_node)
            return current_node, index + 1
        else:
            return None, index + 1

    def _find_prefix_node(self, string):
        """Return a tuple containing the node that terminates the given string
        in this prefix tree and the node's depth, or if the given string is not
        completely found, return None and the depth of the last matching node.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:
            return self.root

        # Start with the root node
        current_node = self.root

        for index, char in enumerate(string):
            if current_node.has_child(char):
                current_node = current_node.get_child(char)
                # return current_node, index + 1 # this line is fixing completions in tongue-twisters but not in the test
            else:
                return None

        return current_node

    def complete(self, prefix=''):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        # TODO; debug this method and update Anisha, another project
        completions = []

        # base case - prefix is a finished string
        # if self._find_node(prefix) is True:
        #     completions.append(prefix)

        current_node = self._find_prefix_node(prefix)

        if current_node == None:
            # print("Current node", current_node)  # this is printing None
            return completions

        if not self.is_empty():
           self._traverse(current_node, prefix, completions.append)
        #    print("current node after traverse", current_node)

        return completions

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        # all_strings = []
        return self.complete()

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node and visit each node with the given function."""

        if node.terminal:
            visit(prefix)

        for char, child in node.children.items():
            # print(f"char {char} and child {child}")
            self._traverse(child, prefix + char, visit)
            # print(f"prefix in treverse: {prefix + char}")


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print('set(strings): ', set(strings))
    print('set(retireved_strings): ', set(retrieved_strings))
    print(f'matches? {matches}')


if __name__ == '__main__':
    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print('\n' + '='*80 + '\n')
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
