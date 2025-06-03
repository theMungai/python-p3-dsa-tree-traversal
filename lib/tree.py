class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    def deep_first(node):
      if node.get('id') == id:
        return node
      for child in node.get('children', []):
        result = deep_first(child)
        if result:
          return result
      return  None

    return deep_first(self.root)
