"""Prepare the HSUPipeline site."""

import os
from pathlib import Path
from copy import deepcopy
from shutil import copyfile

###################################################################################################
###################################################################################################

# Define the string definitions of commands to use
CLONE_COMMAND = 'git clone https://github.com/HSUPipeline/{}'
RM_COMMAND = 'rm -rf {}'

# Define repo(s) to copy from
REPO = 'Overview'

# Define what to add to the files
ADD_LINES = [
    '---\n',
    'title: {}\n',
    'layout: page\n',
    'permalink: /{}/\n',
    '---\n',
    '\n'
]

# Define output folder
FOLDER = Path('outputs')

###################################################################################################
###################################################################################################

def main():
    """Main function to manage site creation."""

    # Check for and create (if missing) outputs folder
    if not os.path.exists(FOLDER):
        os.mkdir(FOLDER)

    # Process files to create webpage
    os.system(CLONE_COMMAND.format(REPO))
    create_page(REPO, 'README.md', 'index.md', 'HSUPipeline')
    drop_lines(FOLDER / 'index.md', ['permalink'])
    create_page(REPO, 'Templates.md', 'templates.md', 'Templates')
    create_page(REPO, 'Sorting.md', 'sorting.md', 'Sorting')
    create_page(REPO, 'Converting.md', 'converting.md', 'Converting')
    create_page(REPO, 'Analysis.md', 'analysis.md', 'Analysis')
    create_page(REPO, 'Projects.md', 'projects.md', 'Projects')
    create_page(REPO, 'CodeMap.md', 'codemap.md', 'CodeMap')
    os.system(RM_COMMAND.format(REPO))


def create_page(repo, file_name, page_name, label):
    """Create web page(s) by cloning and copying from a repository.

    Parameter
    ---------
    repo : str
        Repository name.
    file_name  : str or list of str
        File name to copy.
    page_name : str or list of str
        Name to give the webpage.
    label : str or list of str
        Label to add into the header information.
    """

    copyfile(Path(repo) / file_name, FOLDER / page_name)
    update_file(FOLDER / page_name, ADD_LINES, label)


def update_file(filename, add_lines, label):
    """Helper function to update file contents.

    Parameters
    ----------
    filename : str or Path
        Name of the file to load and update.
    add_lines : list of str
        Lines to add to the file.
    label : str
        Label to add into the header information.
    """

    add_lines = deepcopy(add_lines)

    with open(filename, 'r') as file:
        contents = file.readlines()

    # Drop the first couple lines (title gets added from header info)
    contents = contents[2:]

    # Add in header information
    add_lines[1] = add_lines[1].format(label)
    add_lines[3] = add_lines[3].format(label.lower())

    # Add header lines
    for line in reversed(add_lines):
        contents.insert(0, line)

    with open(filename, 'w') as file:
        file.writelines(contents)


def drop_lines(filename, lines_to_drop):
    """Helper function to drop lines from files.

    Parameters
    ----------
    filename : str or Path
        Name of the file to load and update.
    lines_to_drop : list of str
        Lines to drop from the file.
    """

    with open(filename, 'r') as file:
        contents = file.readlines()

    output = []
    for line in contents:

        dropped = False
        for drop in lines_to_drop:
            if drop in line:
                dropped = True
                break
        if not dropped:
            output.append(line)

    with open(filename, 'w') as file:
        file.writelines(output)


if __name__ == "__main__":
    main()
