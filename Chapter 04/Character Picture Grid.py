#Build with python 2.7.14

grid = [	#XXXXX	 #0   #1   #2	#3   #4	  #5	#YYYYY
			['.', '.', '.', '.', '.', '.'], #0
			['.', 'O', 'O', '.', '.', '.'], #1
			['O', 'O', 'O', 'O', '.', '.'],	#2
			['O', 'O', 'O', 'O', 'O', '.'],	#3
			['.', 'O', 'O', 'O', 'O', 'O'], #4
			['O', 'O', 'O', 'O', 'O', '.'],	#5
			['O', 'O', 'O', 'O', '.', '.'],	#6
			['.', 'O', 'O', '.', '.', '.'],	#7
			['.', '.', '.', '.', '.', '.']	#8
											]


LineNum = len(grid)
RowNum = len(grid[0])
print 'Total line num,'+str(LineNum)+'. Total row num,'+str(RowNum)
print '\n'
for x in range(0,RowNum):
	for i in range(0,LineNum):
	# grid[x]=grid[0],grid[1],grid[2],grid[3],grid[4],grid[5]

		print grid[i][x],'',
	'''	grid[0][0]
		grid[1][0]
		grid[2][0]
		grid[3][0]
		grid[4][0]
		grid[5][0]
		grid[6][0]
		grid[7][0]
		grid[8][0] 
				'''

	print '\n'
