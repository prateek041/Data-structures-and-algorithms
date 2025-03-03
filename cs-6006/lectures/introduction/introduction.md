---
title: "Introduction to Algorithms"
description: ""
date: February 3, 2025
---

[MIT Notes](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/mit6_006s20_lec1/)

## Introduction to Algorithms

An algorithm is a series of steps, if followed, maps an input to a single output.
Instead of storing a mapping of every input -> output, we create an algorithm that
calculates the output on runtime.

Important things to keep in mind:

- Correctness
- Efficiency

## Model of Computation

> [!NOTE]
> Read about this from [The algorithm design manual](https://mimoza.marmara.edu.tr/~msakalli/cse706_12/SkienaTheAlgorithmDesignManual.pdf)

## Solving problems

| **Search Problems**            | **Sorting Algorithms** | **Shortest Path Algorithms** |
| ------------------------------ | ---------------------- | ---------------------------- |
| Static Array (L01)             | Insertion Sort (L03)   | Breadth First Search (L09)   |
| Linked List (L02)              | Selection Sort (L03)   | DAG Relaxation (L11)         |
| Dynamic Array (L02)            | Merge Sort (L03)       | Depth First Search (L10)     |
| Sorted Array (L03)             | Counting Sort (L05)    | Topological Sort (L10)       |
| Direct-Access Array (L04)      | Radix Sort (L05)       | Bellman-Ford (L12)           |
| Hash Table (L04)               | AVL Sort (L07)         | Dijkstra (L13)               |
| Balanced Binary Tree (L06-L07) | Heap Sort (L08)        | Johnson (L14)                |
| Binary Heap (L08)              |                        | Floyd-Warshall (L18)         |

## Designing your own Algorithms

- Brute Force
- Decrease and Conquer
- Divide and Conquer
- Dynamic Programming
- Greedy/Incremental
