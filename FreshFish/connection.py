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
    start_container(container)


def del_image(image_name_tag):
    """Delete image by its image_name_tag."""
    cli.remove_image(image_name_tag, True)


def get_containers():
    """Get all the containers that are running or not."""
    return cli.containers(all=True)


def start_container(container):
    """Run stoped container."""
    cli.start(container)


def stop_container(container):
    """Stop running container."""
    cli.kill(container)


def del_container(container):
    """Delete the container."""
    cli.remove_container(container, force=True)


def kill_container(container):
    """Kill the running container."""
    cli.kill(container)


def restart_container(container):
    """Restart container."""
    cli.restart(container)

if __name__ == '__main__':
    del_container('7cd8acd0aad9')
