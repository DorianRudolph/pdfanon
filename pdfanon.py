import sys
import pymupdf

DATE = "D:20000103120000Z"


def main():
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <in.pdf> <out.pdf>")
        exit(1)
    in_pdf = sys.argv[1]
    out_pdf = sys.argv[2]

    doc = pymupdf.open(in_pdf)
    print(doc.metadata)
    doc.set_metadata({"modDate": DATE, "creationDate": DATE, "modDate": DATE})
    doc.del_xml_metadata()
    print(doc.metadata)

    for page in doc.pages():
        for annot in page.annots():
            annot.set_info(title='X', modDate=DATE, creationDate=DATE)
            annot.update()
            print(annot.info)
    doc.save(out_pdf, garbage=4)


if __name__ == '__main__':
    main()
