

def divided_by(t, m) -> int:
    amount = 0
    
    for element in t:
        if element % m == 0:
            amount += 1
    
    return amount



