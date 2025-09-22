#!/usr/bin/env python3
"""
Generate sample datasets for KappaBySizes tutorials.

This script creates various sample datasets that can be used in the tutorials
for experimentation and learning.
"""

import numpy as np
import pandas as pd
import healpy as hp
from astropy.cosmology import Planck18
from astropy import units as u
import os
import sys

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from common import create_galaxy_sample, generate_simple_kappa_map


def generate_large_galaxy_catalogue(n_galaxies=50000, filename='large_galaxy_catalogue.csv'):
    """Generate a large galaxy catalogue for experiments."""
    print(f"Generating large galaxy catalogue with {n_galaxies} galaxies...")
    
    # Create large sample
    catalogue = create_galaxy_sample(
        n_galaxies=n_galaxies,
        redshift_dist='gamma',
        size_dist='lognormal',
        area_deg2=100,  # 10x10 degree area
        seed=42
    )
    
    # Convert to DataFrame
    df = pd.DataFrame(catalogue)
    
    # Add galaxy IDs
    df['galaxy_id'] = np.arange(len(df))
    
    # Reorder columns
    columns = ['galaxy_id', 'ra', 'dec', 'redshift', 'size', 'galaxy_type', 
               'apparent_mag', 'absolute_mag']
    df = df[columns]
    
    # Save to file
    output_path = os.path.join(os.path.dirname(__file__), filename)
    df.to_csv(output_path, index=False)
    print(f"Saved catalogue to {output_path}")
    
    return df


def generate_kappa_maps(nsides=[128, 256, 512], z_sources=[0.5, 1.0, 1.5, 2.0]):
    """Generate kappa maps at different resolutions and source redshifts."""
    print("Generating kappa maps...")
    
    for nside in nsides:
        for z_source in z_sources:
            print(f"  Creating map: nside={nside}, z_source={z_source}")
            
            kappa_map = generate_simple_kappa_map(
                nside=nside,
                z_source=z_source,
                seed=42
            )
            
            # Save as FITS file
            filename = f'kappa_map_nside{nside}_z{z_source:.1f}.fits'
            output_path = os.path.join(os.path.dirname(__file__), filename)
            hp.write_map(output_path, kappa_map, overwrite=True)
            print(f"    Saved to {output_path}")


def generate_redshift_catalogues():
    """Generate catalogues with different redshift measurement qualities."""
    print("Generating redshift catalogues...")
    
    # Base catalogue
    base_cat = create_galaxy_sample(n_galaxies=10000, area_deg2=25, seed=123)
    
    # Perfect spectroscopic redshifts
    spec_cat = base_cat.copy()
    spec_cat['z_spec'] = spec_cat['redshift']
    spec_cat['z_spec_error'] = np.full(len(spec_cat['redshift']), 0.001)  # Very small errors
    
    # Photometric redshifts with realistic errors
    photo_cat = base_cat.copy()
    z_true = photo_cat['redshift']
    
    # Realistic photo-z errors: σ_z = 0.05 * (1 + z)
    photo_z_error = 0.05 * (1 + z_true)
    z_photo = z_true + np.random.normal(0, photo_z_error)
    z_photo = np.maximum(z_photo, 0.01)  # No negative redshifts
    
    photo_cat['z_photo'] = z_photo
    photo_cat['z_photo_error'] = photo_z_error
    photo_cat['z_true'] = z_true
    
    # Save catalogues
    spec_df = pd.DataFrame(spec_cat)
    photo_df = pd.DataFrame(photo_cat)
    
    spec_df.to_csv(os.path.join(os.path.dirname(__file__), 'spectroscopic_catalogue.csv'), index=False)
    photo_df.to_csv(os.path.join(os.path.dirname(__file__), 'photometric_catalogue.csv'), index=False)
    
    print("  Saved spectroscopic_catalogue.csv")
    print("  Saved photometric_catalogue.csv")


def main():
    """Generate all sample datasets."""
    print("KappaBySizes Sample Data Generation")
    print("=" * 40)
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(__file__), exist_ok=True)
    
    try:
        # Generate different datasets
        generate_large_galaxy_catalogue()
        generate_kappa_maps()
        generate_redshift_catalogues()
        
        print("\nAll sample datasets generated successfully!")
        print("\nGenerated files:")
        data_dir = os.path.dirname(__file__)
        for file in os.listdir(data_dir):
            if file.endswith(('.csv', '.fits')):
                print(f"  {file}")
                
    except Exception as e:
        print(f"Error generating data: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())