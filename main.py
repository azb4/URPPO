import time
from PIL import Image

q_level = 10
q_step = 255 / q_level
q_colors = [(0, 0, 0), (127, 0, 0), (255, 0, 0), (0, 127, 0),
            (0, 255, 0), (0, 0, 127), (0, 0, 255),
            (127, 0, 127), (127, 127, 0), (0, 127, 127)]


def level(red, green, blue):
    intensity = (red + green + blue) / 3

    for lev in range(10):
        if intensity < (lev + 1) * q_step:
            return lev

    return 0


for k in range(10):
    print('Iteration %s' % k)

    for n in range(3):
        pil_img = Image.open('img/%s.png' % n)
        img = pil_img.convert('RGB')
        start = time.time()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = img.getpixel((i, j))
                img.putpixel((i, j), q_colors[level(r, g, b)])

        img.save('img/%s_CPU.png' % n)
        current_time = time.time()
        end = current_time - start
        print('№%s: %s seconds' % (n + 1, round(end, 2)))
