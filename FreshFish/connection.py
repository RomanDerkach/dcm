from docker import Client
cli = Client(base_url='unix://var/run/docker.sock', version='auto')


def get_images():
    print cli.containers()
