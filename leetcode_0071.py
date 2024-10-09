class Solution:
    def simplifyPath(self, path: str) -> str:
        exceptions = {
            '.': True,
            '..': True,
            "": True  # // => [""]
        }

        path = path.split('/') # O(n)
        simplePath = ['/']

        for p in path:
            if p not in exceptions:
                simplePath.append(p + '/')
            elif p == '..' and len(simplePath) > 1:
                simplePath.pop()

        if len(simplePath) == 1:  # simplePath = ['/']
            # add extra slash that remove in next step for root exception
            simplePath.append('/')

        return "".join(simplePath)[:-1] # O(n)
