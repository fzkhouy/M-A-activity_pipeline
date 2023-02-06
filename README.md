# M-A-activity_pipeline
> A transformation pipeline so as to reshape this data into a new graph-oriented model to describe mergers-and-acquisition (M&amp;A) activity.
---

### Project structure :
--- 
- **config .py:** The file contains all the statistic variables needed in the project, files paths in our case.
- **.gitignore:** To ensure that certain files will not be tracked by Git.
- **requirements .txt:** For specifying what python packages are required to run the project ( we worked with json and datetime, they are a built in functions).
- **m_a_pipeline.py:** Contains the transformating pipeline.
- **Dockerfile:** The instructions build Docker image automatically.
- **input_data:** Contains sleak profiles and interactions


### Codes logic:
---
> NB: **In this section we are going to understand the logic behind the code**
1. Input data: 
- sealk-profiles.json: company profiles providing information about companies identified by a source.id property.
> sleak profiles are the node of our graph.
- sealk-interactions.json: interactions between profiles referencing a buyer ( subject.id ) and a target ( object.id ). Every interaction carries a status that refers to the progress of the deal.
> sleak interactions are the links between nodes (goes from buyer to target)
2. Graph structure:
> Graph database (like the famous Neo4j) relies on a graph architecture featuring three fundamental components.It is based on a graph structure composed of: Nodes, Relations and Properties. Formally, we can represent a graph-oriented as G = (N, R, P) where N = {N1 ,..., Nk } is a set of graph nodes (companies), R = {R1,..., Rp } is a set of relations between nodes N (interactions) and P = {P1 ,..., Pn } is a set of properties related to each component Ni or Ri ; each property is represented by a key/value pair ( additional informations). 
- Nodes (N) represent the entities; Each node Ni can be formalized as Ni = (idn , Ln, Pn ) where: idn is its identifier it is the source.id in our case, Ln = {L1 , ..., Lm } is a set of labels describing its semantic, for us its only the name of the company and PN is a set of its properties we can add additional data of profiles, for our case it's empty.
• Relationships (R) define the relations between connected nodes (N). Each relation R i can be formalized as Ri = (idr, Lr , N(start) , N(end) , Pr) where idr is its identifier , i choose the dealId to identify the interactions, Lr is its label (status of the deal), N(start) is the identifier of the start node for us is the buyer ( subject.id ), N(end) is the identifier of the end node, the target (object.id) and Pr is a set of its properties ( P = P N ∪ PR ) if we want to add some more informations.

- To do we developped tree function, the first one create a node (take one element of profiles dataset and transform it into a node). The second function do the same thing with interactions to create a relationship. And then the last one is to map and parallelise those functions with both data inputs to give the final graph structure file as a result.

### Instructions to execute the code source:
---
1. Make sure Docker is running on your laptop.
2. Clone this repo
3. In your terminal, enter to the project and then execute the following so you can build the docker image
    ```sh
        docker build -t m-a-activity:1 .
    ```
4. Then, you can run the docker image by executing the following:
    ```sh
        docker run m-a-activity:1
    ```
4. To keep track of the execution and see the result file physically, you can use this command
    ```sh
        docker run -it -v /tmp/:/tmp m-a-activity:1  bash
    ```
