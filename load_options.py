import time
from threading import Thread
from database.client import NoteDB, ManagerDB, Options
from database.local import kv
from assets.note_util import update_note, set_proxy


def load_options():
    db = Options()
    proxy = db.get_option("proxy")
    if proxy:
        set_proxy(proxy)
    kv["owners"] = {
        5665225938,
    }
    Thread(target=update_notes, args=(3600,)).start()
    reload_managers()


def reload_managers():
    db = ManagerDB()
    managers = set()
    for manager in db.list_managers():
        managers.add(manager.user_id)
    kv["managers"] = managers
    print("Managers updated")


def update_notes(interval, call=False):
    db = NoteDB()
    while True:
        time.sleep(interval)
        for note in db.list_notes():
            update_note(note, db)
            print(note.name, " updated")
        if call:
            break
