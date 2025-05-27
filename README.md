# Diego's Website

## Getting Started

To get started you just need to run `uv sync`, which will install all the dependencies that this project requires (namely Jinja2 and Gunicorn).
You will also need to install foreman with your favorite package manager: `brew install foreman`.

Once you have your virtual environment installed locally and you have foreman, you can run `source .venv/bin/activate` to activate your venv, and then just run `foreman start` to spin up the little web server.

## Caddy

You can use any reverse proxy tool to do this, but caddy makes this whole process super easy, once installed you can run ` touch Caddyfile` and something similar to the following contents to the file: 

```caddy
www.diegollanes.com diegollanes.com {
    reverse_proxy localhost:8000
    log {
        output file diegollanes.log
    }
}
```

Then, like magic, you can run `caddy start` and have a process run in the background that listens for web requests!
