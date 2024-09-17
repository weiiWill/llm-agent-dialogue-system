from backend_interface import BackendInterface

class TicketHandler:
    def __init__(self):
        self.backend = BackendInterface()

    def process(self, user_input, dialogue_state):
        # 实现建单处理逻辑
        # 使用 self.backend 与后端交互
        pass