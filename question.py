def remove_palindromic_words(s):
    n = len(s)
    result = ""
    i = 0

    while i < n:
        found_palindrome = False
        # Try to find the longest palindrome starting at i
        for j in range(n, i + 1, -1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > 1:
                # Skip this palindrome
                i = j
                found_palindrome = True
                break
        if not found_palindrome:
            result += s[i]
            i += 1
    return result


# Example usage

concatenated = "TATTARRATTATFREDIVIDERODETARTRATEDLKAYAKRACECARLROTAVATOROCIVICWMADAMIMADAMMLEVELRRACECARCREDDERAREPAPERTMALAYALAMCSTATSODEIFIEDDPEEPEWOWSMINIMIOTTONANNAIGIGNMOMSREIFIERTMADAMAOPPO"

cleaned = remove_palindromic_words(concatenated)
print("Original:", concatenated)
print("Without palindromes:", cleaned)
