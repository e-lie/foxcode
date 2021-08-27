from ast import parse

from pprint import pprint

from treelib import Node, Tree

from FoxDot import *


# aa = Player()
# ab = Player()


def parse_playstring_tree(string):
    """Parse rhythmic patterns enclosed in numbered square brackets """
    openpar_index_stack = [] # store indexes of parenthesis opening chars
    result_parse_tree = Tree(identifier="parse_tree")
    result_parse_tree.create_node(string, "playstring_root")
    current_node = None
    current_parent_node = "playstring_root"
    for i, c in enumerate(string):
        if c == '[':
            result_parse_tree.create_node(c, i, parent=current_parent_node)
            current_node = None
            current_parent_node = i
            openpar_index_stack.append(i)
            # add a branch to the tree here
        elif c == ']' and openpar_index_stack:
            openpar_index = openpar_index_stack.pop()
            content_start = openpar_index + 1
            content = string[content_start:i]
            if openpar_index > 0 and string[openpar_index-1] in ['1','2','3','4','5','6','7','8','9']:
                openpar_index -= 1 # put the index on the number preceding parenthesis
                base = int(string[openpar_index])
            else:
                base = 1
            result_parse_tree[current_parent_node].tag = string[openpar_index:i+1]
            # get content before and after current parenthesis pair (at depth -1)
            content_before, content_after = '', ''
            if openpar_index_stack:
                content_before = string[openpar_index_stack[-1]+1:openpar_index]
                # start a new parsing to find the corresponding closing parenthesis
                second_stack = []
                for I, C  in enumerate(string[i+1:]): # go through the following chars to find the next closing parenthesis
                    if C == '[':
                        second_stack.append(I)
                    elif C == ']' and second_stack:
                        second_stack.pop()
                    elif C == ']' and not second_stack: # if the stack is empty this is the correct closing parenthesis
                        content_after = string[i+1:i+1+I]
                        break
            else:
                content_before = string[0:openpar_index]
                if i+1 < len(string):
                    content_after = string[i+1:]
            # new parsing to count subdivisions for the current content
            third_stack = []
            subdiv_counter = 0
            for I,C in enumerate(content):
                if C == '[':
                    if not third_stack: # only count as subdivisions characters not inside parenthesis (depth 0 => empty stack)
                        if I > 0 and content[I-1] in ['1','2','3','4','5','6','7','8','9']:
                            subdiv_counter += int(content[I-1])
                        else:
                            subdiv_counter += 1
                    third_stack.append(I)
                elif C == ']' and third_stack:
                    third_stack.pop()
                elif not third_stack and C in ['1','2','3','4','5','6','7','8','9']:
                    if I+1 < len(content) and content[I+1] != '[':
                        subdiv_counter += 1
                elif not third_stack and C not in ['(',')','[',']','<','>','{','}',',']:
                    subdiv_counter += 1
            result_parse_tree[current_parent_node].data = {
                    "openpar_index": openpar_index,
                    "closepar_index": i,
                    "content_start": content_start,
                    "depth": len(openpar_index_stack),
                    "content": content,
                    "content_before": content_before,
                    "content_after": content_after,
                    "base": base, # on how many beats to play the patterns
                    "subdiv": subdiv_counter, # how many time subdivisions in the pattern to play
                  }
            current_node = None
            current_parent_node = result_parse_tree[current_parent_node].predecessor("parse_tree")
        elif current_node is None:
            if c in ['1','2','3','4','5','6','7','8','9'] and len(string) > i+1 and string[i+1] == '[':
                continue
            result_parse_tree.create_node(c, i, parent=current_parent_node)
            current_node = i
            result_parse_tree[current_node].data = {
                    "content_start": i,
                    "depth": len(openpar_index_stack),
                    "content": c,
                    "base": 1, # on how many beats to play the patterns
                    "subdiv": 1, # how many time subdivisions in the pattern to play
                  }
            # current_parent_node = "node"+str(i)
        else:
            if c in ['1','2','3','4','5','6','7','8','9'] and len(string) > i+1 and string[i+1] == '[':
                continue
            result_parse_tree[current_node].tag += c
            result_parse_tree[current_node].data["content"] += c
            # result_parse_tree[current_node].data["base"] += 1
            # result_parse_tree[current_node].data["subdiv"] += 1
        result_parse_tree[result_parse_tree.root].data = {
            "content_start": 0,
            "depth": 0,
            "content": string,
            "base": 1, # on how many beats to play the patterns
        }
    return result_parse_tree

