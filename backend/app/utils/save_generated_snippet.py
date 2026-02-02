import re
import webbrowser
from pathlib import Path

def save_html_code(html_code: str) -> Path:
    """
    Save generated HTML code to a file in the frontend directory.

    Args:
        html_code: The HTML code to be saved.
        filename: The name of the file to save the HTML code to.    
    Returns:
        Path to the saved HTML file.
    base_dir = Path(__file__).parent.parent.parent
    """

    # Remove markdown code fences if model adds them
    html_code = re.sub(r"^```[a-zA-Z]*\n?", "", html_code.strip())
    html_code = re.sub(r"\n?```$", "", html_code).strip()

    # Save HTML file to frontend folder
    base_dir = Path(__file__).parent.parent.parent.parent
    output_dir = base_dir / "frontend"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "generated_app.html"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_code)

    return output_path

def execute_generated_html(file_path: Path):
    """
    Open the generated HTML file in the default web browser.

    Args:
        file_path: Path to the HTML file to be opened.
    """
    webbrowser.open(str(file_path))
