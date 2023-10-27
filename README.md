# Six Degrees of Kevin Bacon

This repository contains an implementation of the "Six Degrees of Kevin Bacon" concept, which posits that anyone in the Hollywood film industry can be linked through their film roles to Kevin Bacon within six steps. The program uses data from the IMDB database to determine the shortest path of connectivity between any two actors, by way of the movies they've appeared in.

## Dependencies

- Python 3.x
- `util.py` from the [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2020/) course by Harvard University.

## Data Structure

The data from IMDB is structured into three CSV files:

- `people.csv`: Maps person IDs to names and birth years.
- `movies.csv`: Maps movie IDs to titles and release years.
- `stars.csv`: Indicates which actors starred in which films by mapping person IDs to movie IDs.

## Usage

1. Clone the repository to your local machine.
```bash
git clone https://github.com/caiogimenes/six-degrees.git
cd six-degrees
```

2. Ensure you have the `util.py` file from the CS50 AI course in the same directory as the script.

3. Run the script using Python.
```bash
python degrees.py [directory]
```
- Replace `[directory]` with the directory containing the CSV files. If omitted, it defaults to a directory named "large".

4. The script will prompt you to enter the names of two actors. It will then compute and display the shortest path of connectivity between them, via the movies they've appeared in.

## Code Overview

- `load_data(directory)`: Loads data from CSV files into memory.
- `main()`: Entry point of the program, handles user input and outputs the results.
- `shortest_path(source, target)`: Implements a breadth-first search to find the shortest path of connectivity between two actors.
- `person_id_for_name(name)`: Resolves a name to a person ID, handling any ambiguities.
- `neighbors_for_person(person_id)`: Finds all actors connected to a given actor by a single movie.

### Shortest Path Algorithm

The `shortest_path` function is central to this program as it implements the breadth-first search algorithm to find the shortest path between two actors:

1. **Initialization**:
   - A new `Node` instance `initial` is created for the source actor.
   - A `QueueFrontier` instance `queue` is created to manage the frontier (the set of nodes to be explored next).

2. **Exploration**:
   - The function enters a loop that continues until the queue is empty (i.e., there are no more nodes to explore).
   - In each iteration, a node is dequeued, and if it represents the target actor, the function constructs and returns the path from the source to the target.
   - Otherwise, the function enqueues all neighboring nodes (i.e., all nodes representing actors who co-starred in a movie with the actor represented by the current node).

3. **Path Reconstruction**:
   - When the target actor is found, the function reconstructs the path from the source actor to the target actor by following the parent pointers from the target node back to the source node, collecting the (movie, actor) pairs along the way.

4. **Output**:
   - The function returns the list of (movie, actor) pairs that represent the shortest path from the source actor to the target actor.
   - If no connection is found between the actors, the function returns `None`, indicating that there is no path of connectivity between the actors.

## License

[MIT](LICENSE)
