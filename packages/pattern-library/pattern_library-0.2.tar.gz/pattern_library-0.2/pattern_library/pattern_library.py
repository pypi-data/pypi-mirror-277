class LetterPatterns:
    def __init__(self):
        self.patterns = {
            'A': self.pattern_a,
            'B': self.pattern_b,
            'C': self.pattern_c,
            'D': self.pattern_d,
            'E': self.pattern_e,
            'F': self.pattern_f,
            'G': self.pattern_g,
            'H': self.pattern_h,
            'I': self.pattern_i,
            'J': self.pattern_j,
            'K': self.pattern_k,
            'L': self.pattern_l,
            'M': self.pattern_m,
            'N': self.pattern_n,
            'O': self.pattern_o,
            'P': self.pattern_p,
            'Q': self.pattern_q,
            'R': self.pattern_r,
            'S': self.pattern_s,
            'T': self.pattern_t,
            'U': self.pattern_u,
            'V': self.pattern_v,
            'W': self.pattern_w,
            'X': self.pattern_x,
            'Y': self.pattern_y,
            'Z': self.pattern_z,
            # Add all other letter functions here...
        }

    def get_pattern(self, letter):
        if letter in self.patterns:
            return self.patterns[letter]()
        else:
            return f"Pattern for {letter} not defined."

    def pattern_a(self):
        result_str = ""
        for row in range(0, 10):
            for column in range(0, 9):
                if ((row == 0 and 2 <= column <= 6) or
                    (row == 1 and (1 <= column <= 7)) or
                    (row == 4 and 0 <= column <= 8) or
                    (row in {2, 3, 5, 6, 7} and (column in {0, 1, 7, 8}))):
                    result_str += 'A'
                else:
                    result_str += " "
            result_str += "\n"
        return result_str

    def pattern_b(self):
        result_str = ""
        for row in range(0, 10):
            for column in range(0, 9):
                if ((row == 0 and 0 <= column <= 7) or 
                    (row in {1,2,4,5} and column in {0,1,7,8}) or 
                    (row in {3,6} and 0 <= column <= 7)):
                    result_str += 'B'
                else:
                    result_str += " "
            result_str += "\n"
        return result_str

    def pattern_c(self):
        result_str = ""
        for row in range(0, 10):
            for column in range(0, 10):
                if ((row in {0, 1, 6, 7} and 5 <= column <= 9) or
                    (row in {1, 2, 5, 6} and 3 <= column <= 5) or
                    (2 <= row <= 5 and column in {1, 2}) or
                    (3 <= row <= 4 and column == 0)):
                    result_str += 'C'
                else:
                    result_str += " "
            result_str += "\n"
        return result_str
    def pattern_d(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((row == 0 and 0 <= column <= 6) or 
                    (row == 1 and 0 <= column <= 8) or 
                    (row == 2 and column in {8,0,1,7,9}) or 
                    (row == 3 and column in {9,8,0,1,10}) or 
                    (row == 4 and column in {0,1,9,10,8}) or 
                    (row == 5 and column in {0,1,9,10,8}) or 
                    (row == 6 and column in {0,1,9,7,8}) or 
                    (row == 7 and 0 <= column <= 8) or
                    (row == 8 and 0 <= column <= 6)):
                    result_str +=  'D'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str'
        return result_str
    def pattern_e(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if  ((column in{0,1}) and (0 <= row <= 8) or 
                     (row in {0,1}) or 
                     (row == 4 and 0 < column < 9) or 
                     (row in {7,8})):
                    result_str +=  'E'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_f(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((column in {0,1}) or 
                    (row in {0,1}) or 
                    (row == 4 or row == 5 and 0 < column < 7)):
                    result_str +=  'F'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_g(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((row in {0,1,7,8} and 3 <= column <= 8) or 
                    (1 <= row <= 7 and column == 2) or 
                    (2 <= row <= 6 and column == 1) or 
                    (2 < row < 6 and column == 0) or 
                    (row in {2,6} and column in {3,4}) or 
                    (4 <= row <= 8 and column in {9,8}) or 
                    (row == 4 and 4 < column < 9)):
                    result_str +=  'G'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_h(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if  ((column in {0,1,7,8} and 0 <= row <= 6) or
                     (row == 3 and column in {0,1,2,3,4,5,6,8})):
                    result_str +=  'H'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_i(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((row in {0,6}) or 
                    (0 < row < 6 and column in {3,4,5})):
                    result_str +=  'I'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_j(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((row == 0) or 
                    (0 < row < 6 and column in {7,8}) or 
                    (row == 6 and 0 < column < 8) or
                    (row == 5 and column == 0)):
                    result_str +=  'J'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_k(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((column in {0,1} and 0 < row < 8) or 
                    (row in {1,7} and column in {6,7,8}) or 
                    (row in {2,6} and column in {4,5,6}) or 
                    (row in {3,5} and column in {3,4,5}) or 
                    (row == 4 and column in {2,3})):
                    result_str +=  'K'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_l(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((column in {0,1} and 0 <= row < 8) or 
                    (row == 7)):
                    result_str +=  'L'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_m(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((column in {0,8} and 0 <= row < 7) or 
                    (row == 0 and column in {1,7,2,6}) or 
                    (row == 1 and column in {6,5,3,2}) or 
                    (row == 2 and column in {3,4,5}) or 
                    (row == 3 and column == 4)):
                    result_str +=  'M'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_n(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((column in {0,8} and 0 <= row < 7)or 
                    (row == 0 and column in {1,2}) or 
                    (row == 1 and column in {2,3}) or 
                    (row == 2 and column in {3,4}) or 
                    (row == 3 and column in {4,5}) or 
                    (row == 4 and column in {5,6}) or 
                    (row == 5 and column in {6,7}) or 
                    (row == 6 and column in {7,8})):
                    result_str +=  'N'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_o(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((row in {0,7} and column in {3,4,5}) or 
                    (row in {1,6} and 1 <= column <= 7) or 
                    (2 <= row <= 5 and column in {0,1,7,8})):
                    result_str +=  'O'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str'
        return result_str
    def pattern_p(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((row in {0,5} and 0 <= column <= 6) or 
                    (row in {1,4} and 0 <= column <= 7) or 
                    (row == 2 and column in {0,1,6,7,8}) or 
                    (row == 3 and column in {0,1,6,7,8}) or  
                    (row in {6,7,8} and column in {0,1})):
                    result_str +=  'P'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_q(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((row in {0,7} and column in {3,4,5}) or 
                    (row in {1,6} and 1 <= column <= 7) or 
                    (2 <= row <= 5 and column in {0,1,7,8}) or 
                    (row in {5,7} and column in {5,8})):
                    result_str +=  'Q'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_r(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if  ((row == 0 and 0 <= column <= 6) or 
                     (row in {1,4,5} and 0 <= column <= 7 ) or   
                     (row in {2,3,6,7,8,9} and column in {0,1,6,7,8})):
                    result_str +=  'R'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_s(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((row in {0,9} and column in {3,4,5}) or 
                    (row in {1,8} and 0 < column < 8) or 
                    (row in {2,3,6,7} and column in {0,1,7,8}) or 
                    (row == 4 and 1 <= column <= 4) or 
                    (row == 5 and 4 <= column <= 7)):
                    result_str +=  'S'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_t(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((row == 0) or 
                    (0 < row < 7 and column in {4,5})):
                    result_str +=  'T'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_u(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((column in {0,1,7,8} and 0 < row < 6) or 
                    (row == 6 and 0 < column < 8) or 
                    (row == 7 and 1 < column < 7)):
                    result_str +=  'U'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_v(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((row == 5 and column in {5,6}) or 
                    (row == 3 and column in {3,4,7,8}) or 
                    (row == 2 and column in {8,9,3,2}) or 
                    (row == 1 and column in {1,2,9,10}) or 
                    (row == 0 and column in {0,1,10,11}) or 
                    (row == 4 and 4 <= column <= 7)):
                    result_str +=  'V'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str'
        return result_str
    def pattern_w(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((row == 0 and column in {0,1,14,13}) or 
                    (row == 1 and column in {1,2,7,12,13}) or 
                    (row == 2 and column in {2,3,5,6,8,9,11,12}) or 
                    (row == 3 and column in {3,4,5,9,10,11})):
                    result_str +=  'W'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_x(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((row in {0,7} and column in {0,1,7,8}) or 
                    (row in {1,6} and column in {1,2,6,7}) or 
                    (row in {2,5} and column in {2,3,5,6}) or 
                    (row in {3,4} and column in {3,4,5})):
                    result_str +=  'X'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    def pattern_y(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if ((row in {0,1} and column in {0,1,7,8}) or 
                    (row == 2 and column in {1,2,6,7}) or 
                    (row == 3 and 2 <= column <= 6) or 
                    (4 <= row <= 6 and column in {3,4,5})):
                    result_str +=  'Y'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str'
        return result_str
    def pattern_z(self):
        result_str = ""
        for row in range(0, 10):
            # R = N[:1];
            for column in range(0, 12):
                if  ((row in {0,6}) or 
                     (row == 1 and column in {7,8}) or 
                     (row == 2 and column in {6,7}) or 
                     (row == 3 and column in {4,5}) or 
                     (row == 4 and column in {2,3}) or 
                     (row == 5 and column in {0,1})):
                    result_str +=  'Z'
                else:
                    result_str += " "  # Append space (' ') to the 'result_str'
            result_str += "\n"  # Add a newline character after each row in 'result_str' 
        return result_str
    # Define other pattern methods similarly...

    def generate_patterns(self, input_str):
        result = ""
        for letter in input_str.upper():
            result += self.get_pattern(letter) + "\n"
        return result

# Example usage
if __name__ == "__main__":
    input_str = input("Type a Letter: ")
    lp = LetterPatterns()
    print(lp.generate_patterns(input_str))
