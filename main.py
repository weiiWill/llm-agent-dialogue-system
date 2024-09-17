from llm_controller import LLMController
from user_interface import UserInterface

def main():
    controller = LLMController()
    ui = UserInterface(controller)
    ui.start_conversation()

if __name__ == "__main__":
    main()