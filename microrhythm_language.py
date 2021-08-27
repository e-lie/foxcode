from pprint import pprint
from treelib import Node, Tree

Clock.bpm = 120

d1 >> play("oxxx", amp=0.5)
d2 >> play("X X ", amp=3)
d3 >> play(" [  p  ] [ p   ]", amp=1)
d4 >> play("---[- -][ - ]", amp=1)

d3 >> play("---2[---]", amp=2)

tt >> play("1 2 3 4 ")

tt >> play("ffff")

d3 >> play("4[-----]")
d3 >> play("""[-   -][   - ][  -  ][ -   ]""")

d3 >> play("4[---2[---]]")
d3 >> play("[o   o][   o ][[   ][   ][o  ][   ][ o ]][[   ][   ][o  ][   ][   ]]")



def parenthetic_contents(string):
    """Generate parenthesized contents in string as pairs (level, contents)."""
    stack = []
    for i, c in enumerate(string):
        if c == '[':
            stack.append(i)
        elif c == ']' and stack:
            start = stack.pop()
            yield (len(stack), string[start + 1: i])

def parse_rhythmic_square_brackets(string):
    """Parse rhythmic patterns enclosed in numbered square brackets """
    openpar_index_stack = [] # store indexes of parenthesis opening chars
    for i, c in enumerate(string):
        if c == '[':
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
            yield {
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

parsed_element = list(parse_rhythmic_square_brackets("--4[---2[-----]3[-[--]]]---[--]"))

sorted_parsed_elements = sorted(parsed_element, key=lambda k: (k['depth'], 1 / k['openpar_index']), reverse=True)

pprint(sorted_parsed_elements)

# def write_subdiv(beat_number, element_list):
#     new_element_list = []
#     element_list_length = len(element_list)
#     index = 0
#     for i in range(beat_number):
#         sublist = []
#         for j in range(element_list_length):
#             if index % beat_number == 0:
#                 sublist.append(element_list.pop(0))
#             else:
#                 sublist.append(' ')
#             index=index+1
#         new_element_list.append(sublist)
#     return new_element_list
#
# print(write_subdiv(4, ['-','-','-','-','-']))




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
d3 >> play("4[---2[---]]")
d3 >> play("<[o   o][   o ][[   ][   ][o  ][   ][ o ]][[   ][   ][o  ][   ][   ]]><XX><xx>")

result = "".join(
                linearize_as_string(
                    rebase(5,
                        linearize_as_string(
                            rebase(3,
                                padding(4,
                                    padding(3, '---') + padding(2, '---')
                                )
                            )
                        )
                    )
                )
            )
print(result)
aa >> play(result)
ab >> play("offf")
# ===========================================

d3 >> play("---[---]-")

result = "".join(
            linearize_as_string(
                rebase(3,
                    padding(3, 'ooo') + padding(1, 'ooo') + padding(3, 'o')
                )
            )
        )
print(result)

aa >> play(result)

ab >> play("ffff")

# ===========================================

d3 >> play("--3[----]-")

result = "".join(
            linearize_as_string(
                rebase(4,
                    padding(4, 'oo') + padding(3, 'oooo') + padding(4, 'o')
                )
            )
        )
print(result)

aa >> play(result)
ab >> play("ffff")


# ===========================================

d3 >> play("---9[---2[-----]3[--]]")

result = "".join(
            linearize_as_string(
            rebase(8,
            linearize_as_string(
            rebase(5,
                linearize_as_string(
                rebase(2,
                padding(80, 'ooo') +
                padding(9,
                    padding(10, 'ooo') + padding(4, 'ooooo') + padding(15, "oo")
                )
                )
                )
            )
            )
            )
            )
        )
print(result)

aa >> play("<" + result + "><xfffffffffff>")


ab >> play("xfffffff")

# ========================================================

"9[---2[-----]3[-[--]]]"

result = "".join(
                                    linearize_as_string(
                                        rebase(8,
                            linearize_as_string(
                                rebase(5,
                    linearize_as_string(
                        rebase(2,
            linearize_as_string(
                rebase(2,
                                            padding(9,
                                                padding(1*2*5*2, "---")
                                                + padding(2*2*2, "-----")
                                                + padding(3*5,
                                                            padding(1*2, "-")
                                                            + padding(1, "--")
                                                        )
                                                )
                                            )
                                       )
                                   )
                            )
                        )
                    )
                )
            )
        )
print(result)

aa >> play("<" + result + "><xffffffff>")


ab >> play("ffffffff")


print("".join(linearize_as_string(rebase(2,padding(2,"-")+padding(1,"--")))))

# ========================================================================

# -----2[---]
print(
    rebase(3,
        padding(5, 'XXXXX') + padding(2, 'XXX')
    )
)


print(padding(3, 'XXX'))

# "4[---2[-----]3[-[--]]]"

# "-[--]" => X XX
print(padding(1,'X')+padding(1,'XX'))

d3 >> play("3[--[--]-]")
d3 >> play("[o  o][  [o ][ o]][[  ][o ]  ]")

d2 >> play("XXX")
