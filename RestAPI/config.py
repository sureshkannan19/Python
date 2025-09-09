import sys

dir = "C://Users//SureshBabu//PycharmProjects//PythonProject//SqlalchemyLearning"
is_loaded = False


def load_dir():
    global is_loaded
    if not is_loaded:
        sys.path.append(dir)
        is_loaded = True
    return dir


# load_dir()
