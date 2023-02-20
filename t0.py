import proto

def findSub(txt:str, startsub:str, endsub:str) -> list:
    i=0
    blks = []
    while txt[i:].find(startsub) != -1: 
        blks.append(
            [   i+txt[i:].find(startsub),
                i+txt[i:].find(endsub  ) + len(endsub)
            ])
        i=blks[-1][1]
    return blks

def concatBlks(txt:str, blks:list) -> str:
    conc = [ txt[bs, be] for (bs,be) in blks ] 
    return ''.join(conc)

def removeBlks(txt:str, blks:list) -> str:
    es=0
    conc=[]
    for (bs,be) in blks:
        conc.append(txt[es:bs])
        es = be 
    conc.append(txt[be:])
    return ''.join(conc)

def findFunc(txt:str, blkstart:int) -> proto.func:
    f_bound = max(
        [   txt.rfind(delim, max(0, blkstart-proto.ASUMP_FUNC_MAXLENGTH), blkstart)
            for delim in proto.BLK_DELIMS
        ])
        
    if f_bound == -1 and max(0, blkstart-proto.ASUMP_FUNC_MAXLENGTH) != 0:
        raise proto.AbnormalLengthException
    
    #seperate args and tokenise the rest
    f_s = f_bound + 1
    argsblk = findSub(txt[f_s:blkstart], '(', ')' )
    
    argslist = txt[argsblk[0]+1:argsblk[1]-1].split(',')
    while argslist.count(''): argslist.remove('')
    argslist = [ arg.rsplit(maxsplit=1) for arg in argslist ]

    lvallist = txt[f_s:argsblk[0]].split()

    mexlist = txt[argsblk[1]+1:blkstart].split()

    #create the obj
    pfunc = proto.func()
    pfunc.setName(lvallist[-1])
    pfunc.setRet(lvallist[0:-1])
    pfunc.setMEx(mexlist)
    pfunc.setArgs(argslist)

    return pfunc

def findClass(txt:str, )

def __test__():
    raw_text = open("./file0.java", 'r').read()
    pass