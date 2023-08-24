class Solution:
    def canConstruct(self, rsn: str, magazine: str) -> bool:
    
        ransomNote = []
        for c in rsn:
            ransomNote.append(c)
        found = 0
        target = len(ransomNote)
        
        # go through all letters in magazine
        for letter in magazine:
            # if the letter is in ransomNote and has not been found yet
            if letter in ransomNote:
                # remove the letter from ransomNote
                ransomNote.remove(letter)
                found += 1
                print(len(ransomNote))

        if found == target:
            return True
        else:
            return False