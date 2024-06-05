"""ats.web.pages.default module."""

# Imports
import random
import string


class DefaultPageGenerator:
    """A generator class for generating the default page."""

    @staticmethod
    def generate_default_page() -> str:
        """Generate the default page.

        Args:

        Returns:
            str: The generated HTML code.
        """
        random_2d_grid: list[list[dict]] = DefaultPageGenerator.__generate_grid()
        html_grid_elements: str = DefaultPageGenerator.__grid_to_html_elements(random_2d_grid)
        html_output: str = DefaultPageGenerator.__insert_elements_in_template(html_grid_elements)
        return html_output

    @staticmethod
    def __generate_grid() -> list[list[dict]]:
        """Generate a 2d grid with random characters.

        Args:

        Returns:
            list[list[dict]]: The generated 2d grid with random characters.
        """
        chars: list[list[list[int]]] = [
            [
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            ],
            [
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [4, 5],
                [4, 5],
                [4, 5],
                [4, 5],
                [4, 5],
            ],
            [
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1],
                [0, 1, 2, 3, 4, 5],
                [0, 1, 2, 3, 4],
                [0, 1],
                [0, 1],
            ],
            [
                [3, 4, 5, 6, 7, 8, 9],
                [2, 3],
                [2, 3],
                [0, 1],
                [2, 3],
                [2, 3],
                [3, 4, 5, 6, 7, 8, 9],
            ],
            [
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            ],
            [
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 8, 9],
                [0, 1, 8, 9],
                [0, 1, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            ],
            [
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 8, 9],
                [0, 1, 8, 9],
                [0, 1, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            ],
            [
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            ],
            [
                [4, 5],
                [4, 5],
                [4, 5],
                [4, 5],
                [],
                [4, 5],
                [4, 5],
            ],
            [
                [0, 1, 2, 3, 4, 5, 6],
                [6, 7],
                [6, 7],
                [8, 9],
                [6, 7],
                [6, 7],
                [0, 1, 2, 3, 4, 5, 6],
            ],
        ]

        char_width: int = 10  # The height of a character
        char_height: int = 7  # The width of a character
        space_between_chars: int = 2  # The space between characters
        number_of_chars: int = len(chars)

        # Number of characters height:
        #  The height of a character * the number of characters to hide to facilitate all characters
        #  The needed empty space between characters * the number of characters -1 because we only need height between characters
        #  2 * the space between characters to add lines before the first and after the last character
        grid_height: int = (
            (char_height * number_of_chars) + (space_between_chars * (number_of_chars - 1)) + (2 * space_between_chars)
        )
        grid_width: int = 80  # Number of characters width. This needs to be a even number!

        # Create a 2 dimensional list that contains random letters and numbers
        random_2d_grid: list[list[dict]] = []
        for height_index in range(grid_height):
            row: list[dict] = []
            for width_index in range(grid_width):
                grid_value = {
                    "value": random.choice(string.ascii_lowercase + string.digits),  # nosec B311
                    "different": False,
                }
                row.append(grid_value)
            random_2d_grid.append(row)

            # Debugging
            # print("".join(row))

        # Loop through the chars that need to be inserted
        for index, letter in enumerate(chars):
            half_grid_index: int = int(grid_width / 2)  # Get the index of the middle of the grid

            # The start position in the grid
            start_position = (char_height * index) + (space_between_chars * (index - 1)) + (2 * space_between_chars)

            # Loop through the letters to generate
            for index, line_positions in enumerate(letter):
                grid_line_index = start_position + index

                # Calculate the position in the row and update the different variable to True to make it different
                for position in line_positions:
                    grid_row_index = half_grid_index + (position - int(char_width / 2))
                    random_2d_grid[grid_line_index][grid_row_index]["different"] = True
        return random_2d_grid

    @staticmethod
    def __grid_to_html_elements(random_2d_grid: list[list[dict]]) -> str:
        """Transform the 2d random grid into html elements.

        Args:
            random_2d_grid (list[list[dict]]): The random 2d grid.

        Returns:
            str: The transformed 2d grid into html elements.
        """
        # Transform the 2d grid into a html page
        html_elements: str = ""
        color_a: str = "83,84,85"
        color_b: str = "82,83,84"
        for line in random_2d_grid:
            for char_dict in line:
                color: str = ""
                if char_dict["different"]:
                    color = color_a
                else:
                    color = color_b
                html_element = f'<span style="color: rgb({color});">{char_dict["value"]}</span>'
                html_elements = html_elements + html_element
            html_element = "<br>"
            html_elements = html_elements + html_element
        return html_elements

    @staticmethod
    def __insert_elements_in_template(html_elements: str) -> str:
        """Insert html elements in a html page template.

        Args:
            html_elements: The html_elements that contain the random 2d grid characters.

        Returns:
            str: The html template that contains the inserted elements.
        """
        html_template: str = """
        <html>
            <head>
                <title>Almost the Same is Still Different</title>
            </head>
            <body style="font-family:monospace;">
                <p>{html_elements}</p>
            </body>
        </html>
        """

        # Insert the html elements in the html template
        html_output: str = html_template.replace("{html_elements}", html_elements)
        return html_output
