class Solution:
    def simplifyPath(self, path: str) -> str:
        simplifiedPath = []
        paths = path.split("/")

        for cur in paths:
            if cur == "..":
                if simplifiedPath:
                    simplifiedPath.pop()
            elif cur != "" and cur != ".":
                simplifiedPath.append(cur)

        return "/" + "/".join(simplifiedPath)