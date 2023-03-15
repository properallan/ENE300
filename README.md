Repository created to store source code implemented for the *Computational Intelligence* course. 

If the system already able to run `jupyter` notebooks. Then, all is need is to download and extract this repository, or assuming a system with a working `git`, just cloning it as follow:

```
git clone https://github.com/properallan/ENE300/
```

Move to the created repository root folder:

```
cd ENE300
```

Install the `ene300` package using pip

```
pip install ./
```

To install a conda environment able to run the `jupyter` notebooks, in the root directory of the cloned repository. Create a new conda environment form the providade `environment.yml` file:

```
conda env create --file environment.yml
```

, end then activate the environment

```
conda activate ene300env
```