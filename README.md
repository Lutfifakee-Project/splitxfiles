# 📂 splitxfiles

[![PyPI](https://img.shields.io/pypi/v/splitxfiles)](https://pypi.org/project/splitxfiles/)
[![Python Versions](https://img.shields.io/pypi/pyversions/splitxfiles)](https://pypi.org/project/splitxfiles/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/splitxfiles)](https://pypi.org/project/splitxfiles/)

A simple and lightweight Python library and Command Line Interface (CLI) for splitting files into smaller parts based on **line count** (text files) or **file size** (any file).

Ideal for processing log files, datasets, backups, wordlists, and other large files.

---

# ✨ Features

- 📄 Split UTF-8 text files by line count
- 📦 Split any file by file size
- 🐍 Easy-to-use Python API
- 💻 Command Line Interface (CLI)
- 📁 Automatically creates output directories
- 📊 Optional progress output
- ✅ Cross-platform (Windows, Linux, macOS)

---

# 📦 Installation

## Install from PyPI

```bash
pip install splitxfiles
```

## Install from Source

```bash
git clone https://github.com/Lutfifakee-Project/splitxfiles.git

cd splitxfiles

pip install -e .
```

---

# 🖥 Requirements

- Python 3.6 or later
- Windows
- Linux
- macOS

---

# 🚀 Python Usage

## Split Text File by Line Count

```python
from splitxfiles import split_by_lines

split_by_lines(
    input_path="data.txt",
    output_path="output",
    lines_per_file=100
)
```

---

## Split File by Size

```python
from splitxfiles import split_by_size

split_by_size(
    input_path="archive.bin",
    output_path="output",
    size_bytes=1024 * 1024  # 1 MB
)
```

---

# 💻 Command Line Usage

## Split by Line Count

```bash
splitxfiles input.txt -o output -l 100
```

---

## Split by File Size

```bash
splitxfiles input.bin -o output -s 1048576
```

---

## Quiet Mode

```bash
splitxfiles input.txt -l 100 -q
```

---

## Display Help

```bash
splitxfiles --help
```

---

# ⚙ CLI Options

| Option | Description |
|---------|-------------|
| `-l`, `--lines` | Split file by line count |
| `-s`, `--size` | Split file by size (bytes) |
| `-o`, `--output` | Output directory (default: `split_output`) |
| `-q`, `--quiet` | Disable progress output |
| `-h`, `--help` | Show help message |

---

# 📂 Output

Example directory:

```text
output/

├── data_part_1.txt
├── data_part_2.txt
├── data_part_3.txt
└── data_part_4.txt
```

Output files are automatically named using the following format:

```text
<original_filename>_part_<number>.<extension>
```

Example:

```text
log_part_1.txt
log_part_2.txt
log_part_3.txt
```

---

# 📸 Example Output

```text
📄 Splitting 1500 lines into 3 files...
📁 Output folder: output
--------------------------------------------------
✅ [1/3] data_part_1.txt (500 lines)
✅ [2/3] data_part_2.txt (500 lines)
✅ [3/3] data_part_3.txt (500 lines)
--------------------------------------------------
✅ Done! 3 files created successfully.
```

> **Note**
>
> The exact output may vary depending on the `verbose` option and future versions.

---

# 📚 API Reference

## `split_by_lines()`

Split a UTF-8 text file into multiple smaller files based on the number of lines.

```python
split_by_lines(
    input_path,
    output_path,
    lines_per_file,
    verbose=True
)
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input_path` | `str` | Path to the input text file |
| `output_path` | `str` | Output directory |
| `lines_per_file` | `int` | Maximum number of lines per output file |
| `verbose` | `bool` | Show progress information (default: `True`) |

### Returns

| Type | Description |
|------|-------------|
| `bool` | Returns `True` if the operation succeeds, otherwise `False`. |

---

## `split_by_size()`

Split any file into multiple smaller files based on file size.

```python
split_by_size(
    input_path,
    output_path,
    size_bytes,
    verbose=True
)
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input_path` | `str` | Path to the input file |
| `output_path` | `str` | Output directory |
| `size_bytes` | `int` | Maximum size of each output file (bytes) |
| `verbose` | `bool` | Show progress information (default: `True`) |

### Returns

| Type | Description |
|------|-------------|
| `bool` | Returns `True` if the operation succeeds, otherwise `False`. |

---

# ⚠ Error Handling

The functions return `False` when:

- The input file does not exist.
- The input file is empty.
- The specified line count is less than or equal to zero.
- The specified file size is less than or equal to zero.
- An unexpected exception occurs during processing.

---

# 🧪 Running Tests

Run all unit tests:

```bash
python -m unittest tests/test_split.py -v
```

---

# 📁 Project Structure

```text
splitxfiles/

├── src/
│   └── splitxfiles/
│       ├── __init__.py
│       └── cli.py
│
├── tests/
│   └── test_split.py
│
├── README.md
├── LICENSE
├── pyproject.toml
├── setup.py
└── .gitignore
```

---

# 🚧 Future Plans

- Merge split files
- Progress bar
- Multi-threaded processing
- Compression support
- Progress percentage display
- Improved error reporting

---

# 📄 License
This project is licensed under the MIT License. See the <a href='https://raw.githubusercontent.com/Lutfifakee-Project/splitxfiles/main/LICENSE'>LICENSE</a> file for details.
