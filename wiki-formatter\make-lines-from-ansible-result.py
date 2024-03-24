def return_next_two_empty_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() and '}' not in line:  
                try:
                    #next_line = next(file, '').strip()  
                    ## we either call next with a second arg -> default value for end of file 
                    ## or we handle the exception that is raised when iterator reaches the end 
                    ## which is more correct, since a single last line is nothing we want in this case 
                    next_line = next(file).strip()
                except StopIteration:
                    yield '', '', False
                    print("...no more lines...")
                    break
                if next_line:  # next line is not empty
                    yield line.strip(), next_line, True  
                else:
                    yield line.strip(), '', False 

def replace_chars(string, chars, replacer):
    for char in chars:
        string = string.replace(char, replacer)
    return string
        
# Example usage
filename = r"C:\Users\burns\Documents\python-stuff\wiki-formatter\content.txt" 
for line1, line2, next_line_non_empty in return_next_two_empty_lines(filename):
    print("Line 1:", line1)
    print("Line 2:", line2)
    print("Next line non-empty:", next_line_non_empty)
    print()
    line1 = replace_chars(line1, [']','[','=','>','{'], '')
    line2 = line2[8:-1]
    ## withough having called strip the indexes are 12:-2
    print(line1, line2)
    print()
    print()