def padding(beat_number, baselist):
    spacedsublist = [[e]+[' ']*(beat_number-1) for e in baselist]
    spacedlinear = [e for sublist in spacedsublist for e in sublist]
    return spacedlinear

def rebase(base_length, spacedlinear):
    rebased = [ spacedlinear[i:i+base_length] for i in range(0, len(spacedlinear), base_length) ]
    return rebased

def linearize_as_string(rebased_list):
    return [ '[' + "".join(sublist) + ']' for sublist in rebased_list ]

def rebase_and_linearize(base_length, padded_playstring_list):
    return linearize_as_string(rebase(base_length, padded_playstring_list))


# parsed_element = parse_playstring_tree("4[---2[---]--]")
# parsed_element = parse_playstring_tree("--4[---2[-----]---3[-[--]]]---[--]--")

parsed_element = parse_playstring_tree("9[---2[-----]3[-[--]]]")

print(parsed_element)

# parsed_element = parse_playstring_tree("--[---[-----]---[-[--]]]---[--]--")

parsed_element.show(key=lambda k: k.identifier)

def compute_padding_values_in_tree(parse_tree):
    """ Calculate padding to apply to each node in the parse tree"""
    # for each node in the tree ...
    for node in parse_tree.expand_tree(mode=Tree.DEPTH, key=lambda k: k.identifier):
        # ... padding is the node rhythmic "base" (~= new subdivision of rhythmic group denoted by the number before square bracket) ...
        parse_tree[node].data["padding"] = parse_tree[node].data["base"]
        # ... times the rhythmic subdivision values (how many subdivision the rhythmic pattern has) of each sibling and his children recursively
        for sibling in parse_tree.siblings(node):
            for sibling_child in parse_tree.expand_tree(nid=sibling.identifier, mode=Tree.DEPTH, key=lambda k: k.identifier):
                parse_tree[node].data["padding"] *= parse_tree[sibling_child].data["subdiv"]

def build_padded_playstring_in_tree(parse_tree):
    """ build padded result for each node beginning from the deepest leaf to the root """
    for level in range(parse_tree.depth()+1):
        for node in parse_tree.expand_tree(mode=Tree.WIDTH, key=lambda k: k.identifier):
            # pprint(parse_tree[node])
            # print("node: ", node, parse_tree[node].tag)
            if parse_tree.depth() + 1 - level == parse_tree.depth(node) + 1:
                # print("node: ", node, parse_tree[node].tag)
                if not parse_tree.children(node):
                    to_padd = parse_tree[node].tag
                    # print('tadaa')
                else:
                    to_padd = []
                    for child in parse_tree.children(node):
                        to_padd.extend(child.data["padded_result"])
                    # print("to_padd_list:", to_padd)
                    # to_padd = sum(to_padd)
                parse_tree[node].data["padded_result"] = padding(parse_tree[node].data["padding"], to_padd)

compute_padding_values_in_tree(parsed_element)
build_padded_playstring_in_tree(parsed_element)

# for node in parsed_element.expand_tree(mode=Tree.DEPTH, key=lambda k: k.identifier):
#     if parsed_element[node].data:
#         print("========================")
#         print(parsed_element[node].tag)
#         print(parsed_element[node].data["padding"])
#         if "padded_result" in parsed_element[node].data.keys():
#             print(parsed_element[node].data["padded_result"])

print(parsed_element["playstring_root"].data["padded_result"])

result = "".join(
            rebase_and_linearize(8,
                rebase_and_linearize(5,
                    rebase_and_linearize(2,
                        rebase_and_linearize(2,
                            parsed_element["playstring_root"].data["padded_result"]
                        )
                    )
                )
            )
        )

print(result)

# aa >> play("<" + result + "><xffffffff>")


# padded = []

# def recpadding(tree, node):
#     if not node.successors[tree.identifier]:
#         padding
#     sum([recpadding(n) for n in node.successors[tree.identifier]])
