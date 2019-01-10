def _iterator(list):
    for i in list:
        if i is None or not i:
            return False


def get_by_key(key, val, dict_):
    result = list(filter(lambda obj: obj[key] == val, dict_))
    if result:
        return result[0]
    return {"message":"{} does not exist in our records".format(key)}


def check_list(list_):
    if not list_:
        return {"message": "There are no records"}
    return list_
