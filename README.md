## Lab 1 - Filesystem

For this lab, you will be practicing manipulating files on the filesystem using the terminal.

In this directory you'll find:

- README.md - this file
- check.py - a python script that checks if your directory structure looks as expected
- files/ - a directory with a bunch of text files mixed up

At any point you may type "./check.py" from this directory and you will see a description of your progress.

TODO: example output

Tips:

- Do not rush through to the "brute force" solution, consider what keyboard shortcuts, globs, etc. will be helpful. The goal is to gain familiarity with the terminal.
- Run "./check.py" after each step to ensure that you didn't miss anything.

### Part 0: Explore `files/`

Take a look at the `files/` directory provided. Use `ls`, `cd`, and `cat` to examine the files.

You should discover that there are files about animals, planets, and computer scientists all mixed up.

Our goal today is going to be reorganizing these files.

### Part 1: Making Directories

We'll want to create a few directories:

- `animals/` - to contain all files on animals
- `people/` - to contain all files on people
- `space/` - which will have two subdirectories
  - `space/planets`
  - `space/comets`

Use the `mkdir` command to create all of these directories.

Run `./check.py` (from the `filesystem-lab` directory) when ready.

### Part 2: Moving Files

Next, you will need to move files into place, `check.py` will assume you follow this order:

- Move people first.
- Then animals.
- Then comets. All comets start with

Tip: if in doubt based on a file name, use `cat` to view the contents.

Run `./check.py` (from the `filesystem-lab` directory) when ready.

### Part 3: Editing Files

Each file in `planets/` contains a line "moons: N" (where N is a number of moons).

You'll need to make the following changes:

- Jupiter had three new moons confirmed in 2023, so update Jupiter to have 95 moons instead of 92.
- There is no `venus.txt`. Venus has no moons. Add a new file for Venus, with "moons: 0".
