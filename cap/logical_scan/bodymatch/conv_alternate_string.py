sig = '7070bb(aa|bb)7171(cc|dd)7272'

def simple_sig_alt(sig):
    sig = sig.replace(' ','') #Remove spaces
    total_end_sigs = []
    while '(' in sig:
        sig_part_0 = sig[:sig.find('(')]
        sig_part_1 = sig[sig.find('(')+1:]
        sig_part_2 = sig_part_1[sig_part_1.find(')')+1:]
        sig_part_1 = sig_part_1[:sig_part_1.find(')')]
        sig_part_1 = sig_part_1.split('|')
        print('0:', sig_part_0, '1:', sig_part_1, '2:',sig_part_2)

        for value in sig_part_1:
            new_sig = ''
            new_sig += sig_part_0
            new_sig += value
            new_sig += sig_part_2
            total_end_sigs.append(new_sig)
        break
    print(total_end_sigs)
    return total_end_sigs

    print('0:', sig_part_0, '1:', sig_part_1, '2:', sig_part_2)


simple_sig_alt(sig)
