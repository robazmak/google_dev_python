#!/usr/bin/python3 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    # Given a file name for baby.html, returns a list starting
    # with the year string followed by the name-rank strings
    # in alphabetical order.
    # ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    re_year = r'(\d+)(</h3>)'
    re_names = r'(\d+)</td><td>(\w+)?</td><td>(\w+)?</td>'
    name_rank = {}
    final_list = []

    with open(filename, 'r') as f:
        content = f.read()
        year = re.search(re_year, content).group(1)
        final_list.append(year)
        match = re.findall(re_names, content)
    for data in match:
        name_rank[data[1]] = data[0]
        name_rank[data[2]] = data[0]

    alpha_list = sorted(name_rank)
    for name in alpha_list:
        year = name_rank.get(name)
        final_list.append('{name} {year}'.format(name=name, year=year))
    return final_list


def write_to_file(filename, name_list):
    with open(filename + '.summary', 'w') as f:
        for name in name_list:
            f.write(name + '\n')


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    if len(sys.argv) < 2:
        print('usage: babynames.py [file ...] [--summaryfile]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    name_list = extract_names(sys.argv[1])
    if sys.argv[2] == '--summaryfile':
        write_to_file(sys.argv[1], name_list)
    else:
        for name in name_list:
            print(name)

if __name__ == '__main__':
    main()
