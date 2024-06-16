def isLongPressedName(self, name: str, typed: str) -> bool:
        ptr = 0
        for i in range(len(name)):
            if ptr >= len(typed) or name[i] != typed[ptr]:
                return False
            if i < len(name)-1 and name[i] == name[i+1]:
                ptr += 1
            else:
                while ptr < len(typed)-1 and typed[ptr] == typed[ptr+1]:
                    ptr += 1
                ptr += 1
        return True if ptr == len(typed) else False
