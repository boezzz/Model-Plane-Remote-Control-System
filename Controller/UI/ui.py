class UI:
    def __init__(self):
        print("ui init")

    def run(self):
        print("ui run")

    def _service(self):
        pass

    def change_info(self, new_info):
        print("info change to", new_info)

    def get_msg(self):
        operation = {"operation"}
        return operation

    def ui_checklist(self):
        print("ui checklist")
        return 1
        pass

    def __del__(self):
        print("ui del")