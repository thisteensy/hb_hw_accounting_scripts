"""Print out all the melons in our inventory."""


from melons import melons_dict


def print_melon(name, attributes):
    """Print each melon with corresponding attribute information."""

    print(f'{name}s')
    for attribute, value in attributes.items():
        print(f'    {attribute}: {value}')

for melon, attributes in melons_dict.items():
    print_melon(melon, attributes)

