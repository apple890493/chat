#對話練習-情況三
#字串切割;把字串一部分取出來(清單切割也可以使用在字串上)

lines = []
with open("3.txt", "r", encoding="utf-8-sig") as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(" ")
	time = s[0][:5]#字串也能做切割
	name = s[0][5:]
	print(time, name)