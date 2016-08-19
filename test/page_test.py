from bin.shell import shell_lines


def page_list_test():
    return shell_lines('x page list', 40, 45)


def page_text_test():
    return shell_lines('x page text all', 1000, 1100)


def page_diff_test():
    return shell_lines('x page diff', 1, 100)
