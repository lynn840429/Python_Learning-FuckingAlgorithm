S = "ADOBECODEBANC"
T = "ABC"


def find_min_string(s="", t=""):
    res = s
    t_sorted = ''.join(sorted(t))

    for i in range(len(s)+1):
        for j in range(i+1, len(s)+1, 1):
            s_sorted = ''.join(sorted(set(s[i:j])))
            if (s_sorted.find(t_sorted)!=-1) and(len(s_sorted)<len(res)):
                    res = s_sorted
    
    return res

print(find_min_string(S, T))