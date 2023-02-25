class Solution:
    def simplifyPath(self, path: str) -> str:
        path_units = path.split("/")
        path_stack = []
        
        for path_unit in path_units:
            if path_unit == "..":
                if path_stack: path_stack.pop()
            elif path_unit == ".":
                pass
            elif path_unit == "":
                pass
            else:
                path_stack.append(path_unit)
        
        
        return "/" + "/".join(path_stack)
        
        
#10min
#2sub
                