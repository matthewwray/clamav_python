from hex_sig_conv import decodehex

target_types = ["ANY", "PE", "OLE2", "HTML", "MAIL", "GRAPHICS", "ELF", "NORMALIZED ASCII TEXT", "DISASM DATA", "MACHO", "PDF", "FLASH", "JAVA CLASS"]

def decode(ext_sig):
    ext_sig = ext_sig.split(':')

    virname = ext_sig[0]
    target = ext_sig[1]
    offset = ext_sig[2]
    sig = decodehex(ext_sig[3])
    print("VIRUS NAME:", virname)
    print("TARGET TYPE:", target_types[int(target)])
    print("OFFSET:", offset)
    print("DECODED SIGNATURE:\n", sig, sep='')
    