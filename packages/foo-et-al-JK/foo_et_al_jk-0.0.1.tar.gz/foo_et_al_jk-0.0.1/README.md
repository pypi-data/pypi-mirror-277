# Foo_package

    This package calculates the fictitious Foo et al. parameterization. When given a shape (default to sphere) and radius it will output the volume.

# Features

    Takes the radius of a sphere and returns its volume

# Usage

    Install the package using the command:

    pip install -i https://test.pypi.org/simple/ foo_et_al_JK==0.0.1

    Import the package using:

    from foo_et_al_JK import foo_et_al

    An example of using the package:
    
    example = foo_et_al.foo_et()
    print(example.getVolume(3))

    This would output: 113.09733552923254