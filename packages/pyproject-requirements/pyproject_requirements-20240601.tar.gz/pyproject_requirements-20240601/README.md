# pip-requirements (aka pyproject-requirements)

Install requirements/dependencies specified in a pyproject.toml using pip.

## Features

- Installs required, optional and/or all dependencies.
- Detects and works with pip in installed in virtual environments.
- Generates a requirements.txt file from a pyproject.toml (for tool compatibility).

## Quick Start

1. Install pip-requirements:

   ```shell
   pip install pyproject-requirements
   ```

2. Install all dependencies of your pyproject.toml 

   ```shell
   # use `--optional name` to limit to optional named dependency section
   # use `--required` to install required dependencies
   pip-requirements install --all path/to/pyproject.toml 
   ```

## Why

- This only exists because it's not builtin to pip.

- Using requirements.txt files is primitive and redundant compared to the expressiveness
  of pyproject.toml files..


## Usage

```
pip-requirements [-h] {install,txt} ...

Install dependencies from a pyproject file.

optional arguments:
-h, --help     show this help message and exit

commands:
Valid commands

```

### `install` Command

```
pip-requirements install [-h] [--all] [--required] [--optional [OPTIONAL ...]] [--pip PIP] [--dry] pyproject_toml

positional arguments:
pyproject_toml        pyproject.toml

optional arguments:
-h, --help            show this help message and exit
--all                 Install dependencies from all known sections (required and optional).
--required            Install required dependencies.
--optional [OPTIONAL ...]
Optional dependency to install. May be specified multiple times.
--pip PIP             Pip tool to use. Autodetected. Default: /home/nate/.local/bin/pip
--dry                 Dry run
```

### `txt` Command


```
pip-requirements txt [-h] [--all] [--required] [--optional [OPTIONAL ...]] pyproject_toml [output_file]

Generate a requirements.txt files for compatibility.

positional arguments:
  pyproject_toml        pyproject.toml
  output_file           path to a file to output. stdout otherwise.

optional arguments:
  -h, --help            show this help message and exit
  --all                 Include dependencies from all known sections (required and optional).
  --required            Include required dependencies.
  --optional [OPTIONAL ...]
                        Include optional dependency. May be specified multiple times.
```


## Future

We should have something like:

```shell
pip install --optional=name --required --all path/to/pyproject.toml
```

Or:

```shell
pip requirements install --all path/to/pyproject.toml
```


## Links

- [Source](https://hg.sr.ht/~metacompany/pip-requirements) (Source Hut)

