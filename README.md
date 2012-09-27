# Arthur

At my current occupation, forms such as testing documentation and 
walkthrough forms are created using Microsoft Word and saving to HTML. This 
leads to a number of issues, from differences in how a document looks between 
browsers and Word to constantly having to fight with Word's kludgy indenting 
and table width rules. I was convinced a better way existed. `Arthur` is an 
experiment in this direction.

Once installed, `arthur` can initialize a directory by typing the following:

    python /path/to/arthur/arthur_main.py init

This will create the following hierarchy:

    ├── output/
    ├── refresh_docs.py
    ├── settings.py
    └── templates/
        ├── Program Specifications.html
            ├── base.html
                └── main.css

Running `python refresh_docs.py` will read settings.py to link a template file 
like `Program Specifications.html` with a Python dictionary. This dictionary 
will define all the variables inside the template. `Arthur` simply combines the 
two and renders out the result to the `output` directory. This simple workflow
allow you to set up a default set of templates and options, and then set them up
in multiple folders, changing the options as you go. After rendering the initial
pass, if you need to change anything, just change settings.py and rerun
`refresh_docs.py`. If you want to keep notes, you can do that via python
comments (starting a line with '#').

This project is still in its infancy. Please feel free to try it out, and notify
me of any issues that come up. As I said, this is an experiment, so changes in
this workflow may appear at any time. Please check this README for any
updates.
