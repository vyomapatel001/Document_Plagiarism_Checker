import difflib

def highlight_differences(text1, text2):
    d = difflib.Differ()
    diff = list(d.compare(text1.split(), text2.split()))
    highlighted = []

    for word in diff:
        if word.startswith('- '):
            highlighted.append(f'<span style="background-color:#CAB6D4">{word[2:]}</span>')  # purple
        elif word.startswith('+ '):
            highlighted.append(f'<span style="background-color:#B7E4C7">{word[2:]}</span>')  #
        elif word.startswith('? '):
            highlighted.append(f'<span style="background-color:#FDE68A">{word[2:]}</span>')  # yellow
        else:
            highlighted.append(word[2:])
    return ' '.join(highlighted)


# Load your .txt files
with open("doc1.txt", "r", encoding="utf-8") as f1:
    text1 = f1.read()

with open("doc2.txt", "r", encoding="utf-8") as f2:
    text2 = f2.read()

diff_output = highlight_differences(text1, text2)
print(diff_output)

# Save the output to a new file
with open("diff_output.txt", "w", encoding="utf-8") as f_out:
    f_out.write(diff_output)