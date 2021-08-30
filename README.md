# Git Updater

This a `python3 script` that updates all your git repositories with only one execution.

## Instructions

1. Have [python3](https://www.python.org/downloads/) and [git download](https://git-scm.com/downloads) in your PC.
2. Fill the `paths.txt` file with all the relative paths *(all of them from this folder)* of all the repositories that you want to update when executing this script.
3. Run in console `python main.py` and see the magic happen.

## Example

If your directories looks like this:

```MD
Folder_1/
    git-updater/
        main.py
        paths.txt
        ...
    repo_1/
        main.rb
        ...
Folder_2/
    repo_2/
        index.js
```

Then your `paths.txt` file should look like this:

```MD
repo_1
../Folder_2/repo_2
```
