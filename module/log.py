from module.time import format_time


def log_format(local_timezone, content, status):
    """
    此函数将返回一个标准的日志内容。

    :param local_timezone: 本地时区。请在调用时填写正确。
    :param content: 内容。
    :param status: 本条日志的严重程度。
    :return: 一个标准的日志字符串
    """
    local_time = format_time(str(local_timezone))
    est_time = format_time('EST')
    priority = "[" + str(status).upper() + "]"
    final_time = local_time + " (" + est_time + ") "
    return priority + final_time + content
