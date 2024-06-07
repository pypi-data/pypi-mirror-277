from pathlib import Path
from typing import Tuple

from sgelt import mdparse
from sgelt.utils import parse_md_file
from .shortcodes import parser

def parse_markdown_file(mdfile_path: Path) -> Tuple[dict, list]:
    """
    Parse the markdown file into a header and a content

    Args:
        mdfile_path: Path to the markdown file

    Returns:
        tuple: (parsed header of the markdown file,
            parsed content sections of the markdown file)
    """
    header, md_content = parse_md_file(mdfile_path)
    md_content = parser.parse(md_content)
    sections = mdparse.get_sections(md_content)
    
    try:
        header["theme"]["name"]
    except KeyError:  # Default theme
        header["theme"] = {"name": "water"}
    
    return header, sections


def create_menu(sections: list) -> list:
    """
    Create a menu from a collection of sections

    Args:
        sections: Sections of the markdown with an id and a title

    Returns:
        list: A list of menu items with a link href and a text
    """
    menu_links = []
    for section in sections[1:]:
        href = f"#{section['id']}"
        text = section["title"]
        menu_links.append({"href": href, "text": text})
    return menu_links