# Ramanujan-Type pi Acceleration and the N-Series Geometric Constant pi_g

**Author:** C. Wayne Baker  
**Date:** June 1, 2026; source updated November 2, 2026  
**Status:** v1.1 source draft — PDF and checksums not yet rebuilt; not release-ready

This repository contains the paper:

> **Ramanujan-Type \(\pi\) Acceleration and the N-Series Geometric Constant \(\pi_g\)**

## Read the paper

- [`paper/ramanujan_pi_nseries_geometric_constant.pdf`](paper/ramanujan_pi_nseries_geometric_constant.pdf)
- [`paper/ramanujan_pi_nseries_geometric_constant.tex`](paper/ramanujan_pi_nseries_geometric_constant.tex)

## Scope

The paper compares two distinct routes to the classical circle constant:

- Ramanujan-type acceleration, based on modular and hypergeometric structure;
- polygonal N-Series acceleration, based on exact cancellation of an
  even-power geometric error hierarchy.

For the regular inscribed polygon quantity

\[
P_N=N\sin(\pi/N),
\]

the raw, two-scale, and three-scale approximations have orders

\[
2,\qquad 4,\qquad 6.
\]

The numerical table verifies this order ladder at high precision. The notation
\(P_N=N\sin(\pi/N)\) is an analytic description of the polygonal length; on
the doubling ladder the corresponding regular polygons and chord lengths are
constructible without taking \(\pi\) as input.

## Main claim boundary

The comparison is structural and complementary. The revised source explicitly derives the Ramanujan summand ratio 1/99^4 (about 7.98 decimal digits per term asymptotically) and distinguishes it from N-Series fixed-depth orders 2, 4 and 6. It does not claim that fixed
polygonal extrapolation is a modular transformation, that it matches the
arithmetic efficiency of Ramanujan's series, or that \(\pi_g\) is numerically
different from \(\pi\). The completed geometric limit satisfies

\[
\pi_g=\pi.
\]

## Reproduce the order table

```bash
python -m pip install mpmath
python scripts/verify_pi_g_orders.py --precision 100 --output-dir output
```

Expected result:

```text
verification_passed: True
```

## Rights

Copyright © 2026 C. Wayne Baker. All rights reserved unless otherwise stated.
