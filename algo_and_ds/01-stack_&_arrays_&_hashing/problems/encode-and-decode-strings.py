
"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    # write your code here
    encoded_str = ""
    for i in range(len(strs)):
        if i == len(strs)-1:
            encoded_str += strs[i]
        else:
            encoded_str += strs[i] + ":;"
    return encoded_str

"""
@param: str: A string
@return: decodes a single string to a list of strings
"""
def decode(str):
    # write your code here
    decoded_str = []
    st = 0
    for i in range(len(str)):
        if str[i] == ':' and str[i+1] == ';' or i == len(str)-1:
            if len(str)-1 == i:
                new_str = str[st:i+1]
            else:
                new_str = str[st:i]
            st = i+2
            decoded_str.append(new_str)

    return decoded_str

print(encode(["abc", "next"]))
print(decode("abc:;next"))

