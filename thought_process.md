## My thought process while building the solution 

### Approach:

- Made use of sqlite which doesn't require any external dependencies or servers set up. 
- Documented and added comments how much ever I can.
- Some assumptions are made on how much data to be considered and how to show results


## Future scope

- Add tests with increasing functionalities and code coverage
- Use more scalable databases and maybe maintain seperate cache like redis when needed.
- Add security to the handle data via encryption, or de-duplication, if the use cases require it
- Introduce retries for failures.
- Add extensive error handling, monitoring (like latency of processing) for failures
