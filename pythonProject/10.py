def longestSubstring(s: str):
    # To keep track of the last
    # index of each xor
    n = len(s)
    index = dict()

    # Initialize answer with 0
    answer = 0

    mask = 0
    index[mask] = -1

    # Now iterate through each character
    # of the string
    for i in range(n):

        # Convert the character from
        # [a, z] to [0, 25]
        temp = ord(s[i]) - 97

        # Turn the temp-th bit on if
        # character occurs odd number
        # of times and turn off the temp-th
        # bit off if the character occurs
        # even number of times
        mask ^= (1 << temp)

        # If a mask is present in the index
        # Therefore a palindrome is
        # found from index[mask] to i
        if mask in index.keys():
            answer = max(answer,
                         i - index[mask])

        # If x is not found then add its
        # position in the index dict.
        else:
            index[mask] = i

        # Check for the palindrome of
        # odd length
        for j in range(26):

            # We cancel the occurrence
            # of a character if it occurs
            # odd number times
            mask2 = mask ^ (1 << j)
            if mask2 in index.keys():
                answer = max(answer,
                             i - index[mask2])

    return answer