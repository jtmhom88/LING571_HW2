import collections,nltk

 

def build(CNF):
	G = collections.defaultdict(list)
	for left, right in CNF:
		G[right].append(left)
	return G

 

def cky(G, W):

	T = [[[] for j in range(len(W)+1)] for i in range(len(W))]
	for j in range(1, len(W)+1):
		T[j-1][j] += G.get(W[j-1], [])
		print "[%d,%d]: %r" % (j-1, j, G.get(W[j-1]))
		for i in range(j-2, -1, -1):
			for k in range(i+1, j):
				for x in T[i][k]:
					for y in T[k][j]:
						T[i][j] += G.get((x,y), [])
						print "[%d,%d]: %r (%s [%d,%d] and %s [%d,%d])" % (i,j,G.get((x,y)),x,i,k,y,k,j)
	print "FINAL T[0][%d]=%r" % (len(W),T[0][len(W)])
	return T

 

if __name__ == '__main__':


	CNF = (
   ('S',('NP','VP')),
   ('S',('NP','NP')),
   ('VP',('VBP','PP')),
   ('VP',('VBZ','NP')),
   ('VP',('VBZ','ADJP')),
   ('VP',('VBZ','VP')),
   ('VP',('VB','NP')),
   ('VP',('VBN','PP')),
   ('VP',('VBP','ADJP')),
   ('VP',('VBP','S')),
   ('VP',('VBD','SBAR')),
   ('VP',('VBG','NP')),
   ('VP',('MD','VP')),
   ('VP',('VB','NP')),
   ('VP',('VBD','NP')),
   ('VP',('TO','VP')),
   ('SBAR',('IN','S')),
   ('NP',('NP','NP')),
   ('NP',('NP','PP')),
   ('NP',('NP','NP')),
   ('NP',('Adj','NP')),
   ('NP',('NP','PP')),
   ('NP',('ADJP','NP')),
   ('NP',('NP','ADJP')),
   ('Quant',('Card','NP')),
   ('NP',('Quant','NP')),
   ('NP',('Det','NP')),
   ('NP',('PossNP','NP')),
   ('NP',('QP','NP')),
   ('PP',('Prep','NP')),
   ('ADJP',('Adj','PP')),
   ('ADJP',('Adv','Adj')),
   ('ADJP',('Adj','PP')),
   ('ADJP',('Adj','S')),
   ('S',('X1','VP')),
   ('X1',('NP','ADVP')),
   ('S',('X2','PUNC')),
   ('X2',('NP','VP')),
   ('FRAG',('X3','PUNC')),
   ('X3',('Adv','NP')),
   ('VP',('X4','PP')),
   ('X4',('VBN','PRT')),
   ('VP',('X5','ADVP')),
   ('X5',('VBZ','VBG')),
   ('NP',('X6','VP')),
   ('X6',('NP','PP')),
   ('NP',('X7','NP')),
   ('X7',('NP','Conj')),
   ('QP',('X8','Det')),
   ('X8',('JJR','IN')),
   ('S',('X9','PUNC')),
   ('X9',('X10','S')),
   ('X10',('S','Conj')),
   ('S',('X11','PUNC')),
   ('X11',('X12','VP')),
   ('X12',('PP','NP')),
   ('SQ',('X13','PUNC')),
   ('X13',('X14','VP')),
   ('X14',('VBP','NP')),
   ('SQ',('X15','PUNC')),
   ('X15',('X16','ADJP')),
   ('X16',('VBZ','NP')),
   ('Det','The'),
   ('Det','the'),
   ('Det','a'),
   ('Det','an'),
   ('Det','An'),
   ('Det','A'),
   ('Det','that'),
   ('Det','Some'),
   ('Det','Few'),
   ('NP','work'),
   ('NP','motor'),
   ('NP','system'),
   ('NP','movement'),
   ('NP','male'),
   ('NP','adult'),
   ('NP','%'),
   ('NP','muscle'),
   ('NP','female'),
   ('NP','action'),
   ('NP','origin'),
   ('NP','insertion'),
   ('NP','pain'),
   ('NP','risk'),
   ('NP','researcher'),
   ('NP','Work'),
   ('NP','growth'),
   ('NP','response'),
   ('NP','face'),
   ('NP','side'),
   ('NP','arthritis'),
   ('NP','DNA'),
   ('NP','heredity'),
   ('NP','abdomen'),
   ('NP','appendicitis'),
   ('NP','week'),
   ('NP','one'),
   ('NP','discovery'),
   ('NP','mystery'),
   ('NP','milestone'),
   ('NP','research'),
   ('NP','disease'),
   ('NP','locations'),
   ('NP','movements'),
   ('NP','muscles'),
   ('NP','people'),
   ('NP','Muscles'),
   ('NP','Scientists'),
   ('NP','Dr'),
   ('NP','David'),
   ('NP','Cook'),
   ('VBZ','Is'),
   ('VBZ','is'),
   ('VBZ','controls'),
   ('VBZ','accelerates'),
   ('VB','have'),
   ('VB','be'),
   ('VB','dispute'),
   ('VBP','Do'),
   ('VBP','grow'),
   ('VBP','are'),
   ('VBP','consider'),
   ('VBN','made'),
   ('VBN','determined'),
   ('PRT','up'),
   ('VBD','realized'),
   ('VBD','was'),
   ('VBG','lasting'),
   ('VBG','functioning'),
   ('Adj','physical'),
   ('ADJP','physical'),
   ('Adj','responsible'),
   ('ADJP','responsible'),
   ('Adj','average'),
   ('ADJP','average'),
   ('Adj','skeletal'),
   ('ADJP','skeletal'),
   ('Adj','pyramidal'),
   ('ADJP','pyramidal'),
   ('Adj','voluntary'),
   ('ADJP','voluntary'),
   ('Adj','tired'),
   ('ADJP','tired'),
   ('Adj','Old'),
   ('ADJP','Old'),
   ('Adj','important'),
   ('ADJP','important'),
   ('Adj','much'),
   ('ADJP','much'),
   ('Adj','many'),
   ('ADJP','many'),
   ('Adj','privy'),
   ('ADJP','privy'),
   ('Adj','willing'),
   ('ADJP','willing'),
   ('Adj','scary'),
   ('ADJP','scary'),
   ('Adv','finally'),
   ('ADVP','finally'),
   ('Adv','normally'),
   ('ADVP','normally'),
   ('Adv','Not'),
   ('ADVP','Not'),
   ('Adv','very'),
   ('ADVP','very'),
   ('Prep','for'),
   ('Prep','of'),
   ('Prep','by'),
   ('Prep','at'),
   ('Prep','in'),
   ('Prep','on'),
   ('Prep','to'),
   ('Prep','Before'),
   ('NP','it'),
   ('JJR','more'),
   ('IN','that'),
   ('IN','than'),
   ('MD','could'),
   ('EX','There'),
   ('TO','to'),
   ('Conj','and'),
   ('Card','45'),
   ('Card','35'),
   ('NP','you'),
   ('PossNP','your'),
   ('PUNC','.'),
   ('PUNC','?'),
   ('NP','There'),
	)

	G = build(CNF)

	#T = cky(G, ('take','the','flight','through','Houston'))
	T = cky(G, ('work','accelerates','the','growth','of','muscles','.'))
	#T = cky(G, ('work','accelerates','the','growth','of','muscles'))


	i = 0
	temp = tok = []
        list = [];
        f = open('inputfile.txt','r')
        for line in f:
           temp = line.strip()
           list.append(temp)
    	   tok = nltk.word_tokenize(temp)
	   if i != 99:
               T = cky(G,tok)
	       print "final parse",temp
           i += 1


