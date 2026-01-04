from typing import Dict, List

def addPropertiesToLand(properties, rows, propertyPerRow) -> None:
    data = {}
    item_index = 0

    for row in range(1, rows + 1):
        row_key = f'row{row}'
        data[row_key] = []
        
        for _ in range(propertyPerRow):
            if item_index < len(properties):
                data[row_key].append(properties[item_index])
                item_index += 1
    
    return data

# Example usage
properties = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7']
rows = 4
propertyPerRow = 2

data = addPropertiesToLand(properties, rows, propertyPerRow)
print(data)

def calculatePropertyPerRow(sqFt: int) -> None:
    if total_items < 4 or total_items > 16:
        raise ValueError("The number of items must be between 4 and 16.")

    # Calculate the square root and round up to determine the number of rows
    import math
    rows = math.ceil(math.sqrt(total_items))
    items_per_row = math.ceil(total_items / rows)

    return rows, items_per_row

# Example usage
total_items = 7
rows, items_per_row = calculatePropertyPerRow(total_items)
print(f'Number of rows: {rows}')
print(f'Number of items per row: {items_per_row}')

def heapStack(propertyElevation: List[int], userInput: int) -> None:
    environment: Dict[int, List[int]] = {}
    landProperties = range(4)

    for landProperty in landProperties:
        environment[landProperty] = []

    print(environment)

print(heapStack([1,1,2,3], 0))