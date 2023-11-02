import subprocess
from multiprocessing import Pool
import time
import random

# Function to clone the Git repository into a specific folder
def clone_repository(clone_index):
    repo_url = "https://github.com/LearningFridayPost/dc-jupyter-notebook.git" 
    destination_folder = f"clones/clone_{clone_index}"
    
    # Generate a random delay of 1 to 5 seconds
    random_delay = random.uniform(1, 20)
    time.sleep(random_delay)
    
    # Run git clone
    subprocess.run(["git", "clone", repo_url, destination_folder])

if __name__ == "__main__":

    # Specify number of clones
    num_clones = 40

    # Create a pool of worker processes
    with Pool(processes=num_clones) as pool:
        # Start the cloning processes
        pool.map(clone_repository, range(num_clones))