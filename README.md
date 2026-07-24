# 🔢 Numerical Techniques — Python Lab

> A complete collection of Numerical Methods implemented in Python, organized topic-wise for easy learning and reference.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Topics](https://img.shields.io/badge/Topics-6-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

---

## 📚 About

This repository contains Python implementations of all major **Numerical Techniques** covered in the B.Tech/B.Sc curriculum. Each method includes:
- Clean, well-commented code
- Sample input/output
- Step-by-step logic

---

## 📁 Folder Structure

```
numerical-techniques/
│
├── 01_Root_Finding/
│   ├── bisection_method.py
│   ├── regular_falsi.py
│   ├── newton_raphson.py
│   ├── secant_method.py
│   └── fixed_point_method.py
│
├── 02_Interpolation/
│   ├── newton_forward.py
│   ├── newton_backward.py
│   ├── gauss_forward.py
│   ├── gauss_backward.py
│   └── sterlings_interpolation.py
│
├── 03_Numerical_Differentiation/
│   ├── forward_difference.py
│   ├── backward_difference.py
│   └── central_difference.py
|
|
├── 04_Numerical_Integration/
│   ├── trapezoidal_rule.py
|   ├── simpsons 1 3.py
│   └── simpsons 3 8.py
|
|
├── 06_ODE_Solvers/
│   ├── README.md
│   ├── eulers_method.py
│   ├── modified_euler.py
│   ├──runge_kutta_4.py
|   └──heat_equation.py
|
├── 07_Curve_Fitting/
│   ├── exponential_power_curve.py
│   ├── fitted_exponential_curve.py
|   └── fitting_straight_line.py 

```

---

## 🧮 Methods Covered

### 1️⃣ Root Finding
| Method | File | Description |
|--------|------|-------------|
| Bisection Method | `bisection_method.py` | Bracket-based root finding |
| Regular Falsi | `regular_falsi.py` | False position method |
| Newton-Raphson | `newton_raphson.py` | Derivative-based iteration |
| Secant Method | `secant_method.py` | Two-point iteration |

### 2️⃣ Interpolation
| Method | File | Description |
|--------|------|-------------|
| Newton Forward | `newton_forward.py` | Forward difference interpolation |
| Newton Backward | `newton_backward.py` | Backward difference interpolation |
| Gauss Forward | `gauss_forward.py` | Gauss forward formula |
| Gauss Backward | `gauss_backward.py` | Gauss backward formula |

### 3️⃣ Numerical Differentiation
| Method | File | Description |
|--------|------|-------------|
| Forward Difference | `forward_difference.py` | First & second order |
| Backward Difference | `backward_difference.py` | First & second order |
| Central Difference | `central_difference.py` | Higher accuracy |


### 4️⃣ Numerical Integration
| Method | File | Description |
|--------|------|-------------|
| Trapezoidal Rule | `trapezoidal_rule.py` | Area under curve |
| Simpson's 1/3 | `simpsons_1_3.py` | Parabolic approximation |
| Simpson's 3/8 | `simpsons_3_8.py` | Cubic approximation |

### 6️⃣ ODE Solvers
| Method | File | Description |
|--------|------|-------------|
| Euler's Method | `eulers_method.py` | First order ODE |
| Modified Euler | `modified_euler.py` | Improved accuracy |
| Runge-Kutta 4 | `runge_kutta_4.py` | 4th order accuracy |

---

## ⚙️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/kiranmv002/numerical-techniques.git
cd numerical-techniques
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Any Method
```bash
python 01_Root_Finding/bisection_method.py
```

---

## 📦 Requirements

```
numpy
sympy
matplotlib
```

Install with:
```bash
pip install numpy sympy matplotlib
```

---

## 🗓️ Progress Tracker

- [x] Root Finding Methods
- [x] Interpolation Methods
- [x] Numerical Differentiation
- [x] Numerical Integration
- [x] Linear Systems
- [ ] ODE Solvers

---

## 🤝 Contributing
 
Pull requests are welcome! If you find a bug or want to add a new method:
1. Fork the repo
2. Create a branch: `git checkout -b feature/new-method`
3. Commit: `git commit -m "Add new method"`
4. Push & open a PR
