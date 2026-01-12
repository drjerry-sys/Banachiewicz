# Solving Matrices Using the Banachiewicz Method (Surveying Applications)

## 📌 Project Overview
This project implements the **Banachiewicz inversion method** to compute the **inverse of a matrix (A⁻¹)** as well as the **inverse of its lower (L⁻¹) and upper (U⁻¹) triangular matrices** for matrices of **any dimension**.

The method is particularly useful in **surveying, geodesy, and adjustment computations**, where large systems of linear equations frequently arise (e.g., least squares adjustment, network analysis, error propagation).

---

## 🎯 Objectives
- Implement the Banachiewicz method for matrix inversion  
- Compute:
  - Inverse of the full matrix (**A⁻¹**)  
  - Inverse of the lower triangular matrix (**L⁻¹**)  
  - Inverse of the upper triangular matrix (**U⁻¹**)  
- Support **any square matrix dimension**  
- Provide a reliable numerical tool for surveying computations  

---

## 📐 Background (Surveying Context)
In surveying and geospatial analysis, matrix inversion is commonly required for:
- Least squares adjustment of observations  
- Covariance and variance–covariance matrix computation  
- Network adjustment and deformation analysis  
- Error propagation in geodetic measurements  

The **Banachiewicz method** offers an efficient approach by exploiting the **block structure** of matrices, reducing computational complexity compared to direct inversion methods.

---

## 🧮 The Banachiewicz Method
The Banachiewicz formula allows the inversion of a partitioned matrix:

\[
A =
\begin{bmatrix}
A_{11} & A_{12} \\
A_{21} & A_{22}
\end{bmatrix}
\]

Using this approach, the inverse is computed recursively, making it suitable for **large matrices** encountered in surveying problems.

---

## 🛠 Features
- ✅ Handles **any square matrix dimension**
- ✅ Computes **A⁻¹, L⁻¹, and U⁻¹**
- ✅ Numerically stable for surveying applications
- ✅ Modular and reusable implementation
- ✅ Suitable for academic, research, and professional use

---

## ⚙️ Workflow
1. Input a square matrix \( A \)  
2. Decompose the matrix into **Lower (L)** and **Upper (U)** triangular matrices  
3. Apply the Banachiewicz inversion formula  
4. Compute:
   - \( L^{-1} \)
   - \( U^{-1} \)
   - \( A^{-1} = U^{-1} L^{-1} \)

---

## 📊 Example Use Cases
- Least squares adjustment in geodetic networks  
- Survey control network analysis  
- Error and uncertainty propagation  
- Academic demonstrations of numerical methods in surveying  

---

## 🧰 Technologies Used
- Mathematical matrix operations  
- Numerical linear algebra techniques  
- (Language-dependent: Python / MATLAB / C++ / etc. — adapt as needed)

---

## 📈 Advantages of This Approach
- More efficient than brute-force inversion for large matrices  
- Well-suited for structured matrices common in surveying  
- Improves numerical reliability in adjustment computations  

---

## 📚 References
- Banachiewicz, T. (1937). *Zur Berechnung der Determinanten, wie auch der Inversen, und zur darauf basierten Auflösung der Systeme linearer Gleichungen.*  
- Wolf, P. R., & Ghilani, C. D. *Adjustment Computations*  
- Strang, G. *Linear Algebra and Its Applications*

---

## 👤 Author
**Adedeji Jeremiah**  
Surveying & Geoinformatics  

- GitHub: https://github.com/connectwithdevjerry  

---

## 📄 License
This project is intended for educational and research purposes. Licensing can be added as required.

