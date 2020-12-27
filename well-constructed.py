# well-structured
# 1. start with consonant
# The 21 consonant letters in the English alphabet are B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z, and usually Y.
# 2. does not contain two consecutive vowels (a, e, i, o, u)
# 3. does not contain two consecutive consonants


def calc( l, d ):
    total = 1
    size = len( l )
    idx = 0

    for k, v in d.items(): 
        total *= (size - idx) / v
        idx += 1
    
    return int( total )
    

def Solution( S ):
    if len( S ) == 1:
        return 1

    consonart = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z', 'Y']
    vowels = ['A', 'E', 'I', 'O', 'U']

    SConsonart = [];                    SVowels = []
    consonartSum = 0;                   vowelsSum = 0
    consonartExist = dict();            vowelsExist = dict()

    for c in S:
        if c in consonart:
            SConsonart.append( c )
            if c not in consonartExist:
                consonartExist[c] = 0
        else:
            SVowels.append( c )
            if c not in vowelsExist:
                vowelsExist[c] = 0
    
    LConsonart = len( SConsonart );     LVowels = len( SVowels )

    for c in consonartExist.keys():
        consonartExist[c] = SConsonart.count( c )
    for c in vowelsExist.keys():
        vowelsExist[c] = SVowels.count( c )

    # sort dict
    # lambda dict: {k: v for k, v in sorted(consonartExist.items(), key=lambda item: item[1])}
    consonartSort = {k: v for k, v in sorted(consonartExist.items(), key=lambda item: item[1])}
    vowelsSort = {k: v for k, v in sorted(vowelsExist.items(), key=lambda item: item[1])}

    if LConsonart == LVowels or LConsonart == LVowels + 1:
        total = 1
        # calc consonar
        total *= calc( SConsonart, consonartSort )
        # calc vowels
        total *= calc( SVowels, vowelsSort )

        return total
    else:
        return 0
    

S = "BAR" # 2
print( "2: ", Solution( S ) )
S = "AABB" # 1
print( "1: ", Solution( S ) )
S = "AABCY" # 6
print( "6: ", Solution( S ) )
S = "AAAB" # 0
print( "0: ", Solution( S ) )
S = "AABBY" # 3
print( "3: ", Solution( S ) )
S = "AOBCY" # 12
print( "12: ", Solution( S ) )
# S = "AATTBBEE"
# print( "x: ", Solution( S ) )
S = "BABAC"
print( "3: ", Solution( S ) )
S = "BABACA"
print( "3: ", Solution( S ) )
S = "BABABA"
print( "1: ", Solution( S ) )



