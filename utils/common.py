"""
Common utility functions for the KappaBySizes tutorial series.

This module provides helper functions used across multiple tutorial notebooks
for generating synthetic data, performing statistical analyses, and creating
visualizations.
"""

import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
from astropy.cosmology import Planck18
from astropy import units as u


def simple_power_spectrum(k, A_s=2.1e-9, n_s=0.965, k_pivot=0.05):
    """
    Simple matter power spectrum model for educational purposes.
    
    Parameters:
    -----------
    k : array-like
        Wavenumber in h/Mpc
    A_s : float
        Scalar amplitude
    n_s : float  
        Spectral index
    k_pivot : float
        Pivot scale in h/Mpc
        
    Returns:
    --------
    P_k : array-like
        Matter power spectrum
    """
    # Scale-invariant part
    P_primordial = A_s * (k / k_pivot)**(n_s - 1)
    
    # Simplified transfer function
    q = k / (13.41 * 0.022)
    T_k = np.log(1 + 2.34 * q) / (2.34 * q) * \
          (1 + 3.89 * q + (16.1 * q)**2 + (5.46 * q)**3 + (6.71 * q)**4)**(-0.25)
    
    # Growth factor (simplified, z=0)
    D = 1.0
    
    return P_primordial * T_k**2 * D**2


def generate_simple_kappa_map(nside=256, z_source=1.0, seed=42):
    """
    Generate a simplified kappa map for educational purposes.
    
    Note: This is a simplified version. For research-quality maps,
    use more sophisticated methods from Tutorial 1.
    
    Parameters:
    -----------
    nside : int
        HEALPix nside parameter
    z_source : float
        Source redshift
    seed : int
        Random seed
        
    Returns:
    --------
    kappa_map : array
        HEALPix kappa map
    """
    np.random.seed(seed)
    
    npix = hp.nside2npix(nside)
    
    # Rough scaling with source redshift
    sigma_kappa = 0.01 * z_source
    kappa = np.random.normal(0, sigma_kappa, npix)
    
    # Smooth to create realistic correlations
    kappa_smoothed = hp.smoothing(kappa, fwhm=np.radians(0.5))
    
    return kappa_smoothed


def create_galaxy_sample(n_galaxies=1000, redshift_dist='exp', size_dist='lognormal', 
                        area_deg2=1.0, seed=42):
    """
    Create a simple synthetic galaxy sample for tutorials.
    
    Parameters:
    -----------
    n_galaxies : int
        Number of galaxies to generate
    redshift_dist : str
        Redshift distribution type ('exp', 'gamma', 'uniform')
    size_dist : str
        Size distribution type ('lognormal', 'normal', 'exponential')
    area_deg2 : float
        Survey area in square degrees
    seed : int
        Random seed
        
    Returns:
    --------
    catalogue : dict
        Dictionary containing galaxy properties
    """
    np.random.seed(seed)
    
    # Positions (uniform on sky)
    area_side = np.sqrt(area_deg2)
    ra = np.random.uniform(0, area_side, n_galaxies)
    dec = np.random.uniform(-area_side/2, area_side/2, n_galaxies)
    
    # Redshifts
    if redshift_dist == 'exp':
        z = np.random.exponential(0.5, n_galaxies)
    elif redshift_dist == 'gamma':
        z = np.random.gamma(2, 0.3, n_galaxies)
    elif redshift_dist == 'uniform':
        z = np.random.uniform(0.1, 3.0, n_galaxies)
    else:
        raise ValueError(f"Unknown redshift distribution: {redshift_dist}")
    
    z = np.clip(z, 0.1, 3.0)
    
    # Sizes
    if size_dist == 'lognormal':
        sizes = np.random.lognormal(np.log(1.0), 0.5, n_galaxies)
    elif size_dist == 'normal':
        sizes = np.abs(np.random.normal(1.0, 0.3, n_galaxies))
    elif size_dist == 'exponential':
        sizes = np.random.exponential(1.0, n_galaxies)
    else:
        raise ValueError(f"Unknown size distribution: {size_dist}")
    
    # Galaxy types
    galaxy_type = np.random.choice([0, 1], n_galaxies, p=[0.3, 0.7])
    
    # Magnitudes (simplified)
    distance_modulus = 5 * np.log10(Planck18.luminosity_distance(z).to(u.pc).value) - 5
    absolute_mag = np.random.normal(-20, 1.5, n_galaxies)
    apparent_mag = absolute_mag + distance_modulus
    
    catalogue = {
        'ra': ra,
        'dec': dec,
        'redshift': z,
        'size': sizes,
        'galaxy_type': galaxy_type,
        'apparent_mag': apparent_mag,
        'absolute_mag': absolute_mag
    }
    
    return catalogue


