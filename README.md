# Site

This repository creates the HSUPipeline website.

Note that created website is hosted via the
[host](https://github.com/HSUPipeline/HSUPipeline.github.io)
repository - this repository is used to organize and create the site content.

## Instructions

Creating the website is managed through the `Makefile`.

To re-deploy the website, run:

`make deploy`

## Details

In addition to the Makefile, this repo contains:
- `_config.yml`: the config file for the site, which gets copied over
- `prep_site.py`: script for getting and converting website content

Note that an interim folder, `outputs`, is created and used when deploying the website.
