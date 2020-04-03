# 9.3.2
#################


def my_mp4_playlist(file_path, new_song):
    source_id = open(file_path, 'r')
    source_lines = source_id.readlines()
    lines_list = list()
    if len(source_lines) < 3:
        for i in range(3):
            if i < len(source_lines):
                lines_list.append(source_lines[i])
            else:
                if i != 2:
                    lines_list.append('\n')
                else:
                    lines_list.append(new_song)
    else:
        for i in range(0, len(source_lines)):
            if i != 2:
                lines_list.append(source_lines[i])
            else:
                lines_list.append(new_song)
    source_id.close()

    source_id = open(file_path, 'w')
    for item in lines_list:
        source_id.write(item)
    source_id.close()

    source_id = open(file_path, 'r')
    print(source_id.read())


def main():
    new_song = "Python;Unknown;7:23;\n"
    my_mp4_playlist(r"/home/liron/PycharmProjects/untitled/hangman-ex1.4.2/songs.txt", new_song)


if __name__ == "__main__":
    main()
