class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ops = {'+','-','*','/'}


        for c in tokens:
            if c not in ops:
                st.append(c)
            elif st and c in ops:
                s = int(st.pop())
                f = int(st.pop())
                if c == '+':
                    r = str(f + s)
                    st.append(r)
                elif c == '*':
                    r = str(f * s)
                    st.append(r)
                elif c == '-':
                    r = str(f - s)
                    st.append(r)
                elif c == '/':
                    r = str(int(f / s))
                    st.append(r)
        return int(st[0])
