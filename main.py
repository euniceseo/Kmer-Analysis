def kmer_func(string):
    kmer_list = {}

    for i in range (len(string) - 2):
        kmer = string[i: i+3]
        if kmer not in kmer_list:
            kmer_list[kmer] = 0

        kmer_list[kmer] = kmer_list.get(kmer) + 1

    print(kmer_list)

if __name__ == '__main__':
    kmer_func("ACAGCCAGCACGACCCCTCTTTGTCCATCTCCGGAGACTACAACATAACTCTACACCTCCATCCCCACCCAGGCATTACGGGAACTTCTTCTTGCTCTTT")

