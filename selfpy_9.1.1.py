# 9.1.1
#################


def are_files_equal(file1, file2):
    file1id = open(file1)
    file2id = open(file2)
    file1str = file1id.read()
    file2str = file2id.read()
    file1id.close()
    file2id.close()

    if file1str == file2str:
        return True
    else:
        return False
