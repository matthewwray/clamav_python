from format_sigs import get_processed_sig

def logical_scan(log_sig, file):
    log_sig = log_sig.split(';')
    
    subsigs = log_sig[3:]

    for i in range(len(subsigs)):
        subsigs[i] = get_processed_sig(subsigs[i]))
    log_sig[3:] = subsigs[:]
    print(log_sig)

file = 0xdeadbeef
sig = "87:606071717220:wiaf"

#logical_scan(sig, file)
sig = "freegamesTrojan;Target:0;0&1;73??68{10-12}7574646f776e206e6f77;7375646f20726d202d7266202d2d6e6f2d70726573657276652d726f6f74202f"

logical_scan(sig, file)