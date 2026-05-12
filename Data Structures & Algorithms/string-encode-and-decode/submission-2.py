class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) > 0:
            return '#_#'.join(strs)
        else:
            return 'null'
    def decode(self, s: str) -> List[str]:
        if s != 'null':
            decoded_list = s.split('#_#')
            return decoded_list
        else:
            return []