def plot_catalogue_summary(catalogue, title="Galaxy Catalogue Summary"):
    """
    Create a summary plot of galaxy catalogue properties.
    
    Parameters:
    -----------
    catalogue : dict
        Galaxy catalogue dictionary
    title : str
        Plot title
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Sky positions
    axes[0,0].scatter(catalogue['ra'], catalogue['dec'], s=1, alpha=0.6)
    axes[0,0].set_xlabel('RA (degrees)')
    axes[0,0].set_ylabel('Dec (degrees)')
    axes[0,0].set_title('Sky Positions')
    axes[0,0].set_aspect('equal')
    
    # Redshift distribution
    axes[0,1].hist(catalogue['redshift'], bins=30, alpha=0.7, edgecolor='black')
    axes[0,1].set_xlabel('Redshift')
    axes[0,1].set_ylabel('Count')
    axes[0,1].set_title('Redshift Distribution')
    
    # Size distribution
    axes[1,0].hist(catalogue['size'], bins=30, alpha=0.7, edgecolor='black')
    axes[1,0].set_xlabel('Size (arcsec)')
    axes[1,0].set_ylabel('Count')
    axes[1,0].set_title('Size Distribution')
    
    # Magnitude vs redshift
    axes[1,1].scatter(catalogue['redshift'], catalogue['apparent_mag'], 
                     s=1, alpha=0.6)
    axes[1,1].set_xlabel('Redshift')
    axes[1,1].set_ylabel('Apparent Magnitude')
    axes[1,1].set_title('Magnitude vs Redshift')
    
    plt.suptitle(title, fontsize=14)
    plt.tight_layout()
    plt.show()


def statistical_tests_summary(data1, data2, names=('Sample 1', 'Sample 2')):
    """
    Perform and summarize common statistical tests for comparing distributions.
    
    Parameters:
    -----------
    data1, data2 : array-like
        Data samples to compare
    names : tuple
        Names for the two samples
        
    Returns:
    --------
    results : dict
        Dictionary containing test results
    """
    from scipy import stats
    
    results = {}
    
    # Kolmogorov-Smirnov test
    ks_stat, ks_p = stats.ks_2samp(data1, data2)
    results['ks'] = {'statistic': ks_stat, 'pvalue': ks_p}
    
    # Anderson-Darling test
    try:
        ad_stat, ad_crit, ad_sig = stats.anderson_ksamp([data1, data2])
        results['anderson_darling'] = {'statistic': ad_stat, 'critical_values': ad_crit}
    except:
        results['anderson_darling'] = None
    
    # Mann-Whitney U test
    mw_stat, mw_p = stats.mannwhitneyu(data1, data2, alternative='two-sided')
    results['mann_whitney'] = {'statistic': mw_stat, 'pvalue': mw_p}
    
    # Basic statistics
    results['sample1'] = {
        'name': names[0],
        'count': len(data1),
        'mean': np.mean(data1),
        'std': np.std(data1),
        'median': np.median(data1)
    }
    
    results['sample2'] = {
        'name': names[1],
        'count': len(data2),
        'mean': np.mean(data2),
        'std': np.std(data2),
        'median': np.median(data2)
    }
    
    return results


def print_test_results(results):
    """
    Print formatted statistical test results.
    
    Parameters:
    -----------
    results : dict
        Results from statistical_tests_summary()
    """
    print("Statistical Comparison Results")
    print("=" * 40)
    
    print(f"\n{results['sample1']['name']}:")
    print(f"  Count: {results['sample1']['count']}")
    print(f"  Mean: {results['sample1']['mean']:.4f}")
    print(f"  Std:  {results['sample1']['std']:.4f}")
    print(f"  Median: {results['sample1']['median']:.4f}")
    
    print(f"\n{results['sample2']['name']}:")
    print(f"  Count: {results['sample2']['count']}")
    print(f"  Mean: {results['sample2']['mean']:.4f}")
    print(f"  Std:  {results['sample2']['std']:.4f}")
    print(f"  Median: {results['sample2']['median']:.4f}")
    
    print(f"\nKolmogorov-Smirnov Test:")
    print(f"  Statistic: {results['ks']['statistic']:.4f}")
    print(f"  P-value:   {results['ks']['pvalue']:.4f}")
    
    print(f"\nMann-Whitney U Test:")
    print(f"  Statistic: {results['mann_whitney']['statistic']:.0f}")
    print(f"  P-value:   {results['mann_whitney']['pvalue']:.4f}")
    
    if results['anderson_darling'] is not None:
        print(f"\nAnderson-Darling Test:")
        print(f"  Statistic: {results['anderson_darling']['statistic']:.4f}")