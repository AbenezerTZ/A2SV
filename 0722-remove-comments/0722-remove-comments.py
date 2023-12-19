class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        result = []
        is_opened = False
        case = ""
        for line in source:
            i = 0
            while i < len(line):
                if line[i:i+2] == '/*' and not is_opened:
                    is_opened = True
                    i += 1
                elif line[i:i+2] == '*/' and is_opened:
                    is_opened = False
                    i += 1
                elif line[i:i+2] == '//' and not is_opened:
                    break
                elif not is_opened:
                    case += line[i]
                i += 1

            if case and not is_opened:
                result.append(case)
                case = ""

        return result
        