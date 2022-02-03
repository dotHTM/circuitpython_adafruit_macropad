# from copy import copy
import re

class Notes():
    semitone = 1.0595
    
    referenceA = 440
    referenceOctave = 4
    ## The scale is defined by A4
    A = referenceA
    As = A * semitone
    B = As * semitone
    ## the octave begins at C, so backsolve, then the rest arise similarly
    C = B * semitone / 2
    Cs = C * semitone
    D = Cs * semitone
    Ds = D * semitone
    E = Ds * semitone
    F = E * semitone
    Fs = F * semitone
    G = Fs * semitone
    Gs = G * semitone

    nameMap = {
        "C": C,
        "C#": Cs,
        "Cb": Cs,
        "D": D,
        "D#": Ds,
        "Db": Ds,
        "E": E,
        "F": F,
        "F#": Fs,
        "Fb": Fs,
        "G": G,
        "G#": Gs,
        "Gb": Gs,
        "A": A,
        "A#": As,
        "Ab": As,
        "B": B,
    #   "C": C,
    }
    
    baseNames = list(nameMap.keys())
    
    for k in baseNames:
        v = nameMap[k]
        for (searchregex, replaceregex) in [(r'(.)#', r'\1s'), (r'(.)b', r'\1f')]:
            if re.search(searchregex, k):
                nk= re.sub(searchregex, replaceregex, k)
                nameMap[nk] = v

    w = 1
    h = w / 2
    q = w / 4
    e = w / 8
    s = w / 16
    
def note( n: str, o:int):
    if n in Notes.nameMap:
        return Notes.nameMap[n] * (2**(Notes.referenceOctave - o))
    return None

def main():
    print ( note("Ds", 4) )
    print ( note("D#", 4) )
    
    print ( note("Df", 4) )
    print ( note("Db", 4) )
    
    

if __name__ == '__main__':
    main()