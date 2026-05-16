class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "\n"
        encoded = "]{]".join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "\n":
            return []
        decoded = s.split("]{]")
        return decoded
