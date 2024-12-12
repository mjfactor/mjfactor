with open('readme.md', 'r') as file:
    content = file.read()


content = content.replace('Dynamic Programming', '###REPLACE###').replace('Docker', 'Dynamic Programming').replace('###REPLACE###', 'Docker')


with open('readme.md', 'w') as file:
    file.write(content)
