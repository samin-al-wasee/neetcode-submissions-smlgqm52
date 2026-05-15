class Solution:

    def encode(self, strs: List[str]) -> str:
        flags = map(lambda str_: f"{len(str_)}#", strs)
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            end = start + length

            res.append(s[start:end])
            i = end

        return res
