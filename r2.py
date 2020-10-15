
def read_file(filename):
	lines = []
	with open(filename, 'r') as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert(lines):
	charlie_word_count = 0
	jane_word_count = 0
	charlie_sticker_count = 0
	jane_sticker_count = 0
	charlie_image_count = 0
	jane_image_count = 0
	person = None
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == '蔡慶良':
			if s[2] == '貼圖':
				charlie_sticker_count += 1
			elif s[2] == '圖片':
				charlie_image_count += 1
			else:
				for m in s[2:]:
					charlie_word_count += len(m)
		elif name == '榛':
			if s[2] == '貼圖':
				jane_sticker_count += 1
			elif s[2] == '圖片':
				jane_image_count += 1
			else:
				for m in s[2:]:
					jane_word_count += len(m)
	print('charlie說了', charlie_word_count)
	print('charlie傳了',charlie_sticker_count, '個貼圖')
	print('charlie傳了',charlie_image_count, '張照片')
	print('jane說了', jane_word_count)
	print('jane傳了',jane_sticker_count, '個貼圖')
	print('jane傳了',jane_image_count, '張照片')

		#print(s)


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('[LINE]Jane.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)


main()