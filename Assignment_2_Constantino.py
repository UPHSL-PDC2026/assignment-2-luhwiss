from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Master process
    for i in range(1, size):
        message = comm.recv(source=i)
        print(f"Received from process {i}: {message}")
else:
    # Worker process
    comm.send(f"Hello from process {rank}", dest=0)