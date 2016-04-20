"""Create julia or mandelbrot set."""
from PIL import Image


def return_iteration(c, z):
    """
    Take complex numbers c and z and see if they "blow out" in max_iterations.

    args:
    c,z - complex numbers
    returns:
    Number of iterations it took complex number to blow out. If it doesn't,
    return  None.
    """
    for i in range(100):
        z = z ** 2 + c
        if abs(z) > 2:
            return i
    return None


def create_mandelbrot(mandelbrot, filename, julia_number=0):
    """
    Create mandelbrot set or Jula set.

    Args:
    mandelbrot - bool, if is True make mandelbrot set, if is False, create
    Julia set
    juliet_number - complex number for Julia set
    filename - name of the image to save

    Returns:
    Image saved as filename
    """
    image = Image.new("RGB", (900, 900))

    l = []
    init = -2.25
    for i in range(0, 900):
        l.append(init + (float(i) / 200))

    for num_y in range(0, 900):

        y = l[num_y]

        for num_x in range(0, 900):
            x = l[num_x]

            if mandelbrot is True:
                color_value = return_iteration(complex(x, y), z=0)
            else:
                color_value = return_iteration(
                    julia_number, complex(x, y))
            if color_value is None:
                point1 = (0, 0, 0)
            else:
                r = color_value % 3 * 15
                g = color_value % 6 * 16
                b = color_value % 2 * 15
                point1 = (r, g, b)
            image.putpixel((num_x, num_y), point1)
    image.save(filename)

create_mandelbrot(mandelbrot=True,
                  filename="mandelbrot.png")
