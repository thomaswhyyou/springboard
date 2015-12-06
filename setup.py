from setuptools import setup

requires = [
    'pyramid',

    # Templating
    'pyramid_jinja2',

    # Database stuff
    'SQLAlchemy',
    'psycopg2',
    'zope.sqlalchemy',
    'pyramid_tm',
    'sqlalchemy-utils',
]

setup(name='springboard',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = springboard.app:main
      """,
)
