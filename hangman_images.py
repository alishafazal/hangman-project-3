class HangmanImages:
    """
    This class holds the hangman images within static methods which are
    displayed at the appropriate time and for the corresponding amount of
    lives left for each level of difficulty
    """
    @staticmethod
    def easy_lives_images():
        """
        Contains a list of hangman images to be displayed for the easy
        difficulty level
        """
        easy_lives_stage = ["""
            ___________
            |/       |
            |        O
            |       /|\\
            |        |
            |       / \\
            |__________
            """, """
            ___________
            |/       |
            |        O
            |       /|\\
            |        |
            |
            |__________
            """, """
            ___________
            |/       |
            |        O
            |        |
            |        |
            |
            |__________
            """, """
            ___________
            |/       |
            |        O
            |        |
            |
            |
            |__________
            """, """
            ___________
            |/       |
            |        O
            |
            |
            |
            |__________
            """, """
            ___________
            |/       |
            |
            |
            |
            |
            |__________
            """, """
            ___________
            |/
            |
            |
            |
            |
            |__________
            """]

        return easy_lives_stage

    @staticmethod
    def medium_lives_images():
        """
        Contains a list of hangman images to be displayed for
        the medium difficulty level
        """
        medium_lives_stage = ["""
            ___________
            |/       |
            |        O
            |       /|\\
            |        |
            |       / \\
            |__________
            """, """
            ___________
            |/       |
            |        O
            |       /|\\
            |        |
            |
            |__________
            """, """
            ___________
            |/       |
            |        O
            |        |
            |        |
            |
            |__________
            """, """
            ___________
            |/       |
            |        O
            |
            |
            |
            |__________
            """, """
            ___________
            |/       |
            |
            |
            |
            |
            |__________
            """, """
            ___________
            |/
            |
            |
            |
            |
            |__________
            """]

        return medium_lives_stage

    @staticmethod
    def hard_lives_images():
        """
        Contains a list of hangman images to be displayed for
        the hard difficulty level
        """
        hard_lives_stage = ["""
            ___________
            |/       |
            |        O
            |       /|\\
            |        |
            |       / \\
            |__________
            """, """
            ___________
            |/       |
            |        O
            |       /|\\
            |        |
            |
            |__________
            """, """
            ___________
            |/       |
            |        O
            |        |
            |        |
            |
            |__________
            """, """
            ___________
            |/       |
            |        O
            |
            |
            |
            |__________
            """, """
            ___________
            |/
            |
            |
            |
            |
            |__________
            """]

        return hard_lives_stage
