import shutil

# Створення ZIP-архіву з вмістом директорії 'my_folder'
shutil.make_archive('directories/example', 'zip', root_dir='./directories/archive_dir')
