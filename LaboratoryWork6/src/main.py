from benchmark import *


def main():
    """
    This function estimates the speed of tree-making algorithms
    using 'benchmarking' function, creates a graph of the speed and
    saves it to '../img/outputImage.png'.
    """

    # Benchmarking...
    benchmarker = BenchMarker(
        range(1, 15),
        100,
        5
    )
    benchmarker.benchmarking_foreach()

    # Graph plotting...
    benchmarker.create_graphs()


if __name__ == "__main__":
    main()
