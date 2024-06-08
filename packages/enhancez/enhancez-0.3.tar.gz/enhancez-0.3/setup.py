from setuptools import setup, find_packages

setup(
    name='enhancez',
    version='0.3',
    packages=find_packages(),
    author='Lalith Kumar Shiyam Sundar ',
    author_email='lalith.shiyamsundar@meduniwien.ac.at',
    url='',  # Add your package's homepage URL here
    description='',  # Add a short description of the package here
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'streamlit',
        'moosez',
        'falconz',
        'pumaz',
        'lionz',
        'halo',
        'altair',
        'd3blocks',
        'SimpleITK',
        'psutil',
        'streamlit_lottie',
        'extra_streamlit_components',
        'streamlit_image_comparison',
        'streamlit-toggle-button-set'
    ],  # List your package's dependencies here
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'enhancez=enhancez.run_streamlit:run',
        ],
    },
)
