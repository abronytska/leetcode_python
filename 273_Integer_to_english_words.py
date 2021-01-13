def numberToWord(num):
    def under_10(n):
        switcher = {
            0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
        }
        return switcher.get(n)

    def under_20(n):
        switcher = {
            10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
            14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
            17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'
        }
        return switcher.get(n)

    def tens(n):
        switcher = {
            2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
            6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'
        }
        return switcher.get(n)

    def numToChunks(num):
        snum = str(num)
        i = -1
        chunk = list()
        chunks_array = list()

        while abs(i) <= len(snum):
            if i % 3 != 0:
                chunk.append(int(snum[i]))
            elif i % 3 == 0:
                chunk.append(int(snum[i]))
                chunk.reverse()
                chunks_array.append(chunk)
                chunk = []

            i = i - 1
        if chunk:
            chunk.reverse()
            chunks_array.append(chunk)
        chunks_array.reverse()

        return chunks_array

    chunks = numToChunks(num)

    for idx, chunk in enumerate(chunks):
        #--len = 3--
        if len(chunk) == 3:
            if chunk[0] == 0:
                chunk[0] = ''
            else:
                chunk[0] = under_10(chunk[0]) + ' Hundred'
            if chunk[1] == 0:
                chunk[1] = ''
                if chunk[2] == 0:
                    chunk[2] = ''
                else:
                    chunk[2] = under_10(chunk[2])
            elif chunk[1] == 1:
                chunk[1] = under_20(chunk[1] * 10 + chunk[2])
                chunk[2] = ''
            elif chunk[1] >= 1:
                chunk[1] = tens(chunk[1])
                if chunk[2] == 0:
                    chunk[2] = ''
                else:
                    chunk[2] = under_10(chunk[2])
        #--len = 2--
        elif len(chunk) == 2:
            if chunk[0] == 1:
                chunk[0] = under_20(chunk[0] * 10 + chunk[1])
                chunk[1] = ''
            elif chunk[0] > 1:
                chunk[0] = tens(chunk[0])
                if chunk[1] == 0:
                    chunk[1] = ''
                else:
                    chunk[1] = under_10(chunk[1])
        #--len = 1--
        elif len(chunk) == 1:
            chunk[0] = under_10(chunk[0])

    res_chunks = list()
    for chunk in chunks:
        res_chunk = ' '.join(chunk).replace('  ', ' ').strip()
        res_chunks.append(res_chunk)

    if len(res_chunks) >= 4:
        res_chunks.insert(-3, 'Billion')
    if len(res_chunks) >= 3 and res_chunks[-3] != '':
        res_chunks.insert(-2, 'Million')
    if len(res_chunks) >= 2 and res_chunks[-2] != '':
        res_chunks.insert(-1, 'Thousand')

    return ' '.join(res_chunks).strip().replace('  ', ' ').replace('  ', ' ')



print('1.234.513.891')
print(numberToWord(1234513891))
print(1234567891)
print(numberToWord(1234567891))
print(123)
print(numberToWord(123))
print(12345)
print(numberToWord(12345))
print(1234567)
print(numberToWord(1234567))
print(0)
print(numberToWord(0))
print(3)
print(numberToWord(3))
print(100)
print(numberToWord(100))
print(20)
print(numberToWord(20))
print(1000)
print(numberToWord(1000))
print(1000000)
print(numberToWord(1000000))
print(1000000000)
print(numberToWord(1000000000))