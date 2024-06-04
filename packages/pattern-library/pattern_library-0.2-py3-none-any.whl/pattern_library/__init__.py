# pattern_library/__init__.py
from pattern_library import LetterPatterns

lp = LetterPatterns()
input_str = input("Enter your letters/statement: ")
print(lp.generate_patterns(input_str))
