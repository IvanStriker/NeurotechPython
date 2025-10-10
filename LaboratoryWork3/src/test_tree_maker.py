import unittest
from tree_maker import *


class TestTreeMaker(unittest.TestCase):
    """
    A simple class for testing TreeMaker's functionality.
    """

    def test1(self):
        """Tests dict recursion with zero height"""
        self.assertEqual(TreeMaker.genBinTree
                         (0, 4),
                         {})

    def test2(self):
        """Tests dict bfs with zero height"""
        self.assertEqual(TreeMaker.genBinTree
                         (0, 4, method=TreeMakingMethod.BFS),
                         {})

    def test3(self):
        """Tests TreeNode recursion with zero height"""
        self.assertEqual(TreeMaker.genBinTree
                         (0, 4, method=TreeMakingMethod.RECURSION,
                          output=TreeView.TREE_NODES),
                         None)

    def test4(self):
        """Tests TreeNode bfs with zero height"""
        self.assertEqual(TreeMaker.genBinTree
                         (0, 4, method=TreeMakingMethod.BFS,
                          output=TreeView.TREE_NODES),
                         None)

    def test5(self):
        """Tests dict recursion with arguments from TO DO"""
        self.assertEqual(TreeMaker.genBinTree(),
                         {"3": [{"5": [{"7": [{"9": []},
                                              {"21": []}]},
                                       {"15": [{"17": []},
                                               {"45": []}]}]},
                                {"9": [{"11": [{"13": []},
                                               {"33": []}]},
                                       {"27": [{"29": []},
                                               {"81": []}]}]}]})

    def test6(self):
        """Tests dict bfs with arguments from TO DO"""
        self.assertEqual(TreeMaker.genBinTree
                         (method=TreeMakingMethod.BFS),
                         {"3": [{"5": [{"7": [{"9": []},
                                              {"21": []}]},
                                       {"15": [{"17": []},
                                               {"45": []}]}]},
                                {"9": [{"11": [{"13": []},
                                               {"33": []}]},
                                       {"27": [{"29": []},
                                               {"81": []}]}]}]})

    def test7(self):
        """Tests TreeNode recursion with arguments from TO DO"""
        RR = TreeNode(27, None, None)
        RL = TreeNode(11, None, None)
        R = TreeNode(9, RL, RR)
        RR.parentNode = RL.parentNode = R
        LR = TreeNode(15, None, None)
        LL = TreeNode(7, None, None)
        L = TreeNode(5, LL, LR)
        LL.parentNode = LR.parentNode = L
        Root = TreeNode(3, L, R)

        RRR = TreeNode(81, None, None, RR)
        RRL = TreeNode(29, None, None, RR)
        RR.rightNode = RRR
        RR.leftNode = RRL

        RLR = TreeNode(33, None, None, RL)
        RLL = TreeNode(13, None, None, RL)
        RL.rightNode = RLR
        RL.leftNode = RLL

        LRR = TreeNode(45, None, None, LR)
        LRL = TreeNode(17, None, None, LR)
        LR.rightNode = LRR
        LR.leftNode = LRL

        LLR = TreeNode(21, None, None, LL)
        LLL = TreeNode(9, None, None, LL)
        LL.rightNode = LLR
        LL.leftNode = LLL
        R.parentNode = L.parentNode = Root

        self.assertEqual(TreeMaker.genBinTree
                         (output=TreeView.TREE_NODES),
                         Root)

    def test8(self):
        """Tests TreeNode bfs with arguments from TO DO"""
        RR = TreeNode(27, None, None)
        RL = TreeNode(11, None, None)
        R = TreeNode(9, RL, RR)
        RR.parentNode = RL.parentNode = R
        LR = TreeNode(15, None, None)
        LL = TreeNode(7, None, None)
        L = TreeNode(5, LL, LR)
        LL.parentNode = LR.parentNode = L
        Root = TreeNode(3, L, R)

        RRR = TreeNode(81, None, None, RR)
        RRL = TreeNode(29, None, None, RR)
        RR.rightNode = RRR
        RR.leftNode = RRL

        RLR = TreeNode(33, None, None, RL)
        RLL = TreeNode(13, None, None, RL)
        RL.rightNode = RLR
        RL.leftNode = RLL

        LRR = TreeNode(45, None, None, LR)
        LRL = TreeNode(17, None, None, LR)
        LR.rightNode = LRR
        LR.leftNode = LRL

        LLR = TreeNode(21, None, None, LL)
        LLL = TreeNode(9, None, None, LL)
        LL.rightNode = LLR
        LL.leftNode = LLL
        R.parentNode = L.parentNode = Root

        self.assertEqual(TreeMaker.genBinTree
                         (method=TreeMakingMethod.BFS,
                          output=TreeView.TREE_NODES),
                         Root)

    def test9(self):
        """Tests dict bfs with other arguments"""

        self.assertEqual(TreeMaker.genBinTree
                         (3, 2, lambda x: x + 1,
                          lambda x: x * 2,
                          method=TreeMakingMethod.BFS),
                         {"2": [{"3": [{"4": []},
                                       {"6": []}]},
                                {"4": [{"5": []},
                                       {"8": []}]}]}
                         )

    def test10(self):
        """Tests dict recursion with other arguments"""

        self.assertEqual(TreeMaker.genBinTree
                         (3, 2, lambda x: x + 1,
                          lambda x: x * 2),
                         {"2": [{"3": [{"4": []},
                                       {"6": []}]},
                                {"4": [{"5": []},
                                       {"8": []}]}]}
                         )

    def test11(self):
        """Tests TreeNode recursion with other arguments"""
        RR = TreeNode(8, None, None)
        RL = TreeNode(5, None, None)
        R = TreeNode(4, RL, RR)
        RR.parentNode = RL.parentNode = R
        LR = TreeNode(6, None, None)
        LL = TreeNode(4, None, None)
        L = TreeNode(3, LL, LR)
        LL.parentNode = LR.parentNode = L
        Root = TreeNode(2, L, R)

        self.assertEqual(TreeMaker.genBinTree
                         (3, 2, lambda x: x + 1,
                          lambda x: x * 2,
                          output=TreeView.TREE_NODES),
                         Root)

    def test12(self):
        """Tests TreeNode bfs with other arguments"""
        RR = TreeNode(8, None, None)
        RL = TreeNode(5, None, None)
        R = TreeNode(4, RL, RR)
        RR.parentNode = RL.parentNode = R
        LR = TreeNode(6, None, None)
        LL = TreeNode(4, None, None)
        L = TreeNode(3, LL, LR)
        LL.parentNode = LR.parentNode = L
        Root = TreeNode(2, L, R)

        self.assertEqual(TreeMaker.genBinTree
                         (3, 2, lambda x: x + 1,
                          lambda x: x * 2,
                          method=TreeMakingMethod.BFS,
                          output=TreeView.TREE_NODES),
                         Root)


if __name__ == "__main__":
    unittest.main()