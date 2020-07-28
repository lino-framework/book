from atelier.projects import load_projects
for p in load_projects():
    p.load_info()
    locale_dir = p.config['locale_dir']
    if locale_dir:
        print("- :ref:`{}` : {}".format(p.nickname, locale_dir))
