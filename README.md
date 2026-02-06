# DLSFH → DESI Lyα 1D: Geometric Transport Constraint

This repository contains a minimal, reproducible pipeline to compare the
DLSFH phenomenological transport operator

$\[
P_m(k,z) \;\rightarrow\; \exp[-2\,\Xi(z)k^2] \, P_m^{\Lambda\mathrm{CDM}}(k,z),
\qquad \Xi(z)=\Xi_0 a^2
\]$

to **DESI Lyα 1D flux power spectrum** measurements.

## What is in this repo

- `data/DESI_Lya_P1D/`
  - `datapoints_p1d_fft_desi_edrm2_v1.zip` (as provided by DESI product distribution)
  - Optional extracted CSV examples (e.g. `z2p2.csv`)
  - Mask lists used in the upstream workflow (as provided)
- `analysis/DESI_allz_profile_chi2_logspace.csv`
  - Profiled likelihood scan output (Δχ² vs Xi0), used to generate the main figure.
- `figures/chi2_vs_Xi0.pdf`
  - The key diagnostic: profiled Δχ²(Ξ0) curve.

## Reproduce Figure 1 (Δχ² vs Ξ0)

```bash
python analysis/make_chi2_plot.py --scan analysis/DESI_allz_profile_chi2_logspace.csv --out figures/chi2_vs_Xi0.pdf
```

## Provenance / citation

DESI Lyα 1D data reference:
- T. Karaçaylı et al., *The one-dimensional Lyα forest power spectrum from DESI Early Data*, arXiv:2306.06316.

DESI survey reference:
- DESI Collaboration, *The DESI Experiment Part I: Science, Targeting, and Survey Design*, arXiv:1611.00036.

## License

This repository is provided for scientific reproducibility. Check DESI data product
licenses/terms for redistribution constraints in your intended use.
