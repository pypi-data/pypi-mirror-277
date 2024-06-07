<p align="center">
  
<a href="https://github.com/netblag/jupyter-notebook-fixer/tree/main" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg" alt="jupyter" width="100" height="100"/>

---
# Updating Notebook Version

## Introduction
In the world of data and computer science, Jupyter Notebook serves as one of the primary tools for data analysis and executing Python code. However, sometimes we encounter issues that result in corruption of notebook files, making it difficult to open or reuse them. This project is created to address this problem and update Jupyter Notebook files to a newer version.

## Problem
Sometimes, you may have a set of .ipynb files that are corrupted due to various reasons or fail to open properly due to the use of older versions. This issue can lead to data loss, incomplete analyses, and wasted valuable time. In such situations, manually inspecting and correcting each notebook file is time-consuming and tiresome.

## Solution
This project provides a simple and efficient script to update and fix all notebook files in a directory. The script automatically updates .ipynb files to version 4 and attempts to recover the file content and create a new notebook if an error occurs while reading the file. This approach ensures that all your notebook files are up-to-date and usable.
----

### Sometimes, you might have a bunch of corrupted .ipynb files that seem to be time-consuming to fix manually. Instead of going through each file one by one, you can place all `.ipynb files in a folder` and use this script to fix them all at once.
***

## How it works

- #### 1. List Files: The script lists all files and folders in the provided directory.

- #### 2. Find Notebooks: For each file found, it checks if it ends with '.ipynb'.

- #### 3. Open and Read: If it's a notebook file, it opens and reads the file using nbformat.

- #### 4. Update Version: It updates the notebook to version 4.

- #### 5. Save Changes: The updated notebook is then saved with version 4.
***

## Requirements

- #### Python: Ensure `Python` is installed on your system.

- #### Jupyter Notebook: The script relies on nbformat module, which is part of the Jupyter ecosystem. Make sure Jupyter is installed:
```sh
pip install jupyter
```


***


<p align="center">
  <a href="https://github.com/netblag">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/github/ccc?viewbox=auto" />
      <source media="(prefers-color-scheme: light)" srcset="https://cdn.simpleicons.org/github?viewbox=auto" />
      <img alt="GitHub" height="90" src="https://cdn.simpleicons.org/github?viewbox=auto" />
    </picture>
  </a>
  
