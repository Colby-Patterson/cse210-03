
class Balloon:
    
    tires = 5
    _guessed_letter = []

    pass



def display_balloon(tries):
    stages = [ """
                        x
                       /|\
                       / \
                     
                     ^^^^^^^
                """,
                """
                       \ /
                        o
                       /|\
                       / \
                     
                     ^^^^^^^
                """,
                """
                      \   /
                       \ /
                        o
                       /|\
                       / \
                     
                     ^^^^^^^
                """,
                """
                       ___
                      \   /
                       \ /
                        o
                       /|\
                       / \
                     
                     ^^^^^^^
                """,
                """
                      /___\
                      \   /
                       \ /
                        o
                       /|\
                       / \
                     
                     ^^^^^^^
                """,
                """
                       ___
                      /___\
                      \   /
                       \ /
                        o
                       /|\
                       / \
                     
                     ^^^^^^^
                """]
    return stages[tries]