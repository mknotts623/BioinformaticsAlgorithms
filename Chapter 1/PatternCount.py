def parseFile(file):
        ''' parses text file from Rosalind to separate text from pattern and runs PatternCount '''
        lines = [line.rstrip() for line in open(file)]
        pattern = lines.pop()
        text = ''.join(lines)
        print(PatternCount(text, pattern))
def PatternCount(text, pattern):
        ''' finds amount of times pattern appears in text using sliding window method as described
        in text pseudocode, overlaps included

        Parameters:
                text (str): The text in which the pattern is being searched for
                pattern (str): The pattern which is being searched for
        Returns:
                count (int): The amount of times which the pattern occurs in the text
        ''' 
        count = 0
        for i in range(len(text) - len(pattern) + 1):
                subtext = text[i : i + len(pattern)]
                if text[i: i + len(pattern)] == pattern :
                        count += 1
        return count
