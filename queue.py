queues = {}

def get_queue(chat_id):
    return queues.get(chat_id, [])


def add_to_queue(chat_id, item):
    q = queues.setdefault(chat_id, [])
    q.append(item)


def skip_current(chat_id):
    q = queues.get(chat_id)
    if q:
        q.pop(0)
        return q[0] if q else None
    return None


def is_active(chat_id):
    return bool(queues.get(chat_id))
