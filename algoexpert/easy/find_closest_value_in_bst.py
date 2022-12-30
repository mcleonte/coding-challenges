def findClosestValueInBst(tree, target):
    closest = float("inf")
    while tree:
        closest = (
            tree.value if abs(target - tree.value) < abs(closest - target) else closest
        )
        tree = tree.left if target < tree.value else tree.right
    return closest


def findClosestValueInBst2(tree, target):
    if target == tree.value:
        return tree.value
    child = tree.left if target < tree.value else tree.right
    if child is None:
        return tree.value
    child_value = findClosestValueInBst(child, target)
    return (
        tree.value
        if abs(target - tree.value) < abs(child_value - target)
        else child_value
    )


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
