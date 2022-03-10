## Persona
Persona is a modularized Discord self-bot, aimed at those who need fast and customizable services in any Discord context.

### Installing
To build the bot, you will need [install Go](https://go.dev/dl/).

In order to properly use the bot, you're gonna have to include the sub-packages (otherwise all you'll have is the core package, which doesn't really do anything).
We add modularization using [go tags](https://wawand.co/blog/posts/using-build-tags/). A list of available tags can be found in [TAGS.md](TAGS.md).

To build the bot, you need to add the dependencies first:

```
$ cd src/
$ go get ./...
```
You also need to specify your [user token](https://pcstrike.com/how-to-get-discord-token/) in a file called `.env`. The file should look like similar to this:

```
TOKEN=a0EwYFeNeAQzFoYhZX8pmHB26aCZ4ZcV3eMrbw88yVchiGtTjkTZO5H0I3qKC6FlyhwXOidGTIf0zfDmgk8HMA==
```

Now, you can install the bot with a specified number of tags:

```
$ go build -tags "<list of tags seperated by spaces>"
$ go install .
```

To run it, type:

```
persona
```

### Usage

Usage depends on the tags included. To run commands, you typically use the prefix, followed by the tagname, followed by the actual command.

e.g.
```
~general ping
```

For more information, see:

```
~help
```

### FAQ
> Q: Why is it called persona?  
> A: It's a personal bot, and [midnadimple](https://github.com/midnadimple) likes the Persona series.

> Q: Why is it written in [the Go programming language](https://go.dev)?  
> A: Speed is considerable important when it comes to AI.
