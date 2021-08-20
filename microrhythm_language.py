from pprint import pprint

Clock.bpm = 100

d1 >> play("oxxx", amp=0.5)
d2 >> play("X X ", amp=3)
d3 >> play(" [  p  ] [ p   ]", amp=1)
d4 >> play("---[- -][ - ]", amp=1)

d3 >> play("---2[---]", amp=2)

tt >> play("1 2 3 4 ")

tt >> play("ffff")

d3 >> play("4[-----]")
d3 >> play("[-   -][   - ][  -  ][ -   ]")

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

def parenthetic_contents2(string):
    """Generate parenthesized contents in string as pairs (level, contents)."""
    openpar_index_stack = [] # store indexes of parenthesis opening chars
    for i, c in enumerate(string):
        if c == '[':
            openpar_index_stack.append(i)
        elif c == ']' and openpar_index_stack:
            openpar_index = openpar_index_stack.pop()
            content_start = openpar_index + 1
            content = string[content_start:i]
            if openpar_index > 0 and string[openpar_index-1] in ['1','2','3','4','5','6','7','8','9']:
                openpar_index -= 1 # put the index on the number preceding parenthesis
                beat_number = int(string[openpar_index])
            else:
                beat_number = 1
            content_before, content_after = [], []
            if len(openpar_index_stack) > 0:
                content_before = string[openpar_index_stack[-1]+1:openpar_index]
                # start a new parsing to find the corresponding closing parenthesis
                second_stack = []
                for I, C  in enumerate(string[i+1:]): # go through the following chars to find the next closing parenthesis
                    if C == '[':
                        second_stack.append(I)
                    elif C == ']' and second_stack:
                        second_stack.pop()
                    elif C == ']' and not second_stack:
                        content_after = string[i+1:i+1+I]
            yield {
                    "openpar_index": openpar_index,
                    "closepar_index": i,
                    "content_start": content_start,
                    "depth": len(openpar_index_stack),
                    "content": content,
                    "content_before": content_before,
                    "content_after": content_after,
                    "beat_number": beat_number
                  }

pprint(list(parenthetic_contents2("4[---2[-----]3[-[--]]]")))

def write_subdiv(beat_number, element_list):
    new_element_list = []
    element_list_length = len(element_list)
    index = 0
    for i in range(beat_number):
        sublist = []
        for j in range(element_list_length):
            if index % beat_number == 0:
                sublist.append(element_list.pop(0))
            else:
                sublist.append(' ')
            index=index+1
        new_element_list.append(sublist)
    return new_element_list

print(write_subdiv(4, ['-','-','-','-','-']))




def paddinglinear(beat_number, baselist):
    spacedsublist = [[e]+[' ']*(beat_number-1) for e in baselist]
    spacedlinear = [e for sublist in spacedsublist for e in sublist]
    return spacedlinear

def rebase(base_length, spacedlinear):
    rebased = [ spacedlinear[i:i+base_length] for i in range(0, len(spacedlinear), base_length) ]
    return rebased

def rebase_string(base_length, rebased_list):
    result = []
    for e in rebased_list:
        result += ['['] + e + [']']
    return result

def linearize_string(base_length, rebased_list):
    return [ '[' + "".join(sublist) + ']' for sublist in rebased_list ]



print(
    rebase(5,
        paddinglinear(4, ['-','-','-','-','-']),
    )
)


d3 >> play("4[---2[---]]")
d3 >> play("[o   o][   o ][[   ][   ][o  ][   ][ o ]][[   ][   ][o  ][   ][   ]]")





result = "".join(
            linearize_string(5,
            rebase(5,
            linearize_string(3,
                rebase(3,
                    paddinglinear(4,
                        paddinglinear(3, 'ooo') + paddinglinear(2, 'ooo')
                        # paddinglinear(3, ['X','X','X']) + paddinglinear(2, ['X','X','X'])
                    )
                )
            )
            )
            )
        )

print(result)

aa >> play(result)

aa >> play("[[x   ][o   ]]")

result = "".join(
    rebase_string(3,
        paddinglinear(4,
            paddinglinear(3, 'ooo') + paddinglinear(2, 'ooo')
        )
    )
)

print(result)

aa >> play(result)

# -----2[---]
print(
    rebase(3,
        paddinglinear(5, 'XXXXX') + paddinglinear(2, 'XXX')
    )
)


print(paddinglinear(3, 'XXX'))

# "4[---2[-----]3[-[--]]]"

# "-[--]" => X XX
print(paddinglinear(1,'X')+paddinglinear(1,'XX'))

d3 >> play("3[--[--]-]")
d3 >> play("[o  o][  [o ][ o]][[  ][o ]  ]")

d2 >> play("XXX")
