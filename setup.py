from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
]

setup(name='springboard',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = springboard.app:main
      """,
)
