# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['medicraft',
 'medicraft.datasets',
 'medicraft.experiments',
 'medicraft.models',
 'medicraft.pipeline',
 'medicraft.pipeline.blocks',
 'medicraft.trackers',
 'medicraft.trainers',
 'medicraft.utils',
 'medicraft.validation']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML==6.0.1',
 'denoising-diffusion-pytorch==1.9.4',
 'ema-pytorch==0.3.1',
 'lightning==2.2.1',
 'matplotlib==3.8.4',
 'pandas==2.2.2',
 'pillow==10.3.0',
 'pydantic==2.7.2',
 'scikit-learn==1.4.2',
 'seaborn==0.13.2',
 'torch>=2.1.1,<3.0.0',
 'torchmetrics==1.3.1',
 'torchvision>=0.16.1,<0.17.0',
 'tqdm==4.66.2',
 'umap-learn==0.5.5',
 'wandb==0.16.3']

setup_kwargs = {
    'name': 'medicraft',
    'version': '0.9.2',
    'description': 'Medicraft synthetic dataset generator',
    'long_description': '# Medicraft\n\n\n## About \n\nThe medical imaging analysis using machine learning encounters challenges such as limited and imbalanced datasets, often constrained by privacy concerns related to patient information. The Medicraft project addresses these limitations by developing software capable of generating synthetic and diverse medical datasets from imaging information. In cooperation with the University Clinical Hospital in Poznan this tool utilizes OCT eye scans, featuring images with abnormalities like tumors and melanomas. To reduce the scarcity of real data, for medically rare cases, the solution uses diffusion models (Denoising Diffusion Probabilistic Model) to create synthetic balanced datasets which can facilitate better research and education in machine learning for medical image analysis and classification. The project uses a data-driven learning approach focused on analyzing the generated data, where synthetic images are analyzed for accuracy with the medical team, in order to achieve the best possible result.\n\n\n## Documentation\nThe documentation for the project can be found [here](https://drfifonz.github.io/medicraft/index.html).\n\n## Installation\n\n###  Using conda (recomended)\n Create an environment from the `environment.yml` file:\n ```bash\n conda env create -f environment.yml\n```\n### Using pip\nInstall the required packages using pip:\n```bash\npip install -r requirements.txt\n```\n\n### As a package (torch dependencies needs to be solved manually)\nTo install the project as a package, run the following command:\n```bash\npip install medicraft\n```\n\n## Post-Installation Steps\nAfter successfully installing Medicraft, it is highly recommended to familiarize yourself with the documentation. You can find the detailed documentation [here](https://drfifonz.github.io/medicraft/index.html).\n\n## Usage\nTo learn how to run the project, refer to the usage instructions provided in the documentation [here](https://drfifonz.github.io/medicraft/usage.html).\n\nFor running a project create `config.yml` file and run the following command:\n```bash\npython src/main.py -f config.yml\n```\nSee config examples here: [configs](https://drfifonz.github.io/medicraft/examples.html#example-section)\n\n\n\n\nFor more information on how to install the project, please refer to the [installation guide](https://drfifonz.github.io/medicraft/installation.html).\n\n---\n ### The conference poster provides information about the project. You can find it [here](docs/conference_poster.pdf).\n',
    'author': 'Filip Patyk',
    'author_email': 'fp.patyk@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/drfifonz/medicraft',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
