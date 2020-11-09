# coding: utf-8

def clear(args,config):
	with open(config['source_path'],mode='r') as f:
		source = f.readlines()
	with open(config['source_path'],mode='w') as f:
		sta = ['root']
		for line in source:
			if line.startswith('#pragma endregion'):
				sta.pop()
			if 'solve' not in sta:
				f.write(line);
			if line.startswith('#pragma region'):
				s = line.split()
				sta.append(s[2])
				if s[2] == 'solve':
					f.write('\nint main(){\n\t\n}\n\n')
	return