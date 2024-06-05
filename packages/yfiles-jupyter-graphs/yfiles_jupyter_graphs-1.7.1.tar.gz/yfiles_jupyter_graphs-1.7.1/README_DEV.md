# yfiles-jupyter-graphs

A diagram visualization extension for JupyterLab and Jupyter Notebooks powered by yFiles for HTML

## Installation

You can install using `pip`:

```bash
pip install yfiles_jupyter_graphs
```

If you are using Jupyter Notebook 5.2 or earlier, you may also need to enable
the nbextension:
```bash
jupyter nbextension enable --py [--sys-prefix|--user|--system] yfiles_jupyter_graphs
```

## Development Installation

Create a dev environment:
```bash
conda create -n yjg-dev -c conda-forge nodejs python jupyterlab=4.0.11 build
# or use 
# conda env create -f environment.dev.yml
conda activate yjg-dev
```

Install the python environment. This will also install the frontend dependencies and build the TS package.
```bash
pip install -e ".[test, examples]"
```

When developing your extensions, you need to manually enable your extensions with the
notebook / lab frontend. For lab, this is done by the command:

```
jupyter labextension develop --overwrite .
jlpm run build
```

For classic notebook, you need to run:

```
jupyter nbextension install --sys-prefix --symlink --overwrite --py yfiles_jupyter_graphs
jupyter nbextension enable --sys-prefix --py yfiles_jupyter_graphs
```

Note that the `--symlink` flag doesn't work on Windows, so you will here have to run
the `install` command every time that you rebuild your extension. For certain installations
you might also need another flag instead of `--sys-prefix`, but we won't cover the meaning
of those flags here.

## Building the distribution package (aka the wheel)

Run
```bash
python -m build .
```
To create both, the source distribution (`.tar.gz`) and the wheel (`.whl`) files. To only build the `whl`, run it with
`--wheel`.

## How to see your changes
### Typescript:
If you use JupyterLab to develop then you can watch the source directory and run JupyterLab at the same time in different
terminals to watch for changes in the extension's source and automatically rebuild the widget.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
jlpm run watch
# Run JupyterLab in another terminal
jupyter lab
```

After a change wait for the build to finish and then refresh your browser and the changes should take effect.

### Python:
If you make a change to the python code then you will need to restart the notebook kernel to have it take effect.

