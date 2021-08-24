from pprint import pprint
from treelib import Node, Tree
from FoxDot import *


aa = Player()
ab = Player()


def parse_playstring_tree(string):
    """Parse rhythmic patterns enclosed in numbered square brackets """
    openpar_index_stack = [] # store indexes of parenthesis opening chars
    result_parse_tree = Tree(identifier="parse_tree")
    result_parse_tree.create_node(string, "playstring_root")
    current_node = ""
    current_parent_node = "playstring_root"
    for i, c in enumerate(string):
        if c == '[':
            result_parse_tree.create_node(c, 'node' + str(i), parent=current_parent_node)
            current_node = 'node' + str(i)
            current_parent_node = 'node' + str(i)
            openpar_index_stack.append(i)
            # add a branch to the tree here
        elif c == ']' and openpar_index_stack:
            openpar_index = openpar_index_stack.pop()
            content_start = openpar_index + 1
            content = string[content_start:i]
            result_parse_tree[current_parent_node].tag = content
            if openpar_index > 0 and string[openpar_index-1] in ['1','2','3','4','5','6','7','8','9']:
                openpar_index -= 1 # put the index on the number preceding parenthesis
                base = int(string[openpar_index])
            else:
                base = 1
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
        
            current_node = ""
            current_parent_node = result_parse_tree[current_parent_node].predecessor("parse_tree")
        elif not current_node:
            result_parse_tree.create_node(c, "node"+str(i), parent=current_parent_node)
            current_node = "node"+str(i)
            current_parent_node = "node"+str(i)
        else:
            result_parse_tree[current_node].tag += c

    return result_parse_tree


parsed_element = parse_playstring_tree("--4[---2[-----]---3[-[--]]]---[--]--")
parsed_element.show()

# sorted_parsed_elements = sorted(parsed_element, key=lambda k: (k['depth'], 1 / k['openpar_index']), reverse=True)

# pprint(sorted_parsed_elements)


def padding(beat_number, baselist):
    spacedsublist = [[e]+[' ']*(beat_number-1) for e in baselist]
    spacedlinear = [e for sublist in spacedsublist for e in sublist]
    return spacedlinear

def rebase(base_length, spacedlinear):
    rebased = [ spacedlinear[i:i+base_length] for i in range(0, len(spacedlinear), base_length) ]
    return rebased

def linearize_as_string(rebased_list):
    return [ '[' + "".join(sublist) + ']' for sublist in rebased_list ]


# ==========================================
aa >> play("4[---2[---]]")
aa >> play("<[o   o][   o ][[   ][   ][o  ][   ][ o ]][[   ][   ][o  ][   ][   ]]><XX><xx>")

result = "".join(
                linearize_as_string(
                    rebase(5,
                        linearize_as_string(
                            rebase(3,
                                padding(4,
                                    padding(3, 'ooo') + padding(2, 'ooo')
                                )
                            )
                        )
                    )
                )
            )
print(result)
aa >> play(result)
ab >> play("ffff")
# ===========================================
