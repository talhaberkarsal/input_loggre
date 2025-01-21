class InputLogger:
    """
    A Python library to capture and log all user inputs from the console.
    """

    def __init__(self, log_file=None):
        """
        Initializes the InputLogger instance.

        :param log_file: Optional log file to save inputs. If None, inputs will only be displayed.
        """
        self.log_file = log_file
        if log_file:
            with open(self.log_file, 'w') as file:
                file.write("Input Logger Initialized\\n")

    def get_input(self, prompt=""):
        """
        Captures and logs user input.

        :param prompt: The prompt displayed to the user.
        :return: The user's input as a string.
        """
        user_input = input(prompt)
        self.log_input(user_input)
        return user_input

    def log_input(self, user_input):
        """
        Logs the user input to the log file if specified.

        :param user_input: The user input to log.
        """
        if self.log_file:
            with open(self.log_file, 'a') as file:
                file.write(user_input + "\\n")
        print(f"Logged: {user_input}")
