# JMDOTS Workbench

JMDOTS Workbench is an OS-agnostic utility suite.

## Tools

### `wbcopy` | `wbpaste`

These tools provide simple `copy` and `paste` functionality from the command line.

| Feature                         | `wbcopy` | `wbpaste` | Example Usage                    |
|---------------------------------|----------|-----------|----------------------------------|
| Copy text from string           | `X`      |           | `wbcopy "Hello, World!"`         |
| Copy text from file             | `X`      |           | `wbcopy -f filename.txt`         |
| Copy text from pipe (stdout)    | `X`      |           | `echo "Hello, World!" \| wbcopy` |
| Paste text to stdout            |          | `X`       | `wbpaste`                        |
| Paste text to file              |          | `X`       | `wbpaste -f output.txt`          |

NOTE: `wbcopy` and `wbpaste` are supported only for local operations. Operations over `ssh` are not supported.

### `wbrebase`

This tool automates the process of `git` rebasing the current branch on top of the `main` branch.

Usage: `wbrebase`

Steps taken by `wbrebase`:

- Step 1: Stow current branch name
- Step 2: Switch to main branch
- Step 3: Fetch all updates
- Step 4: Pull latest changes
- Step 5: Switch back to original branch
- Step 6: Rebase on main
- Step 7: Push changes
- Step 8: Show commit log

## Installation

To install the project to your host Python conda environment outside of Poetry, ensure you have Poetry and GNU Make installed as prerequisites. Then follow these steps:

1. Ensure Poetry and GNU Make are installed:

```bash
# Install Poetry
pip install poetry

# Install GNU Make (if not already installed)
# For Ubuntu/Debian
sudo apt-get install make
```

2. As an example of where you can install, activate your desired conda environment:

```bash
conda activate <your_env_name>
```

3. Navigate to the project directory:

```bash
cd ~/src/workbench
```

4. Install the project using the following command:

```bash
make install
```

5. After installing the project, you can use the installed commands (`wbcopy` and `wbpaste`) directly from your conda environment.

## Running Tests

```bash
make test
```

## License

```
===============================================================
jmdots-workbench - JMDOTS Workbench - OS-agnostic utility suite
===============================================================
Copyright © 2024 Joshua M. Dotson (contact@jmdots.com)

JMDOTS-DUAL-LICENSE-1.2
=======================
https://legal.jmdots.com/licenses/

Personal, Non-Commercial License
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This software is provided under the GNU Affero General Public License (AGPL)
version 3 or later. You are free to use, modify, and distribute this
software for personal, non-commercial use under the terms of the AGPL. If you
modify this software and distribute it, you must also make the modified
source code available under the same license terms. There is no warranty for
this software, to the extent permitted by applicable law.

For more details, please refer to the full text of the GNU AGPL: [GNU Affero
General Public License](http://www.gnu.org/licenses/)

Commercial License
~~~~~~~~~~~~~~~~~
This software is available under a Commercial License for any business,
commercial, enterprise, or governmental use. The Commercial License allows
you to use, modify, and distribute this software in proprietary applications
without the requirement to disclose source code modifications or derivative
works. Under this license, you receive additional support and maintenance
services.

For information on purchasing a commercial license, please contact us at
[sales@jmdots.com](mailto:sales@jmdots.com) or visit our website at [JMDOTS
GitHub](http://www.github.com/jmdots/).

Limited Liability
~~~~~~~~~~~~~~~~
In no event shall the authors or copyright holders be liable for any claim,
damages, or other liability arising from the use or distribution of this
software.
```
