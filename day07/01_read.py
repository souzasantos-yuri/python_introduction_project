# %%

file_name = "story.txt"

with open(file_name) as open_file:
    content = open_file.read()

print(content)