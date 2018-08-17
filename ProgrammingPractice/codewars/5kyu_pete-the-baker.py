# https://www.codewars.com/kata/pete-the-baker

def cakes(recipe, available):
    
    how_much_cakes = []
    
    for key, value in recipe.items():
        if key not in available:
            how_much_cakes.append(0)
        else:
            how_much_cakes.append( round(available[key] / value) )
            
    return min(how_much_cakes)