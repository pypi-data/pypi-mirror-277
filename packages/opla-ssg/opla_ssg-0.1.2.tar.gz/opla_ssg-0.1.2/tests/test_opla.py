import pytest
from pathlib import Path
from opla import opla, payload, markdown, bibliography, shortcodes, templating
import sys


@pytest.fixture
def theme():
    return "theme:\n    name: materialize"


class TestParseMarkdownFile:
    @pytest.fixture
    def setup_dir(self, tmp_path, theme) -> Path:
        """Create a markdown file with a header and sections for testing"""
        data = f"""\
---
title: Ma page perso
name: Erica
occupation: Chargée de recherche
{theme}
---

## Section 1

Section 1 content - Section 1 content Section 1 content - Section 1 content Section 1 content - Section 1 content
Section 1 content - Section 1 content
Section 1 content - Section 1 content

## Section 2

### Section 2.1

Section 2.1 content Section 2.1 content - Section 2.1 content

### Section 2.2

Section 2.2 content Section 2.2 content - Section 2.2 content
Section 2.2 content Section 2.2 content - Section 2.2 content

"""
        with open(tmp_path / "test.md", "w") as f:
            f.write(data)
        mdfilepath = tmp_path / Path("test.md")

        return mdfilepath

    @pytest.mark.parametrize("theme", ["theme:\n    name: materialize", ""])
    def test_parse_markdown_file_header(self, setup_dir, theme):
        header, _ = markdown.parse_markdown_file(setup_dir)

        expected = {
            "title": "Ma page perso",
            "name": "Erica",
            "occupation": "Chargée de recherche",
            "theme": {"name": "water"},
        }

        if theme == "":
            assert header == expected
        else:
            expected["theme"] = {"name": "materialize"}
            assert header == expected

    def test_parse_markdown_file_sections(self, setup_dir):
        _, sections = markdown.parse_markdown_file(setup_dir)

        assert len(sections) == 2


def test_create_menu(tmp_path):
    data = """---
title: Ma page perso
name: Joanna
occupation: Chargée de recherche
theme: 
    name: materialize
---
## Section 1

Section 1 content - Section 1 content Section 1 content - Section 1 content Section 1 content - Section 1 content
Section 1 content - Section 1 content
Section 1 content - Section 1 content

## Section 2

### Section 2.1

Section 2.1 content Section 2.1 content - Section 2.1 content

### Section 2.2

Section 2.2 content Section 2.2 content - Section 2.2 content
Section 2.2 content Section 2.2 content - Section 2.2 content

## Section 3

Section 3 content

"""

    with open(tmp_path / "test.md", "w") as f:
        f.write(data)

    mdfilepath = tmp_path / Path("test.md")
    _, (sections, _) = markdown.parse_markdown_file(mdfilepath)
    menu = markdown.create_menu(sections)

    assert menu == [
        {"href": "#section-2", "text": "Section 2"},
        {"href": "#section-3", "text": "Section 3"},
    ]


def test_argparse():
    parser = opla.parse_args(["mdfile"])
    assert parser.mdfile is not None


def test_publications():
    publications = bibliography.get_publications("idHal")
    assert isinstance(publications, dict)


class TestPublicationsHandlerHal:
    @pytest.fixture
    def setup_pub(self):
        pub = shortcodes.HAL_PUBLICATIONS = {"ART": ["Example of ART publication text"]}
        yield pub

    def test_no_idhal(self, setup_pub):
        kwargs = {"doctype": "ART"}

        with pytest.raises(SystemExit) as exception:
            shortcodes.publications_handler_hal(None, kwargs, setup_pub)

        assert (
            exception.value.args[0]
            == "Publication shortcode: idhal is a required argument"
        )

    def test_no_doctype(self, setup_pub):
        kwargs = {"idhal": "idhal"}

        with pytest.raises(SystemExit) as exception:
            shortcodes.publications_handler_hal(None, kwargs, setup_pub)

        assert (
            exception.value.args[0]
            == "Publication shortcode: doctype is a required argument"
        )

    def test_unknown_doctype(self, setup_pub):
        kwargs = {"idhal": "idhal", "doctype": "PUB"}

        with pytest.raises(KeyError) as exception:
            shortcodes.publications_handler_hal(None, kwargs, setup_pub)

        assert (
            exception.value.args[0]
            == f"Publication shortcode: doctype {kwargs['doctype']} not found in HAL publications"
        )

    def test_publications_handler(self, setup_pub):
        kwargs = {"idhal": "idhal", "doctype": "ART"}
        content = shortcodes.publications_handler_hal(None, kwargs, setup_pub)

        assert "Example of ART publication text" in content


def test_publications_handler_bibtex(tmp_path):
    data = """
            @article{heu:hal-03546417,
  TITLE = {{Holomorphic Connections on Filtered Bundles over Curves}},
  AUTHOR = {Heu, Viktoria and Biswas, Indranil},
  URL = {https://hal.science/hal-03546417},
  JOURNAL = {{Documenta Mathematica}},
  PUBLISHER = {{Universit{\"a}t Bielefeld}},
  YEAR = {2013},
  KEYWORDS = {2010 Mathematics Subject Classification: 14H60 ; 14F05 ; 53C07 Keywords and Phrases: Holomorphic connection ; filtration ; Atiyah bundle ; parabolic subgroup},
  HAL_ID = {hal-03546417},
  HAL_VERSION = {v1},
}
            """
    with open(tmp_path / "test.html", "w") as f:
        f.write(data)

    file = tmp_path / "test.html"

    kwargs = {"bibtex": file}
    res = shortcodes.publications_handler_bibtex(None, kwargs, None)

    assert "Holomorphic Connections on Filtered Bundles over Curves" in res


