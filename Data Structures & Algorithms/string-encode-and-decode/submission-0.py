class Solution:

    def encode(self, strs: List[str]) -> str:
        flags = map(lambda str_: f"{len(str_)}#", strs)
        return "".join(flag + s for flag, s in zip(flags, strs))

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []

        while i < len(s):
            length = ""
            
            while s[i] != "#":
                length += s[i]
                i += 1
            
            length = int(length)
            str_ = ""
            j = i + 1

            while j <= i + length:
                str_ += s[j]
                j += 1

            strs.append(str_)
            i = j

        return strs
