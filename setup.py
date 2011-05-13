from setuptools import setup, find_packages

f = open('README.txt')
readme = f.read()
f.close()

setup(
    name='django-userranks',
    version='0.1',
    description='Fun little app which ranks your users into tiers.',
    long_description=readme,
    author='yeago',
    author_email='stephen@yeago.net',
    url='http://github.com/subsume/django-userranks/tree/master',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
