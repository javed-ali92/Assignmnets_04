SENTENCE_START : str ="The boy sings"

def main():
    adjective : str = input("\033[1;3mEnter an adjective and press enter: \033[0m")
    noun  : str = input("\033[1;3mEnter a noun and press enter: \033[0m")
    verb : str = input("\033[1;3mEnter a verb and press enter: \033[0m")

    sentence_end : str = SENTENCE_START + " " + adjective + " " + noun + " " + verb
    print(sentence_end)

if __name__ == '__main__':
    main()