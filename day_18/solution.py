def parse_char(text, char):
    if text[0] == char:
        return text[1:]

def parse_element(text):
    if text[0] == '[':
        return parse_pair(text)
    else:
        return int(text[0]), text[1:]

# def find_nested_pair(e):
#     num_open = 0
#     num_closed = 0
#     for i in range(len(e)):
#         if e[i] == "]":
#             break
#         elif e[i] == "[":
#             num_open += 1
#         if num_open == 5:
#             return i
#     for j in range(len(e)-1, 0, -1):
#         if e[i] == "[" and num_closed == 5:
#             return j
#         if e[i] == "[" and num_closed < 5:
#             break
#         elif e[i] == "]":
#             num_closed += 1
#     return -1

#def explode_pair(outeer)
def find_nested_pair(e, num=0):
    if type(e) == list:
        if num == 4:
            return e
        num += 1
        res = find_nested_pair(e[0], num)
        if res == None:
            res = find_nested_pair(e[1], num)
        #explode_pair(e, res)
        return res
    else:
        return None
    


def reduce_element(e):
    exp_pair = find_nested_pair(e)
    if i > -1:
        e_ind = e.find("]", i)
        exploding_pair = e[i:e_ind+1]
        pair,_ = parse_pair(exploding_pair)
        if e[i-2].isnumeric():
            sum = int(e[i-2]) + pair[0]
            e = e[:i-2] + str(sum) + ",0" + e[e_ind + 1 :]
            print(e)
    return e
    
    
def sum_list(lst):
    pair = lst[0]
    for i in range(1, len(lst)):
        pair = reduce_element(f"[{pair},{lst[i]}]")
    return pair


def parse_pair(text):
    pair = [0,0]
    text = parse_char(text, '[')
    pair[0], text = parse_element(text)
    text = parse_char(text, ',')
    pair[1], text = parse_element(text)
    text = parse_char(text, ']')
    return pair, text


# def parse_text():
#     with open("example.txt") as f:
#         sum = create_pairs(f.read().split('\n'))

def explode_pair(lst, pair):
    left, right = pair[0], pair[1]


def main():
    # pair, _ = parse_pair("[[[[1,1],[2,2]],[3,3]],[4,4]]")
    # print(pair)
    #print(sum_list(["[1,1]", "[2,2]", "[3,3]", "[4,4]"]))
    #reduce_element([[[[[9,8],1],2],3],4])
    lst = [[[[[9,8],1],2],3],4]
    exp_pair = find_nested_pair(lst)
    print(lst)
    print(exp_pair)
    #explode_pair(lst, exp_pair)
    #print(str(element))
    

if __name__ == "__main__":
    main()