from mpi4py import MPI #Import MPI for Python

comm = MPI.COMM_WORLD
rank = comm.Get_rank() #Get the rank (ID) of the current process
size = comm.Get_size() #Get the total number of processes

if rank == 0:
    #Master process
    for i in range(1, size):  #The master process receives messages from all worker processes
        message = comm.recv(source=i) #Receive a message from worker process with rank i

         #Print the details sent by the worker
        print(f"Received from process {message['rank']}:")
        print(f"  Task assigned: {message['task']}")
        print(f"  Computed result: {message['result']}")
else:
    #Worker process
    #Assign a "task" to each worker process based on its rank
    #Example: sum numbers 1-5 for worker 1, 6-10 for worker 2, etc
    start = (rank - 1) * 5 + 1
    end = rank * 5
    task = f"sum numbers {start} to {end}"
    result = sum(range(start, end + 1)) #Run the computation for this task
     #Includes rank, task description, and computed result
    comm.send({'rank': rank, 'task': task, 'result': result}, dest=0)