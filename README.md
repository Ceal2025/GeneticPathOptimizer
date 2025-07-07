# Simple Genetic Path Optimizer

A minimal implementation of a Genetic Algorithm to find the shortest path on a circular graph with 5 nodes (shaped like a regular pentagon).

---
Problem Description

- There are 5 locations (labeled 0 to 4) arranged in a regular pentagon.
- A valid route must visit each location exactly once.
- Travel time between adjacent nodes is 1, and 2 for non-adjacent nodes.
- The goal is to find the route with the minimum total travel time.

---

Algorithm Overview

- Initial Population: 10 randomly generated routes
- Selection: The top 2 shortest routes are selected as parents
- Crossover: Partial mapping crossover (PMX-inspired)
- Mutation: Random mutation via swap, reverse, or shuffle (with a certain probability)
- Evaluation: Fitness is based on total travel time
- Termination: Loop continues until at least 6 routes reach the optimal value or generation limit (100) is reached
