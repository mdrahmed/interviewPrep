'''
Time complexity of this solution is O(n). This will solve a string even if a string has encoded characters in it like ":;"
Solution: Encode a string adding total length and a special character like ":;" at the beginning.
'''
"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    encoded_str = ""
    for i in range(len(strs)):
        encoded_str += str(len(strs[i])) + "#" + strs[i]
    return encoded_str

"""
@param: str: A string
@return: decodes a single string to a list of strings
"""
def decode(str):
    decoded_str = []
    st = 0
    while st < len(str): 
        # 4#next
        length = int(str[st])
        new_str = str[st+2:st+length+2]
        decoded_str.append(new_str)
        st = st + length + 2
    return decoded_str

strr = ["abc", "nex:;t"]
en = encode(strr)
print(en)
print(decode(en))

