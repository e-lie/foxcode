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


    return result_parse_tree

def padding(beat_number, baselist):
    spacedsublist = [[e]+[' ']*(beat_number-1) for e in baselist]
    spacedlinear = [e for sublist in spacedsublist for e in sublist]
    return spacedlinear


# parsed_element = parse_playstring_tree("4[---2[---]--]")
# parsed_element = parse_playstring_tree("--4[---2[-----]---3[-[--]]]---[--]--")
parsed_element = parse_playstring_tree("9[---2[-----]3[-[--]]]")
# parsed_element = parse_playstring_tree("--[---[-----]---[-[--]]]---[--]--")

parsed_element.show(key=lambda k: k.identifier)

def compute_padding_values_in_tree(parse_tree):
    """ Calculate padding to apply to each node in the parse tree"""
    # for each node in the tree ...
    for node in parse_tree.expand_tree(mode=Tree.DEPTH, key=lambda k: k.identifier):
        if parse_tree[node].data: # ... except the root that has no data dict
            # padding is the node rhythmic base (~= new subdivision of rhythmic group) ...
            parse_tree[node].data["padding"] = parse_tree[node].data["base"]
            # ... times the rhythmic subdivision values of each sibling and his children recursively
            for sibling in parse_tree.siblings(node):
                for sibling_child in parse_tree.expand_tree(nid=sibling.identifier, mode=Tree.DEPTH, key=lambda k: k.identifier):
                    parse_tree[node].data["padding"] *= parse_tree[sibling_child].data["subdiv"]

compute_padding_values_in_tree(parsed_element)

for node in parsed_element.expand_tree(mode=Tree.DEPTH, key=lambda k: k.identifier):
    if parsed_element[node].data:
        print("========================")
        print(parsed_element[node].tag)
        print(parsed_element[node].data["padding"])
        

# padded = []

# def recpadding(tree, node):
#     if not node.successors[tree.identifier]:
#         padding
#     sum([recpadding(n) for n in node.successors[tree.identifier]])