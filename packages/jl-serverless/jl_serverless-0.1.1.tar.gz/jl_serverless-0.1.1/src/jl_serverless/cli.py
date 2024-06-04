import click
import requests

@click.command()
@click.argument('filename')
def send_script(filename):
    """Sends a script to the server for execution."""
    url = 'https://3ac95a2cb4ce1.notebooksb.jarvislabs.net/run-script/'  
    with open(filename, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
        print("Server response:", response.text)

if __name__ == '__main__':
    send_script()
    
# https://3ac95a2cb4ce1.notebooksb.jarvislabs.net/
