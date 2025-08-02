from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the list is empty, return an empty string immediately
        if not strs:
            return ""
        # Assume the first string is the longest possible common prefix
        prefix = strs[0]
        # Compare the current prefix against each string in turn
        for s in strs[1:]:
            # While the string does not start with the prefix,
            # shorten the prefix by one character from the end
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                # If we have reduced it to empty, no common prefix exists
                if not prefix:
                    return ""
        return prefix

if __name__ == "__main__":
    sol = Solution()
    tests = [
        # (input list of strings, expected output)
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"],   ""),
        ([],                           ""),  # test empty list
        (["a"],                        "a"), # test single-element list
        (["cir", "car"],              "c"),
    ]

    for i, (inp, expect) in enumerate(tests, 1):
        out = sol.longestCommonPrefix(inp)
        status = "✅" if out == expect else f"❌ expected '{expect}'"
        print(f"Case {i}: strs={inp} → out='{out}' {status}")
