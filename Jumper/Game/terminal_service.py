class TerminalService:

    def display_balloon(self, tries):
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
                   """
        ]
        return stages[tries]