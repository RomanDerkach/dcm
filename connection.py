from docker import Client
cli = Client(base_url='unix://var/run/docker.sock', version='auto')

print cli.containers()
