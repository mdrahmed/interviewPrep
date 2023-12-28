def designerPdfViewer(h, word):
    # Write your code here
    maxx = 0
    for w in word:
        ind = ord(w) - ord('a')
        if maxx < h[ind]:
            maxx = h[ind]
    return maxx * len(word)
