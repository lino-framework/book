from atelier.test import make_docs_suite

def load_tests(loader, standard_tests, pattern):
    suite = make_docs_suite(
        "welfare_de", addenv=dict(LINO_LOGLEVEL="INFO"))

    suite.addTests(make_docs_suite(
        "welfare_fr", addenv=dict(LINO_LOGLEVEL="INFO")))
    
    suite.addTests(make_docs_suite(
        "docs", addenv=dict(LINO_LOGLEVEL="INFO")))
    return suite

