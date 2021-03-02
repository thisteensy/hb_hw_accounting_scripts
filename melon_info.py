"""Print out all the melons in our inventory."""


from melons import melons_dict


def print_melon(name, attributes):
    """Print each melon with corresponding attribute information."""

    # have_or_have_not = 'have'
    # if attributes['seedlessness']:
    #     have_or_have_not = 'do not have'
    print(f'{name}s')
    for attribute, value in attributes.items():
        print(f'    {attribute}: {value}')

for melon, attributes in melons_dict.items():
    print_melon(melon, attributes)
# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
