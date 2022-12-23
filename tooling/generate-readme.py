from pathlib import Path

# Resolve from the location of this file the README.md file.
readme_path = Path(__file__).resolve().parent.parent.joinpath("README.md")

preamble = """
VOLTTRON™ is an open source platform for distributed sensing and control. The platform provides services for collecting and storing data from buildings and devices and provides an environment for developing applications which interact with that data.
"""

repositories = [
    {'repo': 'volttron-core', 'pypi_name': 'volttron'},
    'volttron-testing',
    'volttron-listener',
    'volttron-platform-driver',
    'volttron-lib-base-driver',
    'volttron-lib-fake-driver',
    'volttron-lib-base-historian',
    'volttron-lib-sql-historian',
    'volttron-sqlite-historian',
    'volttron-lib-web',
    'volttron-bacnet-proxy',
    'volttron-lib-bacnet-driver',

    # 'volttron-lib-actuator',
    # 'volttron-openadr-ven',
    
    
    # Uncomment the packages below once they are published to PyPi and ready for general release
    # 'volttron-lib-historian-postgres',
    # 'volttron-2030_5',
    # 'volttron-actuator',
    # 'volttron-web-service',
    # 'volttron-auth-service',
    # 'volttron-zmq-service',
    # 'volttron-rmq-service',
]

link_pypi = '[![pypi version](https://img.shields.io/pypi/v/{repo}.svg)](https://pypi.org/project/{repo}/)'
link_pytest = '[![Run Pytests develop](https://github.com/eclipse-volttron/{repo}/actions/workflows/run-tests.yml/badge.svg)](https://github.com/eclipse-volttron/{repo}/actions/workflows/run-tests.yml?query=branch%3Adevelop++)'

with open(readme_path, 'w') as fp:
    fp.write(preamble)
    for repo in repositories:
        # support customized repo and pypi_name for volttron-core is actually
        # published to pypi.
        if isinstance(repo, dict):
            pypi_name = repo.get('pypi_name')
            repo = repo['repo']
        else:
            pypi_name = repo
        fp.write(f"## {repo}\n\n")
        fp.write(link_pypi.format(repo=pypi_name) + "\n")
        fp.write(link_pytest.format(repo=repo) + "\n\n")
