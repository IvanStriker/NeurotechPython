### Laboratory work 6
#### Place: `./`
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