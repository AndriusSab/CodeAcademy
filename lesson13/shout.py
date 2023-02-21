def echo(text: str, repetitions: int = 5) -> str:
    """Imitate a real-world echo."""
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"  #\n  - printina vis kitoje eileje - break line
    return f"{echoed_text.lower()}"


if __name__ == "__main__":

    text = input("Yell something at a mountain: ")
    print(echo(text))