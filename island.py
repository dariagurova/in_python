jd = []

with open('/Users/42robotics/inter/johndoe', 'r') as fp:
	line = fp.readline()

	i = 1
	while(line):
		jd.append(list(line.strip('\n')))
		line = fp.readline()
		i += 1

def fill(jd,ln,col,f,h,w):
	if (ln >= 0 and col >= 0 and ln < h and col < w):
		if jd[ln][col] == 'X':
			jd[ln][col]=f
			flood(jd,ln,col,f,h,w)
	return

def flood(jd,ln,col,f,h,w):
	fill(jd,ln,col+1,f)
	fill(jd,ln,col-1,f)
	fill(jd,ln+1,col,f)
	fill(jd,ln-1,col,f)

isl_num=0
h=len(jd)
w=len(jd[0])
for j in range(len(jd)):
	for k in range(len(jd[j])):
		c=jd[j][k]
		if (c == 'X'):
			fill(jd,j,k,str(isl_num),h,w)
			isl_num = isl_num+1

for i in jd:
	print "".join(i)