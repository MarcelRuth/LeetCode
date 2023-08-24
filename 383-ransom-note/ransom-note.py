class Solution:
    def canConstruct(self, rsn: str, magazine: str) -> bool:
        # logical but slow way

        # ransomNote = []
        # for c in rsn:
        #     ransomNote.append(c)
        # found = 0
        # target = len(ransomNote)

        # # go through all letters in magazine
        # for letter in magazine:
        #     # if the letter is in ransomNote and has not been found yet
        #     if letter in ransomNote:
        #         # remove the letter from ransomNote
        #         ransomNote.remove(letter)
        #         found += 1
        #         print(len(ransomNote))

        # if found == target:
        #     return True
        # else:
        #     return False

        # use counters

        # Create Counter objects for the ransomNote and magazine strings
        note, mag = Counter(rsn), Counter(magazine)
        
        # creates two dictionarys that have the letters as keys and the frequency as value
        # such as, Counter("aab") would return a dictionary {'a': 2, 'b': 1}.

        # Check if the intersection of note and mag Counter objects is equal to note Counter object
        # If it is, it means that all the letters in ransomNote can be formed using the letters in magazine
        if note & mag == note: 
            return True
        else:
            return False