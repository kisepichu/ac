# coding: utf-8

def clear(args, config):
    with open(config['source_path'], mode='r') as f:
        source = f.readlines()
    with open(config['source_path'], mode='w') as f:
        sta = ['root']
        for line in source:
            if line.startswith('#pragma endregion'):
                sta.pop()
            if 'solve' not in sta and 'main' not in sta:
                f.write(line)
            if line.startswith('#pragma region'):
                s = line.split()
                sta.append(s[2])
                if s[2] == 'solve':
                    f.write('\nint solve(){\n\t\n\treturn 0;\n}\n\n')
                if s[2] == 'main':
                    f.write('\nint main(){\n\tsolve();\n}\n\n')
    return
