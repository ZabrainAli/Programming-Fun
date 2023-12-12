class strStr:
    def __init__(self, haystack, needle):
        self.haystack = haystack
        self.needle = needle

    def find_occurence(self):
        for i in range(len(self.haystack) - len(self.needle) + 1):
            if self.haystack[i:i+len(self.needle)] == self.needle:
                return i
        return -1