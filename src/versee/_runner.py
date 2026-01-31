import sys

from streamlit.web import cli as stcli

from versee._web import web


def run_streamlit():
    sys.argv = ["streamlit", "run", __file__, "--"] + sys.argv[1:]
    sys.exit(stcli.main())


if __name__ == "__main__":
    web()
