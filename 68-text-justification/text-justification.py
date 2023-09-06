class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        line_list = []
        words_in_line = []

        current_wordcount = 0
        current_width = 0
        current_line = ''

        for w in words:

            # only if no word is in line already
            if len(w) == maxWidth and current_wordcount == 0:
                line_list.append(w)
                words_in_line.append(1)
                continue
            if len(w) + 1 + current_width <= maxWidth:
                if current_line == '':
                    current_line += w
                    current_width += len(w) 
                else:
                    current_line += ' ' + w
                    current_width += 1 + len(w)  
                current_wordcount += 1
                # go to next word
                continue

            # does not fit
            else:
                # add the line to the list and reset
                line_list.append(current_line)
                words_in_line.append(current_wordcount)
                current_wordcount = 1
                current_line = w
                current_width = len(w)
        
        # add last line to list
        if current_line:
            line_list.append(current_line)
            words_in_line.append(current_wordcount)

        justified_list = []
        for i, (l, wc) in enumerate(zip(line_list, words_in_line)):

            # last line
            if i == len(line_list) - 1:
                justified_list.append(l + ' ' * (maxWidth - len(l))) 
                break

            words = l.split()
            number_spaces = wc - 1
            if number_spaces > 0:

                # number of spaces between each word
                space = (maxWidth - len(l)) // number_spaces

                # number of spaces which have space + 1 size
                extra_space = (maxWidth - len(l)) % number_spaces

                justified_line = words[0]
                for j, w in enumerate(words[1:]):
                    if j < extra_space: 
                        # + 2 because its + 1 from extra_space and + 1 to have the initial ' '
                        justified_line += ' ' * (space + 2) + w
                    else:
                        justified_line += ' ' * (space + 1) + w
                    
                justified_list.append(justified_line) 

            else:
                # only one word
                justified_list.append(l + ' ' * (maxWidth - len(l))) 

        return justified_list


