#對話練習-情況二
#簡易統計對話紀錄

def read_file(filename):
	lines = []
	with open(filename, "r", encoding="utf-8-sig") as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):#轉換
	person = None# 預設變數為無(None)
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(" ")#split切割(" ")遇到內容就切割
		time = s[0]
		name = s[1]
		if name == "Allen":
			if s[2] == "貼圖":
				allen_sticker_count += 1 #累加1上去
			elif s[2] == "圖片":
				allen_image_count += 1
			else:
				for msg in s[2:]:
					allen_word_count += len(msg)#統計長度 +=快寫法把右邊加進左邊
		elif name == "Viki":
			if s[2] == "貼圖":
				viki_sticker_count += 1
			elif s[2] == "圖片":
				viki_image_count += 1
			else:
				for msg in s[2:]:
					viki_word_count += len(msg)
	print("Allen said", allen_word_count, "words.")
	print("Allen sent", allen_sticker_count, "stickers.")
	print("Allen sent", allen_image_count, "images.")

	print("Viki said", viki_word_count, "words.")
	print("Viki sent", viki_sticker_count, "stickers.")
	print("Viki sent", viki_image_count, "images.")

def write_file(filename, lines):
	with open(filename, "w") as f:
		for line in lines:
			f.write(line + "\n")

def main():
	lines = read_file("[LINE]Viki.txt")
	lines = convert(lines)
	#write_file("output.txt", lines)

main()

#1. 寫良好的程式碼架構
#2. 轉換的function中,使用了continue來跳到下一行
#3. None適合用來當預設值