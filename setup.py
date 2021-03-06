import os
from setuptools import Extension, setup


setup(
    name='jaeger_model_proto',
    ext_modules=[
        Extension(
            "jaeger_model_proto", ["jaeger_model_proto.c"],
            extra_compile_args=['-Os', '-fpic']
        )
    ],
    version="0.1.2",
    packages=[],
    license="MIT",
    description="Jaeger protobuf model",
    long_description_content_type="text/markdown",
    url="http://github.com/mosquito/jaeger_model_proto",
    author="Dmitry Orlov",
    author_email="me@mosquito.su",
    provides=["jaeger_model"],
    keywords=["python", "protobuf", "cython"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Natural Language :: Russian",
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
        "Topic :: System",
        "Topic :: System :: Operating System",
    ],
)
