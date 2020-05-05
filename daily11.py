"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

# use a Trie


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.last_letter = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []

    def insert(self, key):
        node = self.root

        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]

        node.last_letter = True

    def generate_from_keys(self, keys):
        for key in keys:
            self.insert(key)

    def search(self, key):
        node = self.root

        for a in list(key):
            if not node.children.get(a):
                return False
            node = node.children[a]

        return node and node.last_letter

    def starts_with(self, key):
        node = self.root

        for a in list(key):
            if not node.children.get(a):
                return False
            node = node.children[a]

        return True

    def generate_suggestions(self, key):
        node = self.root
        temp_word = ''

        for a in list(key):
            if not node.children.get(a):
                return []

            temp_word += a
            node = node.children[a]

        if node.last_letter and not node.children:
            return []

        self._suggest_word_list(node, temp_word)

        return self.word_list

    def _suggest_word_list(self, node, word):
        if node.last_letter:
            self.word_list.append(word)

        for a, n in node.children.items():
            self._suggest_word_list(n, word + a)

    def print_trie(self):
        self._print_helper(self.root, ' ')

    def _print_helper(self, node, prefix):
        if node.last_letter:
            return

        for item, child in node.children.items():
            print(prefix + item)
            prefix += ' '
            self._print_helper(child, prefix)


keys = ['dog', 'deer', 'deal']

node = Trie()
node.generate_from_keys(keys)

# print(node.print_trie())
assert(node.starts_with('de'))
print(node.generate_suggestions('de'))
