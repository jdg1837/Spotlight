import line_detection as ld
import blob_detection as bd

def main():
    ld.detect_lines('parkinglot.jpg')
    bd.detect_blobs('cars_demo.jpg')

if __name__ == '__main__':
    main()
