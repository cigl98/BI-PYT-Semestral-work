from editing import *
from image_array import *
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('infile')
parser.add_argument('outfile')
parser.add_argument('--rotate', action='store_true')
parser.add_argument('--mirror', action='store_true')
parser.add_argument('--inverse', action='store_true')
parser.add_argument('--bw', action='store_true')
parser.add_argument('--lighten', type=int, choices=range(1, 101))
parser.add_argument('--darken', type=int, choices=range(1, 101))
parser.add_argument('--sharpen', action='store_true')

args = parser.parse_args()


def do_editing(image: np.array) -> np.array:
    if args.rotate:
        image = rotation(image)
    if args.mirror:
        image = mirror(image)
    if args.inverse:
        image = inverse(image)
    if args.bw:
        image = bw(image)
    if args.lighten:
        image = lighten(image, args.lighten)
    if args.darken:
        image = darken(image, args.darken)
    if args.sharpen:
        image = apply_conv(image, sharpening_kernel)
    return image


def main():
    image = read_image(args.infile)
    image = do_editing(image)
    save_image(image, args.outfile)


if __name__ == "__main__":
    main()
