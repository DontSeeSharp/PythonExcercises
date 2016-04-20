"""EX20."""


class Tree:

    """Tree class."""

    def __init__(self, value=None, left=None, right=None, amount=1):
        """Constructor."""
        self.value = value
        self.left = left
        self.right = right
        self.amount = 1

    def __str__(self):
        """Modification."""
        return str(self.value)

    def add(self, word):
        """
        Take a string an place it into the right place in the tree.

        If it already is in the tree, increase the count of the string in the tree.
        Args:
        word(string) - string to be put in the tree
        Returns:
        None
        """
        if self.value is None:
            self.value = word
        elif word == self.value:
            self.amount += 1
        elif (word < self.value):
            if (self.left is not None):
                if self.left.value == word:
                    self.left.amount += 1
                else:
                    self.left.add(word)
            else:
                self.left = Tree(value=word)
        else:
            if (self.right is not None):
                if self.right.value == word:
                    self.right.amount += 1
                else:
                    self.right.add(word)
            else:
                self.right = Tree(value=word)

    def find(self, word, depth=0):
        """
        Find the word from the binary tree.

        If the word already exists in the tree, return tuple(word, amount, depth in tree).
        If the word doesn't exist, return None.

        Args:
        word - string to be searched
        Returns:
        Tuple(word, amount, depth) if word exists
        None if word doesn't exist.
        """
        if self.value is None:
            return None
        elif word is None:
            return None
        elif word == self.value:
            return (word, self.amount, depth)

        else:
            if word > self.value:
                answer = self.right.find(word, depth + 1)
            else:
                answer = self.left.find(word, depth + 1)

        return answer

    def print_ordered(self, value_list=[]):
        """
        Print whole tree alphabetically with each element with it's amount.

        Returns:
        string and their amounts in the tree.
        a 3
        b 7
        c 8
        """
        if self.value is None:
            return None
        if self.left is not None:
            self.left.print_ordered()
        print(self.value + " " + str(self.amount))
        if self.right is not None:
            self.right.print_ordered()


def get_tree():
    """Return instance of the class Tree."""
    return Tree()

if __name__ == "__main__":
    t = get_tree()
    t.add("7")
    t.add("4")
    t.add("6")
    t.add("5")
    t.add("3")
    t.add("2")
    t.add("1")
    t.add("d")
    t.add("a")
    t.add("b")
    t.add("g")
    t.add("e")
    t.add("1")
    t.add("e")
    t.add("f")
    t.add("2")
    t.add("g")
    print(t)
    print(t.right)
    # print(t.print_ordered())
    t.print_ordered()
