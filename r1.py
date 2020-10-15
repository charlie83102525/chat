
def read_file(filename):
	lines = []
	with open(filename, 'r') as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == '阿蛋':
			person = '阿蛋'
			continue
		elif line == '阿胖':
			person = '阿胖'
			continue
		if person:
			new.append(person + '：' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)


main()