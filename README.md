# 🗺️ Roundtrip Route Optimization - Kenya Counties

This project calculates the **shortest roundtrip route** that starts and ends in **Nairobi**, visiting all other Kenyan counties exactly once.

## 🚀 Project Overview

The goal is to solve a variation of the **Traveling Salesman Problem (TSP)** using brute-force search. The approach explores **all possible routes** between counties, with Nairobi fixed as both the starting and ending point.

### ✨ Key Features
- Uses Python’s `itertools.permutations()` to generate all route permutations (excluding Nairobi).
- Calculates the total distance of each route.
- Identifies the shortest complete roundtrip starting and ending in Nairobi.

## 🧠 How It Works

1. Nairobi is fixed as the starting and ending point.
2. All other counties are permuted to create every possible visiting order.
3. Each route is evaluated by summing the distances between counties.
4. The shortest total distance is selected as the optimal path.

## 🧰 Technologies Used

- Python 3
- `itertools.permutations` for generating routes
- (Optional) Custom distance matrix or API to calculate distances

## 📂 File Structure

