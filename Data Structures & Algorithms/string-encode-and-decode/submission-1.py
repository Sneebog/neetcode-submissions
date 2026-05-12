class Solution:

    def encode(self, strs: List[str]) -> str:
        # checknum = len(strs)
        # if checknum < 10:
        #     checknum = '0' + str(checknum)
        # else:
        #     checknum = str(checknum)
        if len(strs) > 0:
            encoded_string = ''

            for i in range(0, len(strs)):
                encoded_string += strs[i]
                if i != len(strs) -1:
                    encoded_string += '#_#'

            return encoded_string
        else:
            return 'null'

    def decode(self, s: str) -> List[str]:
        # checknum =  s[-2:]
        # if checknum[0] == '0':
        #     checknum = int(checknum[1])
        # else:
        #     checknum = int(checknum)
        if s != 'null':
            decoded_list = s.split('#_#')
            return decoded_list
        else:
            return []
