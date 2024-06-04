# ListObjectsAsync

## Overview
ListObjectsAsync is an asynchronous utility for listing objects in an AWS S3 bucket. 
This tool utilizes the aiobotocore library to provide efficient, non-blocking access to your S3 data, supporting 
recursive directory traversal with depth control.

## Features
- Asynchronous Operations: Utilizes asyncio for non-blocking IO operations.
- Paginated Results: Handles S3 pagination internally to provide a efficient traversal of long S3 objects lists.
- Recursive Traversal: Supports recursive listing of objects with controllable depth control.
- Retries: AUtilize AWS retry strategies.

## Usage

```python
--8<-- "list.py"
```
You can control the depth of recursion by specifying the max_depth parameter, by default depth is not limited.

## Installation

## Installing pipx
[`pipx`](https://pypa.github.io/pipx/) creates isolated environments to avoid conflicts with existing system packages.

=== "MacOS"
    In the terminal, execute:
    ```bash
    --8<-- "install_pipx_macos.sh"
    ```

=== "Linux"
    First, ensure Python is installed.

    Enter in the terminal:

    ```bash
    python3 -m pip install --user pipx
    python3 -m pipx ensurepath
    ```

=== "Windows"
    First, install Python if it's not already installed.

    In the command prompt, type (if Python was installed from the Microsoft Store, use `python3` instead of `python`):
    
    ```bash
    python -m pip install --user pipx
    ```

## Installing `aws-s3`:
In the terminal (command prompt), execute:

```bash
pipx install aws-s3
```

### Implementation Details

[ListObjectsAsync][aws_s3]

