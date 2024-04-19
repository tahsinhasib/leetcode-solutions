class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        size = len(s)

        for i in range(0, size):
            if len(list) == 0:
                list.append(s[i])
            elif s[i] == ')' and list[-1] == '(':
                list.pop()
            elif s[i] == '}' and list[-1] == '{':
                list.pop()
            elif s[i] == ']' and list[-1] == '[':
                list.pop()
            else:
                list.append(s[i])

        if len(list) == 0:
            return True
        else:
            return False