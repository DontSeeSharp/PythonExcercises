"""EX11."""
import re


def ex1_solution(input_string):
    """Check if string is a binary number."""
    if re.match("[0-1]*$", input_string) is None:
        return False
    else:
        return True


def ex2_solution(input_string):
    """check if binary number is divisible by 2."""
    if re.search("1$", input_string) is None:
        return True
    else:
        return False


def ex3_solution(input_string):
    """Check if length of input_string is divisible by two."""
    if re.match("^(..)*$", input_string) is not None:
        return True
    else:
        return False


def ex4_solution(input_string):
    """Check if inpput_string contains '0110' or '1001'."""
    if re.search("0110|1001", input_string) is None:
        return False
    else:
        return True


def ex5_solution(input_string):
    """Check if input_string contains 0110 and 1001."""
    if re.search("1001(.)*(0110)|0110(.)*1001|011001|100110",
                 input_string) is None:
        return False
    else:
        return True


def ex6_solution(input_string):
    """Check if string contains 'kastiauto ratas' or 'kasti auto ratas' or 'kasti-auto ratas'."""
    if re.match(
            "kastiauto ratas|kasti auto ratas|kasti-auto ratas", input_string) is not None:
        return True
    else:
        return False


def ex7_solution(input_string):
    """Check if string consists of 3 or 4 words."""
    if re.search("^\w+\s\w+\s\w+.?$|^\w+\s\w+\s\w+\s\w+.?$",
                 input_string) is not None:
        return True
    else:
        return False


def ex8_solution(input_string):
    """Check if there are maximum of 2 words between word 'kass' and 'koer'."""
    if re.search("kass(\s|\s\w+\s|\s\w+\s\w+\s)koer",
                 input_string) is not None:
        return True
    else:
        return False


def ex9_solution(input_string):
    """Check if it's correct representation of 24 hour clock."""
    if re.match("[1]?[0-9]:[0-5][0-9]$|[2]?[0-3]:[0-5][0-9]$",
                input_string) is not None:
        return True
    else:
        return False


def ex10_solution(input_string):
    """Check if string represents correct DNA sequence."""
    if re.search(
            "ATG([ACGT]{3}){1,}(TAA|TAG|TGA)", input_string) is not None:
        return True
    else:
        return False


def ex11_solution(input_string):
    """Check if string represents correct US dollar representation."""
    if re.search(
            "\$(?!([\d]{1,3}(\.|,|\s|$)))|,((?![\d]{3}(\.|,|\s|$)))|\.(?!([\d]{2}(\s|$)))|^\d|^\w", input_string) is not None:

        return False
    else:
        return True


def ex12_solution(input_string):
    """Check if string contains even number of 0's."""
    if re.match("(1*01*01*)*$|1*$", input_string) is not None:
        return True
    else:
        return False


def ex13_solution(input_string):
    """Check if there are not any occurences of 11 or 00 in binary number string."""
    if re.search("00|11", input_string) is not None:
        return False
    else:
        return True


def ex14_solution(input_string):
    """Check if there is kastiauto ratas or kasti auto ratas or kasti-auto ratas, which is followed by price in dollars."""
    if re.search(
            "(kastiauto ratas |kasti auto ratas |kasti-auto ratas )[\w\s]*(\s?\$[\d]+)", input_string) is not None:
        return True
    else:
        return False


def ex15_solution(input_string):
    """Check if binary number in string is divisibly by 3."""
    if re.match("(1(01*0)*1|0)*$", input_string) is not None:
        return True
    else:
        return False
print(ex15_solution("11011"))
