import os
import random
import string


def id_generator():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


def delete_file(directory, fname):
    try:
        os.remove(fname)  # delete file
        return fname
    except:
        return False



# Main program
if __name__ == '__main__':
    mydir = "PycharmProjects/zipfiles/"
    fname = "cat2.jpg"

    print id_generator()
    print id_generator()
    #print delete_file(mydir, fname)
