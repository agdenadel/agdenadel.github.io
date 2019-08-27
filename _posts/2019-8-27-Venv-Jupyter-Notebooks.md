---
layout: post
title: Using a Virtual Environment in Jupyter notebooks
tags: programming libraries python
---

Recently, I wanted to try out a library that goes along with a paper that was just published. I didn't want to actually install the library, because it comes with a bunch of specific dependencies, so I used a virtual environment for my testing. This is easy 

```
python3 -m venv env
```

Which creates a virtual environment called `env`. The library came with a bunch of examples in Jupyter notebooks. I usually just run Jupyter notebooks with standard Python installation on my machine, but in this case I needed to use the virtual environment that had all of the dependencies I needed. It's easy to set this up. First, activate your new virtual environment

```
source env/bin/activate
```

Then, in the environment, install `ipykernel`

```
pip install ipykernel
```

Finally, add the virtual environment as a kernel.

```
python -m ipykernel install --name=env
```

Then, when you create a new notebook you see `env` as an option and can have sets of notebooks with different dependencies. When you want to go back to your default Python installation just type `deactivate`