# Bering Strait Sabotage

# Client-side

## Developing client side Javascript

### Setup

1. Start with installing [NVM](https://github.com/nvm-sh/nvm).
2. Install NodeJS and the latest version of NPM. Follow [these instructions](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).
3. Install VUE CLI on global level. `npm install -g @vue/cli`

### Running dev environment

1. cd into the client folder.
2. Run `npm install` to install project dependancies.
3. Start the dev server by running `npm run serve`.
4. This will run the vue dev server to develop the frontend app.
5. Visit [the local adress](http://localhost:8080/) to debug the frontend

# Server-side

## Pipenv

### Installation

We use pipenv as a package manager (such as npm for nodejs) to manage our python packages and dependancies.

1. Make sure you have python installed
2. Make sure you have pip installed
3. Install pipenv `pip install pipenv`
4. Add pipenv (and other python packages) to [system path](https://realpython.com/add-python-to-path/).
5. run `pipenv` to check if pipenv is working.

### Using pipenv in server

To develop on the server side, use pipenv to install the correct packages

2. Make sure you are in the server directory `cd ./server`
3. run `pipenv install --dev`
   This installs the correct dependancies.
4. When you are ready to go to production, lock the pipenv file `pipenv lock`
5. Git pull everything on the server hardware
6. Install the dependancies for production with `pipenv install --ignore-pipfile`
7. For more information [see this documentation](https://realpython.com/pipenv-guide/)

# About

## The Bering Strait Crossing

A Bering Strait crossing is a hypothetical bridge or tunnel that would span the relatively narrow and shallow Bering Strait between the Chukotka Peninsula in Russia and the Seward Peninsula in the U.S. state of Alaska. The crossing would provide a connection linking the Americas and Eurasia.

With the two Diomede Islands between the peninsulas, the Bering Strait could be spanned by a bridge or tunnel.

There have been several proposals for a Bering Strait crossing made by various individuals and media outlets. The names used for them include "The Intercontinental Peace Bridge" and "Eurasia–America Transport Link".[1] Tunnel names have included "TKM–World Link" and "AmerAsian Peace Tunnel". In April 2007, Russian government officials told the press that the Russian government would back a US$65 billion plan by a consortium of companies to build a Bering Strait tunnel.[2]
