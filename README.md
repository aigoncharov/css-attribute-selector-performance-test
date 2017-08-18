# css-tag-selector-test

## Usage
```
python3 generator.py [--is_tag] [--no_apply_css] [--block_num=10] [--css_rule_num=10] [--file_name="index.html"]
```
is_tag - forces the generator to create styles with tag selectors (classes are used by default)
no_apply_css - leaves DOm elements unstyled (emply classes, no tags applied)

## What does it do?
generator.py produces an HTML file with a number (specified in block_num) of div blocks inside. A set of classes or tags (depending on is_tag switch) is generated as well. Each CSS rule sets background-color porperty.

## Purpose
This script is created to generate a handful amount of html files with various number of CSS rules and div elements to compare perfomance of tag selectors and class selectors. 