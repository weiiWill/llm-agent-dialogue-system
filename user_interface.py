class UserInterface:
    def __init__(self, controller):
        self.controller = controller

    def start_conversation(self):
        print("Welcome! How can I assist you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Thank you for using our service. Goodbye!")
                break
            response = self.controller.process_input(user_input)
            print("Assistant:", response)