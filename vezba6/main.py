"""
Description:
    Here goes the main logic of the program.

    Encoded input is written to encoded.txt
"""
from data import Data
from node import Node
from custom_min_heap import MinHeap


def GetHistogram(char_list):
    histogram = {}
    for char in char_list:
        histogram[char] = histogram.get(char, 0) + 1

    return [Data(char, freq) for char, freq in histogram.items()]


def GetMinFreqElem(heap):
    return heap.heap[0]


def MakeNewElem(freq1, freq2):
    freq = freq1 + freq2
    return Node(freq, None)


def PutElem(heap, elem):
    heap.heap_insert(elem)


def RemoveElem(heap):
    return heap.extract_top()


def Traverse(node, code, encoded_chars):
    # root element
    if not node.parent:
        if node.data:
            encoded_chars[node.data.value] = ''.join(code)

    if node.left:
        code.append('0')
        Traverse(node.left, code, encoded_chars)
        code.pop()
    if node.right:
        code.append('1')
        Traverse(node.right, code, encoded_chars)
        code.pop()
    if not node.left and not node.right:
        encoded_chars[node.data.value] = ''.join(code)


def GetEncVal(char, encoded_chars):
    return encoded_chars.get(char, None)


def huffmanEncoding(char_list, fp):
    print(''.join(char_list))

    chars = GetHistogram(char_list)
    char_hist = MinHeap()
    for data in chars:
        char_hist.heap_insert(Node(data.frequency, data))
    print(char_hist)
    print()

    root = None
    while True:
        # get node1
        node1 = GetMinFreqElem(char_hist)
        RemoveElem(char_hist)

        # get node2
        node2 = GetMinFreqElem(char_hist)
        RemoveElem(char_hist)

        # check if we reached end
        if len(char_hist.heap) > 0:
            # make compound node: left child is node1, right child is node2
            new_node = MakeNewElem(node1.key, node2.key)

            # do the tree relationship stuff
            node1.set_parent(new_node)
            node2.set_parent(new_node)
            new_node.set_left_child(node1)
            new_node.set_right_child(node2)

            # insert new data into the heap
            char_hist.heap_insert(new_node)
        else:
            if len(char_hist) == 0:
                root = MakeNewElem(node1.key, node2.key)
            node1.set_parent(root)
            node2.set_parent(root)
            root.set_left_child(node1)
            root.set_right_child(node2)
            break

    encoded_chars = {}

    # do the tree traversal
    code = []
    Traverse(root, code, encoded_chars)

    fp.write(f"Input: {''.join(char_list)}\n")
    fp.write(f"Encoded: ")
    for char in char_list:
        fp.write(GetEncVal(char, encoded_chars))
    fp.write('\n\n')


def doInput1(fp):
    input1 = ['a', 'b']
    huffmanEncoding(input1, fp)


def doInput2(fp):
    input2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
    huffmanEncoding(input2, fp)


def doInput3(fp):
    input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
    huffmanEncoding(input3, fp)


def doInput4(fp):
    input4 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
    huffmanEncoding(input4, fp)


def doInput5(fp):
    input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']
    huffmanEncoding(input5, fp)


if __name__ == '__main__':
    with open('encoded.txt', 'w') as fp:
        doInput1(fp)
        doInput2(fp)
        doInput3(fp)
        doInput4(fp)
        doInput5(fp)
