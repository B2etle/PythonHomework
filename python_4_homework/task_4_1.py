def sortnames():
    """Sort the names and write them to a new file."""
    with open(r'data/unsorted_names.txt', 'r') as file_unsorted:
        with open(r'data/sorted_names.txt', 'w') as file_sorted:
            file_sorted.write(''.join(sorted(file_unsorted.readlines())))
