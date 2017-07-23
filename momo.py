import math

# indonesian lang.
# untuk mencari kata dalam puzzel (puzzle word search)
# eksekusi file memang lama tergantung pada panjang inputan
# jika file input pendek, tidak akan berlangsung lama
# algoritma minim wkwk tapi mudah di tracing
# i am so sorry for all the mistake in this file
# hope can help someone
# xannisa - bandung


f = open('word.txt', 'r')
t = f.readline()
T = int(t)
t = 0
hasil = [0 for i in range(T)]
while (t<T):
	puzzle = []
	n = f.readline()
	m = f.readline()
	N = int(n)
	M = int(m)
	n = 0
	caribaru = ''
	while (n<N):
		caribaru = ''
		kata = f.readline()
		for i in range (len(kata)-1):
			caribaru = caribaru + kata[i]
		puzzle.append(caribaru)
		n = n+1
	
	c = f.readline()
	caribaru = ''
	for i in range (len(c)-1):
		caribaru = caribaru + c[i]
	
	puzzleleft = []
	for i in range(N):
		st = ''
		for j in range(M):
			st = st + puzzle[i][M-j-1]
			#print i,j,
		#print
		puzzleleft.append(st) 
	
	puzzledown = []
	for i in range(M):
		st = ''
		for j in range(N):
			st = st + puzzle[j][i]
			#print i,j,
		#print
		puzzledown.append(st)
	
	puzzleup = []
	for i in range(M):
		st = ''
		for j in range(N):
			st = st + puzzle[N-j-1][i]
			#print i,j,
		#print
		puzzleup.append(st)
		
	puzzledownright = []
	for i in range(N):
		for j in range(M):
			l = i
			k = j
			st = ''
			while((k<M) & (l<N)):
				st = st + puzzle[l][k]
				l = l + 1
				k = k+1
			#print i,j,
		#print
			puzzledownright.append(st) 
	
	puzzledownleft = []
	for i in range(N):
		for j in range(M):
			l = i
			k = j
			st = ''
			while((k<M) & (l<N)):
				st = st + puzzleleft[l][k]
				l = l + 1
				k = k+1
			#print i,j,
		#print
			puzzledownleft.append(st) 
	
	puzzleupleft = []
	for i in range(N):
		for j in range(M):
			l = i
			k = j
			st = ''
			while((k<M) & (l<N)):
				st = st + puzzle[N-l-1][M-k-1]
				l = l + 1
				k = k+1
			#print i,j,
		#print
			puzzleupleft.append(st) 
	
	puzzleupright = []
	for i in range(N):
		for j in range(M):
			l = i
			k = j
			st = ''
			while((k<M) & (l<N)):
				st = st + puzzleleft[N-l-1][M-k-1]
				l = l + 1
				k = k+1
			#print i,j,
		#print
			puzzleupright.append(st)
				
	#print puzzle
	#print puzzle[1]
	#print puzzle[1][1]
	
	#print puzzleupright
	#print puzzledown[0][0]
	#print puzzle[1][1]
	
	dapatright = 0
	indexin = 0
	index = 0
	#going right
	for inpuz in range(len(puzzle)):
		for i in range(M):
			j = 0
			k = i
			dapat = ''
			st = puzzle[inpuz]
			#print st,type(st)
			while((j<len(caribaru)) & (k<M)):
				if (st[k] == caribaru[j])& (indexin == 0) & (index ==0 ):
					dapat = dapat + puzzle[inpuz][k]
					k = k+1
				if dapat == caribaru :
					indexin = inpuz
					index = k - len(dapat)
					dapatright = dapatright + 1
					#print dapat
				j = j + 1
	
	dapatleft = 0
	indexin = 0
	index = 0
	#going left
	for inpuz in range(len(puzzleleft)):
		for i in range(M):
			j = 0
			k = i
			dapat = ''
			st = puzzleleft[inpuz]
			#print st,type(st)
			while((j<len(caribaru)) & (k<M)):
				if (st[k] == caribaru[j])& (indexin == 0) & (index ==0 ):
					dapat = dapat + puzzleleft[inpuz][k]
					k = k+1
				if dapat == caribaru :
					indexin = inpuz
					index = k - len(dapat)
					dapatleft = dapatleft + 1
					#print dapat
				j = j + 1
	
	dapatdown = 0
	indexin = 0
	index = 0
	#going down
	for inpuz in range(len(puzzledown)):
		for i in range(N):
			j = 0
			k = i
			dapat = ''
			st = puzzledown[inpuz]
			#print st,type(st)
			while((j<len(caribaru)) & (k<N)):
				if (st[k] == caribaru[j]) & (indexin == 0) & (index ==0 ):
					dapat = dapat + puzzledown[inpuz][k]
					k = k+1
				if dapat == caribaru :
					indexin = inpuz
					index = k - len(dapat)
					dapatdown = dapatdown+ 1
					#print dapat
				j = j + 1
				
	#print dapatdown
	
	dapatup = 0
	indexin = 0
	index = 0
	#going up
	for inpuz in range(len(puzzleup)):
		for i in range(N):
			j = 0
			k = i
			dapat = ''
			st = puzzleup[inpuz]
			#print st,type(st)
			while((j<len(caribaru)) & (k<N)):
				if (st[k] == caribaru[j]) & (indexin == 0) & (index ==0 ):
					dapat = dapat + puzzleup[inpuz][k]
					k = k+1
				if dapat == caribaru :
					indexin = inpuz
					index = k - len(dapat)
					dapatup = dapatup+ 1
					#print dapat
				j = j + 1
				
	#print dapatup
	
	dapatdownright = 0
	indexin = 0
	index = 0
	#going up
	for inpuz in range(len(puzzledownright)):
		for i in range(len(puzzledownright[inpuz])):
			j = 0
			k = i
			dapat = ''
			st = puzzledownright[inpuz]
			#print st,type(st)
			while((j<len(caribaru)) & (k<len(puzzledownright[inpuz]))):
				if (st[k] == caribaru[j])& (indexin == 0) & (index ==0 ):
					dapat = dapat + puzzledownright[inpuz][k]
					k = k+1
				if dapat == caribaru :
					indexin = inpuz
					index = k - len(dapat)
					dapatdownright = dapatdownright+ 1
					#print dapat
				j = j + 1
				
	#print dapatdownright
	
	dapatdownleft = 0
	indexin = 0
	index = 0
	#going up
	for inpuz in range(len(puzzledownleft)):
		for i in range(len(puzzledownleft[inpuz])):
			j = 0
			k = i
			dapat = ''
			st = puzzledownleft[inpuz]
			#print st,type(st)
			while((j<len(caribaru)) & (k<len(puzzledownleft[inpuz]))):
				if (st[k] == caribaru[j])& (indexin == 0) & (index ==0 ):
					dapat = dapat + puzzledownleft[inpuz][k]
					k = k+1
				if dapat == caribaru :
					indexin = inpuz
					index = k - len(dapat)
					dapatdownleft = dapatdownleft+ 1
					#print dapat
				j = j + 1
				
	#print dapatdownleft
	
	dapatupright = 0
	indexin = 0
	index = 0
	#going up
	for inpuz in range(len(puzzleupright)):
		for i in range(len(puzzleupright[inpuz])):
			j = 0
			k = i
			dapat = ''
			st = puzzleupright[inpuz]
			#print st,type(st)
			while((j<len(caribaru)) & (k<len(puzzleupright[inpuz]))):
				if (st[k] == caribaru[j])& (indexin == 0) & (index ==0 ):
					dapat = dapat + puzzleupright[inpuz][k]
					k = k+1
				if dapat == caribaru :
					indexin = inpuz
					index = k - len(dapat)
					dapatupright = dapatupright+ 1
					#print dapat
				j = j + 1
				
	#print dapatupright
	
	dapatupleft = 0
	indexin = 0
	index = 0
	#going up
	for inpuz in range(len(puzzleupleft)):
		for i in range(len(puzzleupleft[inpuz])):
			j = 0
			k = i
			dapat = ''
			st = puzzleupleft[inpuz]
			#print st,type(st)
			while((j<len(caribaru)) & (k<len(puzzleupleft[inpuz]))):
				if (st[k] == caribaru[j]) & (indexin == 0) & (index ==0 ):
					dapat = dapat + puzzleupleft[inpuz][k]
					k = k+1
				if (dapat == caribaru) :
					indexin = inpuz
					index = k - len(dapat)
					dapatupleft = dapatupleft+ 1
					#print dapat
				j = j + 1
				
	#print puzzleupleft
	
	hasil[t] = dapatright + dapatleft + dapatdown + dapatup + dapatupright + dapatupleft + dapatdownleft + dapatdownright
	t = t + 1

t = 0
while(t<T):
	print "Case",
	print t+1,":",
	print hasil[t]
	t = t + 1
