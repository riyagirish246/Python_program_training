def checkInclusion(s1: str, s2: str) -> bool:
    # If s1 is larger than s2, a permutation cannot exist as a substring
    if len(s1) > len(s2):
        return False
    
    # Initialize frequency arrays for lowercase English letters
    s1_counts = [0] * 26
    s2_counts = [0] * 26
    
    # Populate frequencies for s1 and the first window of s2
    for i in range(len(s1)):
        s1_counts[ord(s1[i]) - ord('a')] += 1
        s2_counts[ord(s2[i]) - ord('a')] += 1
        
    # Check if the initial window matches
    if s1_counts == s2_counts:
        return True
        
    # Slide the window across s2
    for i in range(len(s1), len(s2)):
        # Add the new character entering the window
        s2_counts[ord(s2[i]) - ord('a')] += 1
        # Remove the old character leaving the window
        s2_counts[ord(s2[i - len(s1)]) - ord('a')] -= 1
        
        # Check if the updated window matches s1's character profile
        if s1_counts == s2_counts:
            return True
            
    return False
