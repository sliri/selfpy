# 9.3.1
#################


def my_mp3_playlist(file_path):
    source_id = open(file_path, 'r')
    all_lines_list = list()
    for line in source_id:
        line_list = line.split(';')[:-1]
        line_list[2] = float(line_list[2].replace(':', '.'))
        all_lines_list.append(line_list)
    length = len(all_lines_list)
    longest = 0
    performers_list = list()
    for lists in all_lines_list:
        performers_list.append(lists[1])
        if lists[2] > longest:
            longest = lists[2]
            name = lists[0]
        else:
            continue
    max_occurrence = 0
    for element in performers_list:
        if max_occurrence < performers_list.count(element):
            max_occurrence = performers_list.count(element)
            performer = element
        else:
            continue
    final_tuple = (name, length, performer)
    print(final_tuple)

    source_id.close()


def main():
    my_mp3_playlist(r"/home/liron/PycharmProjects/untitled/hangman-ex1.4.2/songs.txt")


if __name__ == "__main__":
    main()
