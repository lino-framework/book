from atelier.test import make_docs_suite

def load_tests(loader, standard_tests, pattern):
    return make_docs_suite(
        "docs", exclude="docs/specs/printing.rst",
        addenv=dict(LINO_LOGLEVEL="INFO"))

