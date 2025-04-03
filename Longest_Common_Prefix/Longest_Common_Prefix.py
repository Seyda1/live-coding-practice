class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        shortest_string = min(strs, key=len)
        common_prefix = []

        for i in range(len(shortest_string)):
            char = shortest_string[i]

            for word in strs:
                if word[i] != char:
                    return "".join(common_prefix)

            common_prefix.append(char)

        return "".join(common_prefix)
