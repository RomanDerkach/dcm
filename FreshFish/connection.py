"""Module for working with docker..."""

from docker import Client
cli = Client(base_url='unix://var/run/docker.sock', version='auto')


def get_images():
    """Get all images from docker pull."""
    return cli.images()


def run_container(image_name_tag):
    """Run container from image id."""
    host_config = cli.create_host_config(port_bindings={80: ''})
    container = cli.create_container(image=image_name_tag,
                                     detach=True, stdin_open=True,
                                     ports=[80],
                                     host_config=host_config)
    cli.start(container)


def del_image(image_name_tag):
    """Delete image by its image_name_tag."""
    cli.remove_image(image_name_tag, True)

if __name__ == '__main__':
    print get_images()
