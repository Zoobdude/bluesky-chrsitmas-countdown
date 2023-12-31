#check the size of the files and compress them if they are too big

import os

#max bluesky API file size in KB
MAX_FILESIZE = 976.56


list_of_images = os.listdir('images')
list_of_optimized_images = []

for file in list_of_images:
    while os.path.getsize(f'images/{file}')*0.001 > MAX_FILESIZE:
        print(f'File {file} is too big at {os.path.getsize(f"images/{file}")/1024} KB')
        print(f'Optimizing {file}...')
        os.system(f'optimize-images images/{file} --reduce-colors')
        list_of_optimized_images.append(file)
    
print("__________________________________________________________")

print("Optimization complete!")

print(f"optimized files: {list_of_optimized_images}")