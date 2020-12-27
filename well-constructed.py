# well-structured
# 1. start with consonant
# The 21 consonant letters in the English alphabet are B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z, and usually Y.
# 2. does not contain two consecutive vowels (a, e, i, o, u)
# 3. does not contain two consecutive consonants


def calc( l, d ):
    total = 1
    size = len( l )
    idx = 0
    count = [];                 countExit = []

    for k, v in d.items(): 
        total *= (size - idx) / v
        idx += 1
        count.append( v )
        if v not in countExit:
            countExit.append( v )

    for c in countExit:
        if c > 1: total *= count.count( c )
    
    return int( total )
    

def Solution( S ):
    if len( S ) == 1:
        return 1

    consonart = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z', 'Y']
    vowels = ['A', 'E', 'I', 'O', 'U']

    SConsonart = [];                    SVowels = []
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


def test( d ):
    size = len( d )
    correct = 0

    for k, v in d.items():
        res = Solution( k )
        if v == res:
            correct += 1
        else:
            print( "String: {0}, Should be: {1}, but {2}".format( k, v, res) )

    print( "total: {0}, correct: {1}, ratio: {2}".format( size, correct, correct/size ))



d = {"TTBBAAAA": 6, "TTTBAAAA": 4, "BAR": 2, "AABB": 1, "AABCY": 6, 
     "BABAC": 3, "BABACA": 3, "BABABA": 1, 
    }

test( d )

