
def read_file(filename):
	lines = []
	with open(filename, "r", encoding="utf-8-sig") as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):#轉換
	new = []#創造一個新清單
	person = None# 預設變數為無(None)
	for line in lines:
		if line == "Allen":
			person = "Allen"#將右邊變數取名
			continue
		elif line == "Tom":
			person = "Tom"
			continue
		if person:
			new.append(person + ": " + line)
	return new

def write_file(filename, lines):
	with open(filename, "w") as f:
		for line in lines:
			f.write(line + "\n")

def main():
	lines = read_file("input.txt")
	lines = convert(lines)
	write_file("output.txt", lines)
main()