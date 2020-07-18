import requests
import click
import json
from pygments import highlight, lexers, formatters

def format_json_response(json_data):
    formatted_json = json.dumps(json_data, sort_keys=True, indent=4)
    highlighted_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    return highlighted_json

@click.command()
@click.option('--name', help='name of the beer')
def search_beers(name):
    click.echo(click.style('searching brewerydb...🍺', fg='blue'))
    brewerydb_url = 'https://sandbox-api.brewerydb.com/v2/search'
    payload = {'key': '89464b3cc474b22ea5dee881ca0b6360', 'type': 'beer', 'q': name}
    json_data = requests.get(brewerydb_url, params=payload).json()
    click.echo(format_json_response(json_data))

if __name__ == '__main__':
    search_beers()