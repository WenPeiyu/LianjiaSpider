import time
import os


def save_file(data, filename, path=os.getcwd(), filetype="txt"):
    """

    :param data:
    :param filename:
    :param path:
    :param filetype:
    :return:
    """
    if filetype == 'txt':
        with open("{0}/{1}".format(path, filename), "w") as f:
            for i in data:
                f.write("{}\n".format(i))
