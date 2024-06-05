import setuptools

setuptools.setup(
    name="doc2tei-CERTIC",
    version="0.0.98",
    author="Mickaël Desfrênes",
    author_email="mickael.desfrenes@unicaen.fr",
    description="Convert ODT and DOCX files to TEI",
    long_description="Convert ODT and DOCX files to TEI",
    long_description_content_type="text/plain",
    url="https://git.unicaen.fr/fnso/i-fair-ir/xsl-tei-circe",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CeCILL-B Free Software License Agreement (CECILL-B)",
        "Operating System :: OS Independent",
    ],
    install_requires=["argh"],
    python_requires=">=3.7",
    include_package_data=True,
    entry_points={
        "console_scripts": ["doc2tei=doc2tei.__main__:run_cli"],
    },
)
