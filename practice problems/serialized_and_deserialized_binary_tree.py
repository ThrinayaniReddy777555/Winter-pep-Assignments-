class Codec:
    def serialize(self, root):
        vals = []
        def _serialize(node):
            if node:
                vals.append(str(node.val))
                _serialize(node.left)
                _serialize(node.right)
            else:
                vals.append("#")
        _serialize(root)
        return " ".join(vals)

    def deserialize(self, data):
        vals = iter(data.split())
        def _deserialize():
            val = next(vals, None)
            if val == "#" or val is None: return None
            node = TreeNode(int(val))#type: ignore
            node.left = _deserialize()
            node.right = _deserialize()
            return node
        return _deserialize()

