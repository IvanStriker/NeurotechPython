import random
import timeit
import matplotlib.pyplot as plt

from tree_maker import *
from utility import *


class BenchMarker:
    """
    A class created to collect all the variables needed to
    benchmark different tree-making algorithms and to plot the
    respective graph in a single place.

    Attributes:
        tree_heights (range): Heights of trees for test data.
        res_recursive_dict (list[float]): Dict with time
            amounts needed to execute recursive tree-making
            algorithm saving the tree in a dict.
        res_iterative_dict (list[float]): Dict with time
            amounts needed to execute bfs tree-making
            algorithm saving the tree in a dict.
        res_recursive_nodes (list[float]): Dict with time
            amounts needed to execute recursive tree-making
            algorithm saving the tree in a nodes.
        res_iterative_nodes (list[float]): Dict with time
            amounts needed to execute bfs tree-making
            algorithm saving the tree in a nodes.
        number (int): The amount of times the method timeit will
            be called for each tree-making algorithm.
            It's set to 100 by default.
        repeat (int): The amount of times the method timeit will
            execute the "func" for each tree-making algorithm.
            It's set to 5 by default.
    """

    @check_types(Any, range, int, int)
    def __init__(self,
                 tree_heights: range,
                 number: int,
                 repeat: int):
        """
        Args:
            tree_heights (range): Heights of trees for test data.
            number (int): The amount of times the method timeit will
                be called for each tree-making algorithm.
                It's set to 100 by default.
            repeat (int): The amount of times the method timeit will
                execute the "func" for each tree-making algorithm.
                It's set to 5 by default.
        Raises:
            TypeError: If arguments' types doesn't match
                the signature.
        """
        self.tree_heights = tree_heights
        self.res_recursive_dict = []
        self.res_iterative_dict = []
        self.res_recursive_nodes = []
        self.res_iterative_nodes = []
        self.number = number
        self.repeat = repeat

    @check_types(Any, Callable, dict, int, int)
    def _benchmarking(self, func: Callable[[Any], Any],
                      data: dict[Any],
                      number: int = 100,
                      repeat: int = 5) -> float:
        """
        Returns the average time of the function's execution on
        "data" input

        Args:
            func (Callable[[Any], Any]): The function to estimate
            data (Dict[Any]): The input data for "func" parameter
            number (int): The amount of times the method timeit will
                be called. It's set to 100 by default.
            repeat (int): The amount of times the method timeit will
                execute the "func". It's set to 5 by default.

        Returns:
            float: The average amount of time the "func" took to
                return a result.

        Raises:
            TypeError: If given arguments are of wrong types.
            ValueError: If "func" can't work with "data".
        """
        try:
            times = timeit.repeat(lambda: func(**data),
                                  number=number,
                                  repeat=repeat)
        except TypeError:
            raise TypeError(
                "Parameter 'data' must be of the type "
                "appropriate for 'func' to be called with."
            )
        except ValueError:
            raise ValueError(
                "Parameter 'data' must be of the value "
                "appropriate for 'func' to be called with."
            )
        return sum(times) / len(times)

    def create_graphs(self):
        """
        Creates the graph of tree-making algorithms' speed and
        Saves it to '../img/outputImage.png'.
        """
        plt.figure(figsize=(20, 10))
        plt.subplot(1, 2, 1)
        plt.plot(self.tree_heights, self.res_recursive_dict,
                 label="Рекурсивный (в dict)")
        plt.plot(self.tree_heights, self.res_iterative_dict,
                 label="Итеративный (в dict)")
        plt.xlabel("height")
        plt.ylabel("Время (сек)")
        plt.title(
            "Сравнение рекурсивного и итеративного дерева в dict")
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(self.tree_heights, self.res_recursive_nodes,
                 label="Рекурсивный (в TreeNode)")
        plt.plot(self.tree_heights, self.res_iterative_nodes,
                 label="Итеративный (в TreeNode)")
        plt.xlabel("height")
        plt.ylabel("Время (сек)")
        plt.title(
            "Сравнение рекурсивного и итеративного дерева в TreeNode")
        plt.legend()
        # plt.show()
        plt.savefig("../img/outputImage.png")

    def benchmarking_foreach(self):
        """
        Estimates different tree-making algorithms' speed and saves grades
        to its args.
        """
        methods = [TreeMakingMethod.RECURSION,
                   TreeMakingMethod.BFS]
        outputs = [TreeView.DICT,
                   TreeView.TREE_NODES]
        containers = [self.res_recursive_dict,
                      self.res_iterative_dict,
                      self.res_recursive_nodes,
                      self.res_iterative_nodes]
        tree_making_params = [{"method": j, "output": i}
                              for i in outputs for j in methods]
        for n in self.tree_heights:
            for params_i in range(4):
                params = tree_making_params[params_i]
                containers[params_i].append(self._benchmarking(
                    TreeMaker.genBinTree,
                    {
                        "height": n,
                        "method": params["method"],
                        "output": params["output"]
                    },
                    self.number, self.repeat))


random.seed(42)
