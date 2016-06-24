feature_dir = '../features/'

main_file = file(feature_dir + 'train.csv')
outfile0 = file('financial_only_id.txt', 'w')
outfile1 = file('financial_full_line.csv', 'w')

for line in main_file:
    cg = line[7]
    creative_id = line[6]
    if cg[0] == '6':
        outfile0.write(cg)
        outfile1.write(line)
