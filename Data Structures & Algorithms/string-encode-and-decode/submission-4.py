class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "\0"
        encoded = "]{]".join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "\0":
            return []
        decoded = s.split("]{]")
        return decoded
