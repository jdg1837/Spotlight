import line_detection as ld
import blob_detection as bd

def main():
    inputfile = ld.detect_lines('../images/parkinglot.png')
    bd.detect_blobs(inputfile)

if __name__ == '__main__':
    main()
