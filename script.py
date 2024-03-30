with open('readme.md', 'r') as file:
    content = file.read()


content = content.replace('Dynamic Programming', 'Docker').replace('Docker', 'Dynamic Programming', 1)

with open('readme.md', 'w') as file:
    file.write(content)
