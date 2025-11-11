# Rendering Equations in Mkdocs

It is easy to add complex equations to any chapter content.
Our intelligent textbooks all come configured with the MathJax
libraries installed so that you just put LeTeX directly in the
markdown files surrounded by dollar signs `$`.  You do not need
to put in backslashes before the `$` or `.`.

## Equation Rendering Rules

1. Always put name of the equation in markdown level 4 header.  This allows us to send a link to each equation in a chat or email.
2. Within the body text, render equation in LaTeX format on a line with blank lines before and after the LaTeX equation.
3. Surround the equation with single dollar signs in front and in back of the LaTeX strings.
4. For each variable in the equation, add a "where:" that defines each variable.
5. Put blank lines around the word "where:" and list of variables.
6. Follow the "where" with a markdown list of the variables.
7. Wrap the variables names in single dollar signs within the definitions.

Here are two examples of the format I want.

#### Slope and Intercept

$y = m * x + b$

where:

- $y$ is the vertical axis
- $x$ is the horizontal axis
- $m$ is the slope
- $b$ is the intercept

#### Point-Slope Form

The point-slope form of a line passing through point $(x_1, y_1)$ with slope $m$:

$$y - y_1 = m(x - x_1)$$

#### Standard Form of a Quadratic

The standard form of a quadratic equation:

$ax^2 + bx + c = 0$

where:

- $a is the coefficient of the square of x
- $b is the coefficient of x
- $c is a constant
- $a \neq 0$.

#### The Quadratic Formula

The quadratic formula for solving $ax^2 + bx + c = 0$:

$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

### Vertex Form of the Quadric Function

The vertex form of a quadratic function:

$y = a(x - h)^2 + k$

where:

- $(h, k)$ is the vertex of the parabola.

#### Area of a Circle

$A = 2\pi r^2$

where:

- $A$ is the area of the circle
- $r$ is the radius

#### Ohm's Law

$V = I R$

where:

- $V$ is the voltage across the resistor
- $I$ is the current through the resistor
- $R$ is the resistance

#### Kirchhoff's Voltage Law (KVL)

$\sum_{k=1}^{n} V_k = 0$

where:

- $V_k$ is the voltage across the $k$th element in the loop
- $n$ is the number of elements in the loop

#### Complex Power

$S = V_{\text{RMS}} I_{\text{RMS}}^\* = P + j Q$

where:

-   $S$ is the complex power
-   $V_{\text{RMS}}$ is the RMS voltage
-   $I_{\text{RMS}}^\*$ is the complex conjugate of the RMS current
-   $P$ is the real power
-   $Q$ is the reactive power
-   $j$ is the imaginary unit ($j = \sqrt{-1}$)