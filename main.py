import os
import sys

input_dir = sys.argv[1]
output_dir = sys.argv[2]
max_depth = sys.argv[3]
max_depth = int(max_depth)
if max_depth != 0:
    max_depth -= 1
for i in os.walk(input_dir):
    pth = i[0].split('/')[1:]
    depth_path = pth[len(pth) - max_depth:]
    create = output_dir + "/"
    for j in depth_path:
        create += j + "/"
        if not os.path.isdir(create):
            os.system(f"mkdir {create}")
    for file in i[2]:
        os.system(
                f'cp {i[0]}/{file} {create}'
            )
