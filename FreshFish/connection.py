"""Module for working with docker..."""

from docker import Client
cli = Client(base_url='unix://var/run/docker.sock', version='auto')


def get_images():
    """Get all images from docker pull."""
    return cli.images()

if __name__ == '__main__':
    get_images()
