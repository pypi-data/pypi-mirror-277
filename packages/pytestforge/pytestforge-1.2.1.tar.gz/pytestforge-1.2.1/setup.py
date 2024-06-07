from setuptools import setup

setup(
    name='pytestforge',
    version='1.2.1',
    description='TestForge pytest plugin',
    license='MIT',
    packages=['pytestforge'],
    author='Monq Digital Lab',
    author_email='askformonq@monqlab.com',
    keywords=['monq', 'pytest'],
    install_requires=['requests', 'selenium==3.141.0', 'pytest==6.1.0', 'allure-pytest==2.12.0',
                      'seleniumwrapper==0.5.4', 'urllib3==1.26.12'],
    entry_points={"pytest11": ["pytestforge = pytestforge.plugin"]},
    classifiers=["Framework :: Pytest"],
    python_requires='>=3.6'
)
