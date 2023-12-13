def Frequency_analytic(s):
	cl = {}
	for c in s:
		if c in cl:
			cl[c] += 1
		else:
			cl[c] = 1
	cl = sorted(cl.items())
	cl = dict(cl)
	for key, value in cl.items():
		print(key, value)
		
if __name__=="__main__":
	msg = input("input your message: ")
	Frequency_analytic(msg)
