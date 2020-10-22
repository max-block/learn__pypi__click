from setuptools import find_packages, setup

setup(
    name="learn",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click==7.1.2", "click-aliases==1.0.1"],
    entry_points={
        "console_scripts": [
            "t0 = t0__test:cli",
            "t1 = t1__basic:cli",
            "t2 = t2__group:cli",
            "t3 = t3__command_aliases:cli",
            "t4 = t4__run_other_commands:cli",
            "t5 = t5__choice_argument:cli",
            "t6 = t6__variadic_arguments:cli",
            "t7 = t7__boolean_flags:cli",
            "t8 = t8__different_name:cli",
        ]
    },
)
