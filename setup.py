"""Setup script for tau2-adv-bench."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="tau2-adv-bench",
    version="1.0.0",
    author="Anonymous",
    author_email="",
    description="Adversarial Robustness Evaluation for Conversational Agents in Dual-Control Environments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neurips2026-submission/tau2-adv-bench",
    project_urls={
        "Bug Tracker": "https://github.com/neurips2026-submission/tau2-adv-bench/issues",
        "Documentation": "https://github.com/neurips2026-submission/tau2-adv-bench/tree/main/docs",
        "Source Code": "https://github.com/neurips2026-submission/tau2-adv-bench",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "tau-adversarial=tau_adversarial.run_adversarial:main",
        ],
    },
    include_package_data=True,
    package_data={
        "tau_adversarial": [
            "../data/domains/*/tasks_adversarial.json",
        ],
    },
    keywords="adversarial-robustness conversational-ai agent-safety llm-evaluation benchmark",
    zip_safe=False,
)
