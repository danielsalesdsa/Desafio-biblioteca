#importar uma biblioteca 
from chempy import balance_stoichiometry
reactants, products = balance_stoichiometry({'H2', 'O2'}, {'H2O'})
print(reactants, products)  # {'H2': 2, 'O2': 1} {'H2O': 2}