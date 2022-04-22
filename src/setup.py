import setuptools

setuptools.setup(
    name="bellman_ford",
    version="0.0.1",
    author="Equipo",
    description="Método numérico que resuelva problemas de optimización convexa de pequeña escala.",
    url="https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-joelitam2021",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        'numpy>=1.19.2'
        ],
    python_requires=">=3.7.3",
)
