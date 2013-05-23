
Usage = """RBH BLASTOUTPUT1 BLASTOUTPUT2 RBH-list-outfile """

import sys, re

infl1 = ''
infl2 = ''
outfile = '_tmpout.txt'

#parse first BLAST results
FL1 = ??
D1 = {}
for Line in FL1:
	if ( Line[0] != '#' ):
		Line.strip()
		Elements = re.split('\t', Line)
		queryId = Elements[0]
		subjectId = Elements[1]
			??

if (debug): D1.keys() 

#parse second BLAST results
FL2 = open(infl2, 'r')
D2 = {}
for Line in FL2:
	if ( Line[0] != '#' ):
		Line.strip()
		Elements = re.split('\t', Line)
		queryId = Elements[0]
		subjectId = Elements[1]
			???
			
if (debug): D2.keys() 

#Now, pick the share pairs

SharedPairs={}
for id1 in D1.keys():
	value1 = D1[id1]
	if ( value1 in D2.keys() ):
		????
		SharedPairs[value1] = id1

if (debug): SharedPairs 

#outfl = open("_out.csv", "w")
outfl = open( outfile, 'w')

for k1 in SharedPairs.keys():
	line = k1 + '\t' + SharedPairs[k1] + '\n'
	outfl.write(???)
	
outfl.close()

print("Done. RBH from", sys.argv[1], "and", sys.argv[2], "are in", sys.argv[3])
