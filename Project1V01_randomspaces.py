import Project1V01 as pr
import random as rd

#we Define a function to generate random spanning vectors
def random_spanning_vectors(num_vectors,num_coordinates):
    M = [[None] * num_coordinates for _ in range(num_vectors)]
    for row in range(num_vectors):
        for column in range(num_coordinates):
            M[row][column] = rd.uniform(-10,10)
    return M

#We define a function to evaluate the expected dimension of a given number of vectors and subspace of R^n.
def expected_dimension(num_trials, num_vectors, num_coordinates):
    running_count = 0
    for i in range(num_trials):
        running_count += pr.minor(random_spanning_vectors(num_vectors, num_coordinates))
    expectation = running_count / num_trials
    return expectation
