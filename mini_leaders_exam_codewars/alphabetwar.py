def alphabet_war(fight):
    left_power = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_power = {'m': 4, 'q:': 3, 'd': 2, 'z': 1}
    
    left_score = 0
    right_score = 0
    for character in fight:
        
    if character in left_power:
        left_score += left_power.get(character)
    if character in right_power:
        right_score += right_power.get(character)
return "left side wins!" if left_score > right_score\
else "right side wins!" if right_score > left_score else "let's fight again!"

print(alphabet_war("wpbsmdq"))
print(alphabet_war("mqd"))
print(alphabet)war("pz")