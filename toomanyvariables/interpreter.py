import re
import sys

def parse_TMV(codeString):
    """Parse codeString as Too Many Variables! code and return a nested
    list that's easier to work with.
    """
    textLines = codeString.splitlines()
    codeLines = []
    for lineNum, line in enumerate(textLines, 1):
        # Check for correct syntax
        if re.fullmatch(r'\d+=\d+[+\-*/]\d+', line) is None:
            raise SyntaxError(f'Line {lineNum}: Line ({line}) should have '
                               'format <number>=<number><op><number>')
        # Get leftHandSide, firstOperand, operator, and secondOperand
        leftHandSide, rightHandSide = line.split('=')
        operator = re.search(r'[+\-*/]', rightHandSide).group(0)
        firstOperand, secondOperand = rightHandSide.split(operator)
        # Make sure the variables are all valid
        if re.fullmatch(r'0([1-9]\d*|00)', leftHandSide) is not None:
            raise SyntaxError(f'Line {lineNum}: Cannot assign to literal '
                              f'{leftHandSide}')
        for variable in [leftHandSide, firstOperand, secondOperand]:
            if re.fullmatch(r'00([1-9]|0\d)\d*', variable) is not None:
                raise NameError(f'Line {lineNum}: Variable ({variable}) is '
                                 'illegal')
        # The line is valid code--add it in!
        codeLines.append([leftHandSide, firstOperand, operator, secondOperand])
    return codeLines

def run_TMV(parsedCode):
    """Run code from Too Many Variables! that has been parsed by
    parse_TMV().
    """
    variableDict = {'0': '', '00': 1}
    numLines = len(parsedCode)
    while variableDict['00'] in range(1, numLines + 1):
        # Get the current line
        line = parsedCode[variableDict['00'] - 1]
        # Get the variables
        operands = []
        for variable in (line[1], line[3]):
            if variable == '0': # Input
                operands.append(ord(sys.stdin.read(1)))
            elif re.fullmatch(r'0[1-9]\d*', variable): # Literal integer
                operands.append(int(variable.removeprefix('0')))
            elif variable == '000': # Literal 0
                operands.append(0)
            else: # Variable
                try:
                    operand = variableDict[variable]
                except KeyError:
                    raise NameError(f'Line {variableDict["00"]}: Variable '
                                    f'{variable} is not defined') from None
                else:
                    operands.append(operand)
                    
        operator = line[2]
        if operator == '+':
            result = operands[0] + operands[1]
        elif operator == '-':
            result = operands[0] - operands[1]
        elif operator == '*':
            result = operands[0] * operands[1]
        elif operator == '/':
            if operands[1] == 0:
                result = 0
            else:
                result = operands[0] // operands[1]

        assignee = line[0]
        if assignee == '0':
            try:
                printedChar = chr(result)
            except ValueError:
                raise ValueError(f'Line {variableDict["00"]}: Codepoint '
                                 f'U{result:+04X} invalid') from None
            else:
                print(printedChar, end='')
                variableDict['00'] += 1
        elif assignee == '00':
            variableDict['00'] = result
        else:
            variableDict[assignee] = result
            variableDict['00'] += 1