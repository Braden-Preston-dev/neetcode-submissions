class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for string in strs:
            for c in string:
                encodedStr += str(ord(c))
                encodedStr += ","
            encodedStr += "/"
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedStrs = [[""] for _ in range(s.count("/") + 1)]
        decodedStrs = s.split("/")
        
        res = []
        for string in decodedStrs:
            decodedStr = string.split(",")
            decodedC = ""
            for s in decodedStr:
                s.strip()
                if s:
                    decodedC += chr(int(s))
            res.append(decodedC)
        res.pop(-1)
        return res