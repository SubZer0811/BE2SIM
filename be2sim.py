length = 2
width = 4

def in2post (in_exp):

	post_exp = []
	stack = []

	for i in in_exp:
		
		if(i == '('):
			stack.append('(')
		elif(i == ')'):
			
			if(stack[-1] == '+' or stack[-1] == '!' or stack[-1] == '.'):
				post_exp.append(stack[-1])
				stack.pop()
				stack.pop()
			else:
				stack.pop()
		elif(i == '+' or i == '!' or i == '.'):
			stack.append(i)
		else:
			post_exp.append(i)

	return post_exp

def generate (post_exp):

	stack = []
	network = []
	node_counter = 1
	out_counter = 1

	# type gate source drain length width
	for i in post_exp:

		if(i == '+' or i == '!' or i == '.'):
			if(i == '+'):
				gate1 = ['p', stack[-2], 'vdd', node_counter, length, width]
				gate2 = ['p', stack[-1], node_counter, 'out'+str(out_counter), length, width]
				gate3 = ['n', stack[-2], 'out'+str(out_counter), 'gnd', length, width]
				gate4 = ['n', stack[-1], 'out'+str(out_counter), 'gnd', length, width]
				network.append(gate1); network.append(gate2); network.append(gate3); network.append(gate4)
				
				gate5 = ['p', 'out'+str(out_counter), 'vdd', 'out'+str(out_counter+1), length, width]
				gate6 = ['n', 'out'+str(out_counter), 'out'+str(out_counter+1), 'gnd', length, width]
				network.append(gate5); network.append(gate6)
				
				stack.pop(); stack.pop()
				stack.append('out'+str(out_counter+1))
				
				out_counter += 2
				node_counter += 1

			if(i == '.'):
				gate1 = ['p', stack[-2], 'vdd', 'out'+str(out_counter), length, width]
				gate2 = ['p', stack[-1], 'vdd', 'out'+str(out_counter), length, width]
				gate3 = ['n', stack[-2], 'out'+str(out_counter), node_counter, length, width]
				gate4 = ['n', stack[-1], node_counter, 'gnd', length, width]
				network.append(gate1); network.append(gate2); network.append(gate3); network.append(gate4)
				
				gate5 = ['p', 'out'+str(out_counter), 'vdd', 'out'+str(out_counter+1), length, width]
				gate6 = ['n', 'out'+str(out_counter), 'out'+str(out_counter+1), 'gnd', length, width]
				network.append(gate5); network.append(gate6)
				stack.pop(); stack.pop()
				stack.append('out'+str(out_counter+1))

				out_counter += 2
				node_counter += 1

			if(i == '!'):

				gate = stack[-1]

				gate1 = ['p', gate, 'vdd', 'out'+str(out_counter+1), length, width]
				gate2 = ['n', gate, 'out'+str(out_counter+1), 'gnd', length, width]
				network.append(gate1); network.append(gate2)
				stack.pop()

				stack.append('out'+str(out_counter+1))

				out_counter += 2

		else:
			stack.append(i)

	# out = int(stack[0][3:])

	for i in range(len(network)):
		if(network[i][3] == stack[0]):
			network[i][3] = 'out'
		if(network[i][2] == stack[0]):
			network[i][2] = 'out'

		network[i] = ' '.join([str(n) for n in network[i]]) + '\n'

	return network


if __name__ == "__main__":
	
	print("DISCLAIMER: Make sure to use paranthesis whereever possible. \ne.g. !A.B.C should be writtern as (((!(A)).B).C)")
	print("The input variables can be any alphabet. The final output is 'out'.\n")
	print("The following gates can be used: + (OR), . (AND), ! (NOT)\n")
	exp = input("Enter the boolean expression: ")

	print("\nPostfix Expression: " + str(in2post(exp)))

	n = generate((in2post(exp)))

	f = open("exp.sim", 'w')
	f.writelines(n)
	f.close()

	print("\n[+] Output: exp.sim file created")