"""
Ce module teste si une chaîne de caractères est un palindrome.
"""
def ispalindrome(s):
    """
    Cette fonction teste si une chaîne de caractères est un palindrome.
    
    :param s: La chaîne de caractères
    :return: True si la chaîne est un palindrome, sinon False
    """
    translation_table = str.maketrans("éèêëêçùàôÂÊÎÔÛÄËÏÖÜÀÉÈÙ", "eeeeecuaoAEIOUAEIOUAEEU")
    # Nettoyer la chaîne : enlever les espaces et mettre tout en minuscules
    ponctuation="()[]{},?!;'.:-"
    ponctuation_table=str.maketrans('','',ponctuation)
    s = s.translate(ponctuation_table)
    s = s.translate(translation_table)
    s = ''.join(s.split()).lower()
    return s == s[::-1]  # Retourne True si s est un palindrome, sinon False

def main():
    """
    Fonction principale pour tester plusieurs chaînes de caractères
    afin de déterminer si elles sont des palindromes.
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s,ispalindrome(s))
if __name__ == "__main__":
    main()
