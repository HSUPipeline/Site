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

# Define what to add to the files
ADD_LINES = [
    '---\n',
    'title: {}\n',
    'layout: page\n',
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

    # Process index file
    os.system(CLONE_COMMAND.format('Overview'))
    copyfile(Path('Overview') / 'README.md', FOLDER / 'index.md')
    update_file(FOLDER / 'index.md', ADD_LINES, 'HSUPipeline')
    os.system(RM_COMMAND.format('Overview'))


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

    # Add header lines
    for line in reversed(add_lines):
        contents.insert(0, line)

    with open(filename, 'w') as file:
        file.writelines(contents)


if __name__ == "__main__":
    main()
