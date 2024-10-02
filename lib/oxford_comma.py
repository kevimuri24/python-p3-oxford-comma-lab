def oxford_comma(items):
    if len(items) == 2:
        str = f"{items[0]} and {items[1]}"
        return str
    if len(items) > 2:
        str = ', '.join(items[:-1]) + ', and '+ items[-1]
        return str
    else:
        return items[0]

