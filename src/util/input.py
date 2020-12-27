from util.ChoiceError import ChoiceError

def get_option(min, max, input):
    try:
        parsed_input = int(input)
        if not min <= parsed_input <= max:
            raise ChoiceError("That is not a valid option")
        else: return parsed_input
    except ValueError:
        raise ChoiceError("That is not a valid option")

def prompt_option(input):
    string_builder = ""
    for k, v in input.items():
        string_builder += f"({k}) {v}\n"
    return print(string_builder)
