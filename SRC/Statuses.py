
def get_files_list():
    files_list = []
    return files_list


def get_statuses_list(files_list):
    status_list = []
    return status_list


def get_docs_statuses():
    files_list = get_files_list()
    status_list = get_statuses_list(files_list)
    return status_list


status_list = get_docs_statuses()