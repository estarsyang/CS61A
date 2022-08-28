class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches = []):
      for b in branches:
        assert isinstance(b, Tree)
      self.label = label
      self.branches = list(branches)
    
    def is_leaf(self):
      return not self.branches