# Persona
> Persona is in it's earliest stages of development, so we recommend that you check back in a few weeks or so. However, if you want to use it anyway, please note that documentation **is** incomplete and innaccurate, so for now, you're by yourself.

Persona is a modularized Discord userbot, created for those who need fast and customizable services in any Discord context.

## Installation
To build the bot, you will first need to install [Python 3.8.*](https://www.python.org/).
After you've done that, head over to the release page of this repository and download the latest release [here](https://github.com/rodofdiscord/persona/releases/latest).

Then, `cd` into the downloaded folder (after extracting) and run:
```
python3 -m pip install poetry
poetry install
cp data/config.json.sample data/config.json
# then edit your user token and poketwo channel id
```

Finally, run:
```
poetry run python launcher.py
```

If everything has been setup correctly, the bot will run without issue, and display a `Logged into account <username>` message, where `username` is your Discord account's username.

## Contributing

1. Fork it (<https://github.com/rodofdiscord/persona/fork>)
2. Create your feature branch - `git checkout -b my-new-feature`
3. Commit your changes - `git commit -am 'Add some feature'`
4. Push to the branch - `git push origin my-new-feature`
5. Create a new Pull Request on GitHub

## Contributors

- [devraza](https://github.com/devraza) - Lead Programmer, Founder & Maintainer
- [midnadimple](https://github.com/midnadimple) - Founder & Maintainer