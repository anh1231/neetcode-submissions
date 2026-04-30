class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            for i in s:
                code = ord(i) + 42
                encoded += chr(code)
            encoded += '//'
        return encoded
        
    def decode(self, s: str) -> List[str]:
        split = s.split('//')[:-1]
        decoded = []
        for s in split:
            word = ''
            for i in s:
                decode = chr(ord(i) - 42)
                word += decode
            decoded.append(word)
        return decoded