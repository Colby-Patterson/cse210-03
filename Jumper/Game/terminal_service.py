# Creates a list of pictures for the balloon guy and stores them so that we can call on a certain picture
# based on the number of lives that they player has left
class TerminalService:

  def display_balloon(self, tries):
    stages = [ """
              x
             /|\\
             / \\
                     
           ^^^^^^^
              """,
              """
              \ /
               o
              /|\\
              / \\
                     
            ^^^^^^^
              """,
              """
             \   /
              \ /
               o
              /|\\
              / \\
                     
            ^^^^^^^
              """,
              """
              ___
             \   /
              \ /
               o
              /|\\
              / \\
                     
            ^^^^^^^
              """,
              """
             /___\\
             \   /
              \ /
               o
              /|\\
              / \\
                     
            ^^^^^^^
              """,
              """
              ___
             /___\\
             \   /
              \ /
               o
              /|\\
              / \\
                     
            ^^^^^^^
              """
        ]
    return stages[tries]