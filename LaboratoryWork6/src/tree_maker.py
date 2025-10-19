from typing import Callable
from enum import Enum
from queue import Queue


class TreeMakingMethod(Enum):
    """
    Enum for different tree making algorithms

    Attributes:
        RECURSION (TreeMakingMethod): Recursive algorithm
        BFS (TreeMakingMethod): Breadth first search algorithm
    """
    RECURSION = 1
    BFS = 2


class TreeView(Enum):
    """
    Enum for different types of tree structures

    Attributes:
        DICT (TreeView): tree inside a dict
        TREE_NODES (TreeView): tree saved in TreeNode objects
    """
    DICT = 1
    TREE_NODES = 2


class TreeNode:
    """
    A class representing trees saved in lots of separate nodes.

    Each node is an object of this TreeNode class. They are bound
    through its attributes-links.

    Attributes:
        value (int): values saved in a current node
        leftNode (TreeNode | None): a link to the lift child
        rightNode (TreeNode | None): a link to the right child
        parentNode (TreeNode | None): a link to the parent item
    """

    def __init__(self, value: int,
                 leftNode: "TreeNode | None" = None,
                 rightNode: "TreeNode | None" = None,
                 parentNode: "TreeNode | None" = None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.parentNode = parentNode

    def __eq__(self, other: "TreeNode") -> bool | None:
        if self.value != other.value:
            return False
        if any([self.rightNode is None, self.leftNode is None]) \
                and any([other.rightNode is not None,
                         self.leftNode is not None]):
            return False
        if any([self.rightNode is not None, self.leftNode is not None]) \
                and any([other.rightNode is None,
                         self.leftNode is None]):
            return False
        if any([self.rightNode is None, self.leftNode is None]):
            return True
        return self.rightNode.__eq__(other.rightNode) \
            and self.leftNode.__eq__(other.leftNode)


class TreeMaker:
    """
    The main class of the project.

    It provides you with methods able to make different sorts of trees.

    Attributes:
        _WrongMethodValueError (ValueError): An error raised when there
            is no such making tree algorithm. All available algorithms
            are listed in TreeMakingMethods enum.
        _WrongOutputValueError (ValueError): An error raised when there
            is no such tree structure. All available structures
            are listed in TreeView enum.
    """

    _WrongMethodValueError: ValueError = ValueError(
        "`method` argument of TreeMaker.genAsDict must be a value "
        "of TreeMakingMethod enum."
    )

    _WrongOutputValueError: ValueError = ValueError(
        "`output` argument of TreeMaker.genBinTree must be a value "
        "of TreeView enum."
    )

    @staticmethod
    def genBinTree(height: int = 4,
                   root: int = 3,
                   l_b: Callable[[int], int] = lambda x: x + 2,
                   r_b: Callable[[int], int] = lambda y: y * 3,
                   method: TreeMakingMethod = TreeMakingMethod.RECURSION,
                   output: TreeView = TreeView.DICT
                   ) -> dict | TreeNode | None:
        """
        This is the main function. It constructs trees.

        It generates the tree of the height, root value,
        functions describing algorithm to count the child's values,
        algorithm of tree building and final structure of the tree.

        Args:
            height (int): The amount of `floors` in the tree:
                2**nodes - 1 == height
            root (int): The root node's value
            l_b (Callable[[int], int]): functions describing algorithm
                to count the left child's values. It accepts
                the current node's value and returns its left child's
                value
            r_b (Callable[[int], int]): functions describing algorithm
                to count the right child's values. It accepts
                the current node's value and returns its right child's
                value
            method (TreeMakingMethod): The algorithm of tree building.
                For more info see enum TreeMakingMethod
            output (TreeView): The structure of the final tree.
                For more info see enum TreeView

        Returns:
            Dict | TreeNode | None: The tree constructed. The type of it
                depends on the tree building method chosen.

        Raises:
            TypeError: If types of the arguments doesn't match
                the signature.
            ValueError: If method or output argument doesn't contain
                any of the values listed in TreeMakingMethod and TreeView
                respectively.
        """
        TreeMaker._checkInput(height, root, l_b, r_b)
        if output == TreeView.DICT:
            return TreeMaker._genAsDict(height, root, l_b, r_b, method)
        if output == TreeView.TREE_NODES:
            return TreeMaker._genAsTreeNodes(height, root, l_b, r_b, method)
        raise TreeMaker._WrongOutputValueError

    @staticmethod
    def _checkInput(height: int,
                    root: int,
                    l_b: Callable[[int], int],
                    r_b: Callable[[int], int]):
        """
        This function tests whether the arguments of TreeMaker.genBinTree
        have proper types.

        Args:
            height (int): The amount of `floors` in the tree:
                2**(nodes + 1) == height
            root (int): The root node's value
            l_b (Callable[[int], int]): functions describing algorithm
                to count the left child's values. It accepts
                the current node's value and returns its left child's
                value
            r_b (Callable[[int], int]): functions describing algorithm
                to count the right child's values. It accepts
                the current node's value and returns its right child's
                value

        Raises:
            TypeError: If types of the arguments doesn't match
                the signature.
        """
        inputError = (
            TypeError("Types of the arguments must match the signature"))
        if not all([
            isinstance(height, int),
            isinstance(root, int),
            isinstance(l_b, Callable),
            isinstance(r_b, Callable)]):
            raise inputError

        try:
            a, b = l_b(3), r_b(3)
            if not isinstance(a, int) or not isinstance(b, int):
                raise TypeError
        except TypeError:
            raise inputError

    @staticmethod
    def _genAsTreeNodes(height: int,
                        root: int,
                        l_b: Callable[[int], int],
                        r_b: Callable[[int], int],
                        method: TreeMakingMethod) -> TreeNode | None:
        """
        This is a TreeMaker.genBinTree realization constructing trees
        of TreeNode structure.

        Args:
            height (int): The amount of `floors` in the tree:
                2**nodes - 1 == height
            root (int): The root node's value
            l_b (Callable[[int], int]): functions describing algorithm
                to count the left child's values. It accepts
                the current node's value and returns its left child's
                value
            r_b (Callable[[int], int]): functions describing algorithm
                to count the right child's values. It accepts
                the current node's value and returns its right child's
                value
            method (TreeMakingMethod): The algorithm of tree building.
                For more info see enum TreeMakingMethod

        Returns:
            TreeNode | None: The tree constructed. None is returned if
                height == 0

        Raises:
            ValueError: If method argument doesn't contain
                any of the values listed in TreeMakingMethod.
        """
        if method == TreeMakingMethod.RECURSION:
            return TreeMaker._genAsTreeNodesRecursively(height, root, l_b,
                                                        r_b, None)
        if method == TreeMakingMethod.BFS:
            return TreeMaker._genAsTreeNodesWithBfs(height, root, l_b,
                                                    r_b)
        raise TreeMaker._WrongMethodValueError

    @staticmethod
    def _genAsDict(height: int,
                   root: int,
                   l_b: Callable[[int], int],
                   r_b: Callable[[int], int],
                   method: TreeMakingMethod) -> dict:
        """
        This is a TreeMaker.genBinTree realization constructing trees
        of dict structure.

        Args:
            height (int): The amount of `floors` in the tree:
                2**nodes - 1 == height
            root (int): The root node's value
            l_b (Callable[[int], int]): functions describing algorithm
                to count the left child's values. It accepts
                the current node's value and returns its left child's
                value
            r_b (Callable[[int], int]): functions describing algorithm
                to count the right child's values. It accepts
                the current node's value and returns its right child's
                value
            method (TreeMakingMethod): The algorithm of tree building.
                For more info see enum TreeMakingMethod

        Returns:
            Dict: The tree constructed.

        Raises:
            ValueError: If method argument doesn't contain
                any of the values listed in TreeMakingMethod.
        """
        if method == TreeMakingMethod.RECURSION:
            return TreeMaker._genAsDictRecursively(height, root,
                                                   l_b, r_b)
        if method == TreeMakingMethod.BFS:
            return TreeMaker._genAsDictWithBfs(height, root,
                                               l_b, r_b)
        raise TreeMaker._WrongMethodValueError

    @staticmethod
    def _genAsDictRecursively(height: int,
                              root: int,
                              l_b: Callable[[int], int],
                              r_b: Callable[[int], int]
                              ) -> dict:
        """
        This is a TreeMaker._genAsDict realization constructing trees
        with recursive algorithm.

        Args:
            height (int): The amount of `floors` in the tree:
                2**nodes - 1 == height
            root (int): The root node's value
            l_b (Callable[[int], int]): functions describing algorithm
                to count the left child's values. It accepts
                the current node's value and returns its left child's
                value
            r_b (Callable[[int], int]): functions describing algorithm
                to count the right child's values. It accepts
                the current node's value and returns its right child's
                value

        Returns:
            Dict: The tree constructed.
        """
        if height == 0:
            return {}
        if height <= 1:
            return {str(root): []}
        return {
            str(root):
                [TreeMaker._genAsDictRecursively(height - 1, l_b(root),
                                                 l_b, r_b),
                 TreeMaker._genAsDictRecursively(height - 1, r_b(root),
                                                 l_b, r_b)]
        }

    @staticmethod
    def _genAsDictWithBfs(height: int,
                          root: int,
                          l_b: Callable[[int], int],
                          r_b: Callable[[int], int]
                          ) -> dict:
        """
        This is a TreeMaker._genAsDict realization constructing trees
        with bfs algorithm.

        Args:
            height (int): The amount of `floors` in the tree:
                2**nodes - 1 == height
            root (int): The root node's value
            l_b (Callable[[int], int]): functions describing algorithm
                to count the left child's values. It accepts
                the current node's value and returns its left child's
                value
            r_b (Callable[[int], int]): functions describing algorithm
                to count the right child's values. It accepts
                the current node's value and returns its right child's
                value

        Returns:
            Dict: The tree constructed.
        """
        if not height:
            return {}
        res = {str(root): []}
        treeQueue = Queue()
        treeQueue.put(res)
        for i in range(1, 2 ** (height - 1)):
            node = treeQueue.get()
            for key in node:
                leftNode = {str(l_b(int(key))): []}
                rightNode = {str(r_b(int(key))): []}
                node[key] = [leftNode, rightNode]
                treeQueue.put(leftNode)
                treeQueue.put(rightNode)

        return res

    @staticmethod
    def _genAsTreeNodesRecursively(height: int,
                                   root: int,
                                   l_b: Callable[[int], int],
                                   r_b: Callable[[int], int],
                                   parentNode: TreeNode | None = None
                                   ) -> TreeNode | None:
        """
        This is a TreeMaker._genAsTreeNodes realization constructing trees
        with recursive algorithm.

        Args:
            height (int): The amount of `floors` in the tree:
                2**nodes - 1 == height
            root (int): The root node's value
            l_b (Callable[[int], int]): functions describing algorithm
                to count the left child's values. It accepts
                the current node's value and returns its left child's
                value
            r_b (Callable[[int], int]): functions describing algorithm
                to count the right child's values. It accepts
                the current node's value and returns its right child's
                value

        Returns:
            TreeNode | None: The tree constructed. None is returned if
                height == 0
        """
        if height == 0:
            return None
        node = TreeNode(root, parentNode=parentNode)
        node.leftNode = TreeMaker._genAsTreeNodesRecursively(
            height - 1, l_b(root), l_b, r_b, node)
        node.rightNode = TreeMaker._genAsTreeNodesRecursively(
            height - 1, r_b(root), l_b, r_b, node)
        return node

    @staticmethod
    def _genAsTreeNodesWithBfs(height: int,
                               root: int,
                               l_b: Callable[[int], int],
                               r_b: Callable[[int], int]
                               ) -> TreeNode | None:
        """
        This is a TreeMaker._genAsTreeNodes realization constructing trees
        with bfs algorithm.

        Args:
            height (int): The amount of `floors` in the tree:
                2**nodes - 1 == height
            root (int): The root node's value
            l_b (Callable[[int], int]): functions describing algorithm
                to count the left child's values. It accepts
                the current node's value and returns its left child's
                value
            r_b (Callable[[int], int]): functions describing algorithm
                to count the right child's values. It accepts
                the current node's value and returns its right child's
                value

        Returns:
            TreeNode | None: The tree constructed. None is returned if
                height == 0
        """
        if not height:
            return None
        res = TreeNode(root)
        treeQueue = Queue()
        treeQueue.put(res)
        for i in range(1, 2 ** (height - 1)):
            node = treeQueue.get()
            leftNode = TreeNode(l_b(node.value), parentNode=node)
            rightNode = TreeNode(r_b(node.value), parentNode=node)
            node.leftNode = leftNode
            node.rightNode = rightNode
            treeQueue.put(leftNode)
            treeQueue.put(rightNode)
        return res
