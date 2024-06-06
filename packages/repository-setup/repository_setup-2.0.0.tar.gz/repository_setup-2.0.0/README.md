# Description

Creates the basic repository structure for python projects

# Installation

`pip install repository_setup`

# Usage

`python -m repository_setup [-h] --path PATH --name NAME`


| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path of the directory in which the repository shall be created |
|--name | -n | String | - | Name of the new repository |

# Example

`python -m repository_setup -p /path/to/repo/dir -n new-module-repo`

Creates the following result:

```
################################################################################

Repository Setup by 5f0
Creates the basic repository structure for python projects

Current working directory: /path/to/repository-setup

Target directory: /path/to/repo/dir
Name of new repository: new-module-repo

Creation Datetime: 01/01/1970 10:11:12

################################################################################

Repository of type module created successfully under /path/to/repo/dir/new-module-repo

################################################################################
```

With the following folder structure:

```
/path/to/repo/dir/new-module-repo
├─── /src
     └─── /new_module_repo
          └─── /output
               └─── __init__.py
               └─── Output.py
          └─── /util
               └─── __init__.py
               └─── Util.py
          └─── /args
               └─── __init__.py
               └─── Args.py
          └─── __init__.py
          └─── __main__.py
└─── .gitignore
└─── LICENSE.md
└─── README.md
└─── setup.py
```

# License

MIT
