[![Gitlab CI](https://gitlab.com/odoo-tools-grap/odoo-tools-grap/badges/main/pipeline.svg)](https://gitlab.com/odoo-tools-grap/odoo-tools-grap/-/pipelines)
[![codecov](https://gitlab.com/odoo-tools-grap/odoo-tools-grap/badges/main/coverage.svg)](https://gitlab.com/odoo-tools-grap/odoo-tools-grap/)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/odoo-tools-grap)
![PyPI - Downloads](https://img.shields.io/pypi/dm/odoo-tools-grap)
![GitLab last commit](https://img.shields.io/gitlab/last-commit/34780558)
![GitLab stars](https://img.shields.io/gitlab/stars/34780558?style=social)

# odoo-tools-grap

This tools provide extra cli commands to simplify recurring operations for Odoo developers.

* To develop and contribute to the library, refer to the ``DEVELOP.md`` file.
* Refer to the ``ROADMAP.md`` file to see the current limitation, bugs, and task to do.
* See authors in the ``CONTRIBUTORS.md`` file.


# Table of Contents

* [Installation](#installation)
* [Usage](#usage)
    * [Command ``diff`` (View repositories status)](#command-diff)
    * [Command ``generate`` (Generate Odoo config File)](#command-generate)
    * [Command ``create-branch`` (Create new Orphan Branch)](#command-create-branch)
    * [Command: ``migrate`` (Migrate module from a version to another)](#command-migrate)
* [Prerequites](#prerequites)


<a name="installation"/>

# Installation

The library is available on [PyPI](https://pypi.org/project/odoo-tools-grap/).

To install it simply run :

``pipx install odoo-tools-grap``

(See alternative installation in ``DEVELOP.md`` file.)

```
    pipx install
```

<a name="usage"/>

# Usage

<a name="command-diff"/>

## Command: ``diff`` (View repositories status)

Based on a repos config file (``repos.yml file``, used by gitaggregate by
exemple), this script will display the result of the ``git diff`` for each
repository.

```
    odoo-tools-grap diff --config repos.yml
```

**Result Sample**

```
2024-03-27 16:37:24.725 | WARNING  | odoo_tools_grap.cli.cli_diff:diff:31 - [BAD BRANCH] ./src/OCA/product-attribute is on 16.0-product_pricelist_simulation-various-fixes.(Should be on 16.0-current)
2024-03-27 16:37:25.395 | WARNING  | odoo_tools_grap.cli.cli_diff:diff:38 - [LOCAL CHANGES] ./src/OCA/sale-workflow has 1 local changes.
2024-03-27 16:37:25.444 | WARNING  | odoo_tools_grap.cli.cli_diff:diff:43 - [UNTRACKED] ./src/OCA/sale-workflow has 2 untracked files.
```

<a name="command-generate"/>

## Command: ``generate`` (Generate Odoo config File)

Base on a repos config file, (``repos.yml file``, used by gitaggregate by exemple),
and template(s) of odoo config file, this script will generate a complete config file for Odoo
with addons_path depending on the repos config file.

```

    odoo-tools-grap generate\
        --config repos.yml\
        --input-files ./template.config.cfg\
        --output-file ./odoo.cfg
```

<a name="command-create-branch"/>

## Command: ``create-branch`` (Create new Orphan Branch)

TODO.

<a name="command-migrate"/>

## Command: ``migrate`` (Migrate module from a version to another)


<a name="prerequites"/>

# Prerequites

To understand this tool, you need to know the following tools:

* git-aggregator (https://github.com/acsone/git-aggregator)
