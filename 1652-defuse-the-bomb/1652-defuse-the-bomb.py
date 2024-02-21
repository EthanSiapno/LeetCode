class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        last = len(code) - 1
        output = [0] * len(code)
        kCopy = k
        # if k == 0:
        #     for i in range(0, len(code)):
        #         code[i] = 0
        if k > 0:
            for i in range(0, len(code)):
                while k != 0:
                    if i + k >= len(code):
                        index = i + k - len(code)
                        output[i] += code[index]
                    else:
                        output[i] += code[i+k]
                    k -= 1
                k = kCopy
        if k < 0:
            for i in range(0, len(code)):
                while k != 0:
                    if i - k < 0:
                        index = i + k + len(code)
                        output[i] += code[index]
                    else:
                        output[i] += code[i+k]
                    k += 1
                k = kCopy
        return output
                