def test_create_output_directory(tmp_path):
    dir = tmp_path / Path("output")
    payload.create_output_directory(dir)

    file = dir / "coco.txt"
    file.touch()

    payload.create_output_directory(dir)
    assert dir.exists()


class TestCopyFiles:
    @pytest.fixture
    def setup_dir(self, tmp_path):
        dir = payload.create_output_directory(tmp_path / Path("dir"))
        return dir

    def test_water(self, setup_dir):
        header = {"theme": {"name": "water"}}
        payload.copy_files(header, setup_dir)
        assert (Path(setup_dir) / "water/static").exists()

    def test_custom_list(self, setup_dir):
        header = {
            "theme": {
                "name": "rawhtml",
                "custom": [Path(__file__).parent / "data/css/index2.css"],
            }
        }
        payload.copy_files(header, setup_dir)
        assert (Path(setup_dir) / "custom/index2.css").exists()

    def test_custom_single(self, setup_dir):
        header = {
            "theme": {
                "name": "rawhtml",
                "custom": Path(__file__).parent / "data/css/index2.css",
            }
        }
        payload.copy_files(header, setup_dir)
        assert (Path(setup_dir) / "custom/index2.css").exists()

    def test_custom_dict_css_list(self, setup_dir):
        header = {
            "theme": {
                "name": "rawhtml",
                "custom": {"css": [Path(__file__).parent / "data/css/index2.css"]},
            }
        }
        payload.copy_files(header, setup_dir)
        assert (Path(setup_dir) / "custom/css/index2.css").exists()

    def test_custom_dict_css_single(self, setup_dir):
        header = {
            "theme": {
                "name": "rawhtml",
                "custom": {"css": Path(__file__).parent / "data/css/index2.css"},
            }
        }
        payload.copy_files(header, setup_dir)
        assert (Path(setup_dir) / "custom/css/index2.css").exists()

    def test_custom_dict_js_list(self, setup_dir):
        header = {
            "theme": {
                "name": "rawhtml",
                "custom": {
                    "js": [
                        Path(__file__).parent
                        / "data/bootstrap-5.3.3-dist/js/bootstrap.min.js"
                    ]
                },
            }
        }
        payload.copy_files(header, setup_dir)
        assert (Path(setup_dir) / "custom/js/bootstrap.min.js").exists()

    def test_custom_dict_js_single(self, setup_dir):
        header = {
            "theme": {
                "name": "rawhtml",
                "custom": {
                    "js": Path(__file__).parent
                    / "data/bootstrap-5.3.3-dist/js/bootstrap.min.js"
                },
            }
        }
        payload.copy_files(header, setup_dir)
        assert (Path(setup_dir) / "custom/js/bootstrap.min.js").exists()

    def test_materialize(self, setup_dir):
        header = {"theme": {"name": "materialize"}}
        payload.copy_files(header, setup_dir)
        assert (Path(setup_dir) / "materialize/static").exists()

    def test_data(self, setup_dir):
        header = {
            "theme": {"name": "rawhtml"},
            "data": [
                Path(__file__).parent / "data/img",
                Path(__file__).parent / "data/Resume.pdf",
            ],
        }
        payload.copy_files(header, setup_dir)
        assert Path(setup_dir / "img").exists()


class TestGetTemplate:
    def test_materialize(self):
        header = {"theme": {"name": "materialize"}}
        template = opla.get_template(header)

        assert (
            Path(template.filename)
            == templating.TEMPLATES_PATH / "materialize/templates/index.j2.html"
        )

    def test_rawhtml(self):
        header = {"theme": {"name": "rawhtml"}}
        template = opla.get_template(header)
        assert Path(template.filename) == templating.TEMPLATES_PATH / Path(
            "base/templates/base.j2.html"
        )

    def test_unknown_theme(self):
        header = {"theme": {"name": "doesnotexist"}}
        with pytest.raises(ValueError, match=r"Unknown theme name: 'doesnotexist'"):
            opla.get_template(header)


def test_main(tmp_path):
    data = """---
title: Ma page perso
name: Joanna
occupation: Chargée de recherche
theme: 
    name: materialize
    color: teal
---
## Section 1

Section 1 content - Section 1 content Section 1 content - Section 1 content Section 1 content - Section 1 content
Section 1 content - Section 1 content
Section 1 content - Section 1 content

## Section 2
### Section 2.1
Section 2.1 content Section 2.1 content - Section 2.1 content
### Section 2.2
Section 2.2 content Section 2.2 content - Section 2.2 content
Section 2.2 content Section 2.2 content - Section 2.2 content"""

    with open(tmp_path / "test.md", "w") as f:
        f.write(data)
    file = tmp_path / "test.md"
    dir = tmp_path / "dirtest"
    sys.argv = ["opla", str(file), "-o", str(dir)]
    opla.main()
    assert (dir / "index.html").exists()
