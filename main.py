def calculate_total_sales(sales_totals):
    total = 0
    for sale in sales_totals.values():
        total += sale['quantity'] * sale['price']
    return total

def calculate_average_sales(sales_totals):
    if len(sales_totals) == 0:
        return 0.0
    total = calculate_total_sales(sales_totals)
    return total/len(sales_totals)

def filter_to_better_than_average_sales(sales_totals):
    avg_sales = calculate_average_sales(sales_totals)
    if avg_sales == 0:
        return {}
    sales_better_than_avg = {}
    for item, sales_details in sales_totals.items():
        item_sales = sales_details['quantity']* sales_details['price']
        if item_sales > avg_sales:
            sales_better_than_avg[item] = sales_details
    return sales_better_than_avg

    
def ninety_nine_bottles(count, beverage):
    lyrics = []
    while count > 0:
        if count == 1:
            lyrics.append(f"1 bottle of pop on the wall, 1 bottle of pop")
            lyrics.append(f"If one of those bottles should happen to fall, 0 bottles of pop on the wall")
        else: 
            lyrics.append(f"{count} bottles of pop on the wall, {count} bottles of pop")
            if count == 2: 
                lyrics.append(f"If one of those bottles should happen to fall, 1 bottle of pop on the wall")
            else: 
                lyrics.append(f"If one of those bottles should happen to fall, {count-1} bottles of pop on the wall")
        count -= 1
    return lyrics   
        