from RemoveDuplicates import RemoveDuplicates
from strStr import strStr
def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    nums_no_dupes = RemoveDuplicates(nums)
    print(nums_no_dupes.nums)

    haystack = "leetcode"
    needle = "leeto"

    print(strStr(haystack, needle).find_occurence())    
    
main()