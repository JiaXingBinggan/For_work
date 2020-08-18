import sys

if __name__ == '__main__':
    while True:
        try:
            s1 = sys.stdin.readline().strip()
            if not s1:
                break
            s2 = sys.stdin.readline().strip()
            n1 = len(s1)
            n2 = len(s2)


            def match(i, j):
                if i == n1 - 1 and j == n2 - 1 and s1[i] == s2[j]:
                    return True
                elif i == n1 - 1 or j == n2 - 1:
                    return False
                elif s1[i] == '?':
                    return match(i + 1, j + 1)
                elif s1[i] == '*':
                    return match(i + 1, j) or match(i + 1, j + 1) or match(i, j + 1)
                elif s1[i] == s2[j]:
                    return True

                return False


            i, j = 0, 0
            is_compare = True
            while i < n1 and j < n2 and is_compare:
                if not match(i, j):
                    is_compare = False
                i += 1
                j += 1
            if is_compare:
                print('true')
            else:
                print('false')
        except:
            pass