# 9.2.2
#################


def copy_file_content(source, destination):
    source_id = open(source, 'r')
    destination_id = open(destination, 'w')
    for line in source_id:
        destination_id.write(line)
    source_id.close()
    destination_id.close()


def main():
    copy_file_content(r"/home/liron/PycharmProjects/untitled/hangman-ex1.4.2/copy.txt",
                      r"/home/liron/PycharmProjects/untitled/hangman-ex1.4.2/paste.txt")


if __name__ == "__main__":
    main()
