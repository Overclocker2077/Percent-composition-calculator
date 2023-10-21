import re

# element key : paired with atomic mass
periodicTable_atomic = {
    "H": 1.00797,
    "He": 4.00260,
    "Li": 6.941,
    "Be": 9.01218,
    "B": 10.81,
    "C": 12.011,
    "N": 14.0067,
    "O": 15.9994,
    "F": 18.998403,
    "Ne": 20.179,
    "Na": 22.98977,
    "Mg": 24.305,
    "Al": 26.98154,
    "Si": 28.0855,
    "P": 30.97376,
    "S": 32.06,
    "Cl": 35.453,
    "K": 39.0983,
    "Ar": 39.948,
    "Ca": 40.08,
    "Sc": 44.9559,
    "Ti": 47.90,
    "V": 50.9415,
    "Cr": 51.996,
    "Mn": 54.9380,
    "Fe": 55.847,
    "Ni": 58.70,
    "Co": 58.9332,
    "Cu": 63.546,
    "Zn": 65.38,
    "Ga": 69.72,
    "Ge": 72.59,
    "As": 74.9216,
    "Se": 78.96,
    "Br": 79.904,
    "Kr": 83.80,
    "Rb": 85.4678,
    "Sr": 87.62,
    "Y": 88.9059,
    "Zr": 91.22,
    "Nb": 92.9064,
    "Mo": 95.94,
    "Tc": 98,
    "Ru": 101.07,
    "Rh": 102.9055,
    "Pd": 106.4,
    "Ag": 107.868,
    "Cd": 112.41,
    "In": 114.82,
    "Sn": 118.69,
    "Sb": 121.75,
    "I": 126.9045,
    "Te": 127.60,
    "Xe": 131.30,
    "Cs": 132.9054,
    "Ba": 137.33,
    "La": 138.9055,
    "Ce": 140.12,
    "Pr": 140.9077,
    "Nd": 144.24,
    "Pm": 145,
    "Sm": 150.4,
    "Eu": 151.96,
    "Gd": 157.25,
    "Tb": 158.9254,
    "Dy": 162.50,
    "Ho": 164.9304,
    "Er": 167.26,
    "Tm": 168.9342,
    "Yb": 173.04,
    "Lu": 174.967,
    "Hf": 178.49,
    "Ta": 180.9479,
    "W": 183.85,
    "Re": 186.207,
    "Os": 190.2,
    "Ir": 192.22,
    "Pt": 195.09,
    "Au": 196.9665,
    "Hg": 200.59,
    "Tl": 204.37,
    "Pb": 207.2,
    "Bi": 208.9804,
    "Po": 209,
    "At": 210,
    "Rn": 222,
    "Fr": 223,
    "Ra": 226.0254,
    "Ac": 227.0278,
    "Th": 232.0381,
    "Pa": 231.0359,
    "U": 238.029,
    "Np": 237.0482,
    "Pu": 242,
    "Am": 243,
    "Cm": 247,
    "Bk": 247,
    "No": 250,
    "Cf": 251,
    "Es": 252,
    "Hs": 255,
    "Mt": 256,
    "Fm": 257,
    "Md": 258,
    "Lr": 260,
    "Rf": 261,
    "Bh": 262,
    "Db": 262,
    "Sg": 263,
    "Uun": 269,
    "Uuu": 272,
    "Uub": 277
}
def compound_formula_parser(formula):
    elements_and_total_atoms = {}
    current_element = ""
    current_count = 0

    i = 0
    while i < len(formula):
        char = formula[i]

        if char.isupper():
            if current_element:
                elements_and_total_atoms[current_element] = current_count if current_count else 1
            current_element = char
            current_count = 0
        elif char.islower():
            current_element += char
        elif char.isnumeric():
            count_str = char
            while i + 1 < len(formula) and formula[i + 1].isnumeric():
                i += 1
                count_str += formula[i]
            current_count = int(count_str)
        elif char == '(':
            j = i + 1
            while j < len(formula) and formula[j] != ')':
                j += 1
            sub_formula = formula[i + 1:j]
            i = j
            sub_elements = compound_formula_parser(sub_formula)
            count_str = ""
            while j + 1 < len(formula) and formula[j + 1].isnumeric():
                j += 1
                count_str += formula[j]
            count = int(count_str) if count_str else 1
            for element, sub_count in sub_elements.items():
                elements_and_total_atoms[element] = elements_and_total_atoms.get(element, 0) + sub_count * count
        i += 1

    if current_element:
        elements_and_total_atoms[current_element] = current_count if current_count else 1

    return elements_and_total_atoms

def calculate_percent_composition(formula):
    elements_and_total_atoms = compound_formula_parser(formula)
    total_atomic_mass = sum(periodicTable_atomic[element] * count for element, count in elements_and_total_atoms.items())
    percent_composition = {element: (periodicTable_atomic[element] * count / total_atomic_mass) * 100 for element, count in elements_and_total_atoms.items()}
    return percent_composition

formula = input("Enter a chemical formula: ")
result = calculate_percent_composition(formula)
print(result)
