import sys
import pymupdf

DATE = "D:20000103120000Z"
AUTHOR = "X"


def main():
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <in.pdf> <out.pdf>")
        exit(1)
    in_pdf = sys.argv[1]
    out_pdf = sys.argv[2]

    doc = pymupdf.open(in_pdf)
    doc.set_metadata({"modDate": DATE, "creationDate": DATE, "modDate": DATE, "author": AUTHOR})
    doc.del_xml_metadata()

    for page in doc.pages():
        for annot in page.annots():
            annot.set_info(title=AUTHOR, modDate=DATE, creationDate=DATE)
            annot.update()
    doc.save(out_pdf, garbage=4)


if __name__ == '__main__':
    main()
