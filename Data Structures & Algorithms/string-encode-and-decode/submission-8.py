class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return "";

        [""]
        # Covert to List[List[Int]] containining ord value of strs
        list_of_ords = []
        for s in strs:
            if len(s) == 0:
                list_of_ords.append([])
            else:    
                list_of_ords.append([ord(x) for x in s])

        [[]]
        # join each Int with , 
        list_of_str = [",".join(list(map(str,each))) for each in list_of_ords]

        print(list_of_str)
        list_of_str = [ each if  len(each) > 0 else "EMPTY_STRING" for each in list_of_str ]
        # join each List[str] with |
        result = "|".join(list_of_str)


        ""
        print(result)
        return result



    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return []
        
        # split by | to get List[str]
        list_of_str = s.split("|")
        
        list_of_str = [ "" if each == "EMPTY_STRING" else each for each in list_of_str ]

        # split each str by , and convert to Int to get List[Int]
        # list_of_ord = [ list(map(int, each.split(","))) for each in list_of_str ]
        list_of_ord = []
        for each in list_of_str:
            if len(each) > 0:
                list_of_ord.append(list(map(int, each.split(","))))
            else:
                list_of_ord.append([])



        # Covert ord/int back to str using chr 
        list_of_str = []
        for each in list_of_ord:
            list_of_str.append("".join([chr(ch) for ch in each]))
        
        return list_of_str