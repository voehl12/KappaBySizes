# Sample Data for KappaBySizes Tutorials

This directory contains sample datasets and utilities for generating synthetic data used in the tutorials.

## Files:

- `README.md` - This file
- `generate_sample_data.py` - Script to create sample datasets for tutorials
- `catalogue.npy` - Pre-generated galaxy catalogue (25MB, excluded from git)
- `cl_kappa.txt` - Angular power spectrum data for kappa map generation
- (Generated files will appear here when tutorials are run)

## Usage:

The tutorials will automatically generate sample data as needed. You can also run the generation scripts directly to create larger datasets for experimentation.

## Data Files Description:

### catalogue.npy
A numpy array containing galaxy catalogue data used in the intro notebook. This file contains:
- Galaxy positions (RA, Dec)
- Galaxy properties (magnitudes, sizes, etc.)
- Data structure compatible with HEALPix operations

### cl_kappa.txt
Angular power spectrum coefficients for generating kappa (convergence) maps. Contains:
- Power spectrum values for different multipole moments ℓ
- Data for realistic gravitational lensing map generation
- Compatible with HEALPix synfast function