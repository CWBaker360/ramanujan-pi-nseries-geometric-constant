# Reproducibility

## Requirements

- Python 3.10 or newer
- `mpmath`
- `pdflatex` to rebuild the paper

Install and run:

```bash
python -m pip install mpmath
python scripts/verify_pi_g_orders.py --precision 100 --output-dir output
```

The reported order at displayed scale \(N\) is

\[
p_N(A)=\log_2\left(\frac{|A_{N/2}-\pi|}{|A_N-\pi|}\right).
\]

This convention explains why the row labelled `N=32` compares the errors at
16 and 32.

Rebuild the paper:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -output-directory paper paper/ramanujan_pi_nseries_geometric_constant.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory paper paper/ramanujan_pi_nseries_geometric_constant.tex
```
