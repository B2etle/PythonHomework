"""When importing the module 'mod_b.py' in the module 'mod_a.py', it changes the value of the variable 'x' in the
imported module 'mod_c.py', which is also imported into the module 'mod_a.py' and is a common object for these modules.
The code of the imported module is executed earlier than the main module, and at the time the value of the variable 'x'
in the module 'mod_a.py' is output, it has already been changed."""
