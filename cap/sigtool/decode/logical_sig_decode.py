#SignatureName;TargetDescriptionBlock;LogicalExpression;Subsig0;Subsig1;Subsig2;...
sig = "freegamesTrojan;Target:0;0&1;EP+127:73687574646f776e206e6f77::awif;7375646f20726d202d7266202d2d6e6f2d70726573657276652d726f6f74202f"
sig = "Sig4;Engine:51-255,Target:1;((0|1)&(2|3))&4;EP+123:33c06834f04100f2aef7d14951684cf04100e8110a00;S2+78:22??232c2d252229{15}6e657361706528;S3+50:68efa311c3b9963cb1ee8e586d32aeb9043e;f9c58dcf43987e4f519d629b103375;SL+550:6300680065005c0046006900"

from hex_sig_conv import decodehex
from sig_preprocessing import preprocess

def decode(log_sig):
    log_sig = log_sig.split(';')
    
    signame = log_sig[0]
    tdb = log_sig[1]
    logexp = log_sig[2]
    subsigs = log_sig[3:]

    print("VIRUS NAME:", signame)
    print("TDB:", tdb)
    print("LOGICAL EXPRESSION:", logexp)


    for i in range(len(subsigs)):
        subsig = subsigs[i]
        if '::' in subsig:
            sigmod = subsig.split('::')[1]
            subsig = subsig.split('::')[0]

            sigmod = sigmod.replace('a', 'ASCII ')
            sigmod = sigmod.replace('w', 'WIDE ')
            sigmod = sigmod.replace('i', 'NOCASE ')
            sigmod = sigmod.replace('f', 'FULLWORD ')

        else:
            sigmod = "NONE"

        if ':' in subsig:
            offset = subsig.split(':')[0]
            subsig = subsig.split(':')[1]
        else:
            offset = 'ANY'

        subsig = preprocess(subsig)

        print(" SUBSIG ID", i)
        print(" +-> OFFSET:", offset)
        print(" +-> SIGMOD:", sigmod) #TODO: wtf is sigmod
        print(" +-> DECODED SIGNATURE:\n", decodehex(subsig), sep='')

decode(sig)