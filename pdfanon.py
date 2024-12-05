import sys


def main():
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <in.pdf> <out.pdf>")
        exit(1)
    in_pdf = sys.argv[1]
    out_pdf = sys.argv[2]
    print(in_pdf, out_pdf)

if __name__ == '__main__':
    main()