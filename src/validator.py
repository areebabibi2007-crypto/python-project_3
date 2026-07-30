class Validator:
    """
    Validates user input.
    """

    @staticmethod
    def validate_length(length):

        if length < 6:
            return False, "Password length must be at least 6."

        if length > 50:
            return False, "Password length cannot exceed 50."

        return True, ""