# DLSFH → DESI Lyα 1D: Geometric Transport Constraint

This repository is a minimal, reproducible testbed for confronting the **DLSFH
phenomenological geometric-transport operator** with **DESI Lyα one-dimensional
flux power spectrum** measurements.

## Scientific interface

We implement the canonical minimal ansatz used in the associated manuscript:

The DLSFH suppression acts on the density field as

$$
\delta_{\rm DLSFH}(\mathbf{k},z) = T_{\rm DLSFH}(k,z) \, \delta_{\rm GR}(\mathbf{k},z),
\qquad
T_{\rm DLSFH}(k,z) = \exp\left[-\Xi(z) k^2\right],
\qquad
\Xi(z) = \Xi_0 \, a^{2}.
$$

At the level of the matter power spectrum, this corresponds to the multiplicative suppression factor

$$
P_m(k,z) \;\to\; \exp\left[-2\,\Xi(z) k^2\right] \, P_m(k,z).
$$

## Repository layout

- `data/DESI_Lya_P1D/`
  - `datapoints_p1d_fft_desi_edrm2_v1.zip` : upstream DESI Lyα 1D product bundle (as provided)
  - mask lists used in the extraction workflow (as provided)
  - optional extracted CSV examples (e.g. `z2p2.csv`)
- `model/`
  - `dlsfh_transport.py` : theory-only transport operator (no survey assumptions)
  - `desi_forward_model.py` : forward-model scaffold (optional extension point)
- `analysis/`
  - `DESI_allz_profile_chi2_logspace.csv` : profiled χ² scan output used for Fig. 1 (if present)
  - `make_chi2_plot.py` : generate Δχ²(Ξ0) figure from the scan CSV
- `figures/`
  - `chi2_vs_Xi0.pdf` : profiled Δχ²(Ξ0) curve (main diagnostic)

## Quickstart (reproduce Fig. 1)

Create an environment (conda recommended):

```bash
conda env create -f environment.yml
conda activate dlsfh-desi-lya1d
```

Generate the figure (requires the scan CSV to exist at the path below):

```bash
python analysis/make_chi2_plot.py \
  --scan analysis/DESI_allz_profile_chi2_logspace.csv \
  --out figures/chi2_vs_Xi0.pdf
```

## Provenance / references

DESI Lyα 1D reference:
- T. Karaçaylı et al., *The one-dimensional Lyα forest power spectrum from DESI Early Data*, arXiv:2306.06316.

DESI survey reference:
- DESI Collaboration, *The DESI Experiment Part I: Science, Targeting, and Survey Design*, arXiv:1611.00036.

## Zenodo archive / DOI

A versioned snapshot of this repository is intended to be archived on Zenodo
for a permanent DOI-backed scientific record.

- Concept DOI: `10.5281/zenodo.18505662`
- Version DOI (this release): `10.5281/zenodo.18505662`

## License and data terms

This repository code is released under the license indicated in the repository.
If you redistribute this repository publicly, verify DESI data product terms for
redistribution and citation.
