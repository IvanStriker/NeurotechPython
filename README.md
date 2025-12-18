# Hi! This is my Python ITMO practice!
Author: Ivan Vinogradov (501493)
## Laboratory works
### Laboratory work 1
#### Place: `./LaboratoryWork1`
#### Structure:
- `./LaboratoryWork1/src` - code files
- `./LaboratoryWork1/docs` - Sphinx documentation files
#### Code files description:
- method `searcher -> Searcher -> searchTwoWithSum` realizes the main algorithm
- file `searcher.py` consists of 3 classes: `Searcher` (main class), `SearcherInputTypeError` and `SearcherInputValueError` (classes, describing errors being raised in searchTwoWithSum)
- file `test_searcher.py` includes all the testing logic
#### Docs description:
- docs can be found by opening `./LaboratoryWork1/docs/html/index.html`
- other files in `./LaboratoryWork1/docs` are for Sphinx only
### Laboratory work 2
#### Place: `./LaboratoryWork2`
#### Structure:
- `./LaboratoryWork2/src` - code files
- `./LaboratoryWork2/docs` - Sphinx documentation files
#### Code files description:
- function `main.py -> main` is the entry point
- method `guesser.py -> Guesser -> guess` realizes the prime algorithm using `Guesser`'s private methods
- file `test_searcher.py` includes all the testing logic
#### Docs description:
- docs can be found by opening `./LaboratoryWork2/docs/_build/html/index.html`
- other files in `./LaboratoryWork2/docs` are for Sphinx only
### Laboratory work 3
#### Place: `./LaboratoryWork3`
#### Structure:
- `./LaboratoryWork3/src` - code files
- `./LaboratoryWork3/docs` - Sphinx documentation files
#### Code files description:
- method `tree_maker.py -> TreeMaker -> genBinTree` realizes the prime algorithm using `TreeMaker`'s private methods
- file `tree_maker.py` includes classes `TreeMaker` (main class), `TreeNode` (realizes my tree data structure) and enums `TreeMakingMethod` (for recursion and bfs options), `TreeView` (for dict and TreeNode structures)
- file `test_tree_maker.py` includes all the testing logic
#### Docs description:
- docs can be found by opening `./LaboratoryWork3/docs/html/index.html`
- other files in `./LaboratoryWork3/docs` are for Sphinx only
### Laboratory work 4
#### Place: `./LaboratoryWork4`
#### Structure:
- `./LaboratoryWork4/src` - code files
- `./LaboratoryWork4/img` - the file with matplotlib graph
#### Code files description:
- function `main.py -> main` is the entry point. It realizes UI
- class `factorial_counter.py -> FactorialCounter` realizes all needed factorial counting and benchmarking method
### Laboratory work 5
Its functionality is realized in **LaboratoryWork3**
### Laboratory work 6
#### Place: `./LaboratoryWork6`
#### Structure:
- `./LaboratoryWork6/src` - code files
- `./LaboratoryWork6/img` - the file with matplotlib graph
- `./LaboratoryWork6/docs` - Sphinx doc files
#### Code files description:
- function `main.py -> main` is the entry point. It realizes benchmarking and creates the image of graph
- class `benchmark.py -> BenchMarker` provides me with all the needed benchmarking methods: `benchmarking_foreach` (collecting statistic data for each tree-making algorithm) and `create_graphs` (plotting the respective graphs and saving them to `img/outputImage.png`)
- file `tree_maker.py` is copied from `LaboratoryWork3` and realizes tree-making logic
- decorator `utility.py -> check_types` is written to automate checking whether types of functions' arguments match the ones declared in its signature
#### Docs description:
- docs can be found by opening `./LaboratoryWork6/docs/html/index.html`
- other files in `./LaboratoryWork6/docs` are for Sphinx only
### Laboratory work 7
#### Place: `./LaboratoryWork7`
#### Structure:
- `./LaboratoryWork7/src` - code files
#### Further description can be found in `./LaboratoryWork7/README.md`
### Laboratory work 8
#### Place: `./LaboratoryWork8`
#### Structure:
- `./LaboratoryWork8/src` - code files
#### Further description can be found in `./LaboratoryWork8/README.md`
### Laboratory work 9
#### Place: `./LaboratoryWork9`
#### Structure:
- `./LaboratoryWork9/src` - code files
#### Further description can be found in `./LaboratoryWork9/README.md`
### Laboratory work 10
#### Place: `./LaboratoryWork10`
#### Structure:
- `./LaboratoryWork10/src` - code files
#### Further description can be found in `./LaboratoryWork10/README.md`