# setup.py

from setuptools import setup, find_packages


def parse_requirements():
    """Parse requirements.txt and filter out incompatible entries."""
    requirements = []

    with open('requirements.txt', 'r') as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue

            # Skip git URLs (these need to be installed separately)
            if line.startswith('git+'):
                continue

            # Handle jax with find-links by using just the base requirement
            if 'jax[cuda12]' in line and '--find-links' in line:
                requirements.append('jax[cuda12]==0.4.23')
                continue

            # Skip lines with --find-links or other pip-specific flags
            if '--find-links' in line or line.startswith('-'):
                continue

            requirements.append(line)

    return requirements


setup(
    name='lapa-form',
    version='0.1.0',
    packages=find_packages(),
    install_requires=parse_requirements(),
    dependency_links=[
        # Git dependencies that need special handling
        'git+https://github.com/lhao499/tux.git#egg=tux'
    ],
)
