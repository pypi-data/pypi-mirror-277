FRETBursts Release Notes
========================

.. module:: fretbursts

Version 0.8.3 (Jun. 2024)
------------------------

- Removed support for Python 3.6, as Python 3.7 now in end of life and 3.6 not supported
- Switch to using setuptools_scm for version managemnt instead of versioneer
- Updates for newer numpy compatibility (deprecation of np.float)
- Introduce :func:`burst_plot.scatter_burst_data` function for scatter plotting (currently now used in :func:`burst_plot.scatter_ra`, :func:`burst_plot.scatter_naa_nt`, and :func:`scatter_alex`) to normalize scatter ploting.
- use of :func:`burst_plot.scatter_burst_data` enables KDE density estimation with keyword argument `color_style='kde'` 

Version 0.7.1
-------------

- Require Python 3.6+. Python 2.7 is not supported anymore.
- Fix deprecation warning when plotting timetraces. Now matplotlib 3+ is required.
- Fix error loading Photon-HDF5 files with polarization data
  (`issue <https://github.com/OpenSMFS/FRETBursts/issues/18>`__)
- More fixes for PIE file with polarization, thanks to Christian Gebhardt 
  for reporting the problem and suggesting solutions 
  (`issue <https://github.com/OpenSMFS/FRETBursts/issues/25>`__)
- Passing list of strings to `loader.photon_hdf5()` loads each file into the same data object as an excitation spot.
- dplot function keyword argument `i=None` now plots concatenated data from all excitation spots. Does not apply to trace-based plots
- Fitter attributes relating to fit values now have parallel attributes ending in `_tot` which are for concatentated data across all spots.


Version 0.7 (Jul. 2018)
-----------------------

To update to the latest FRETBursts version type `conda install fretbursts -c conda-forge`.
For more detailed instructions see :doc:`Getting Started <getting_started>`.



Exporting:

- Export photon burst data to pandas DataFrame (function `bext.burst_photons <https://fretbursts.readthedocs.io/en/latest/plugins.html?highlight=burst_photons#fretbursts.burstlib_ext.burst_photons>`__)

Loading:

- Support for Photon-HDF5 0.5 and validation during loading
- Add function to load SM files acquired with 1-laser
  (`96d39b <https://github.com/OpenSMFS/FRETBursts/commit/96d39bb9c53c3a1f8dbf190410c2b1bad092f875>`__)
- Support smFRET-1color measurements from "generic" Photon-HDF5
  (`ab87e8 <https://github.com/OpenSMFS/FRETBursts/commit/ab87e8108e16ce6440fd57224e62b2ba96cc14a2>`__)
- Faster loading of nsALEX data when `ondisk=True`
  (`a6b343 <https://github.com/OpenSMFS/FRETBursts/commit/a6b343a0bc8e946cc1b4229a8c12f57bf95e598b>`__)
- Add support for loading polarization and split data as "spectral"
  (`a5b7d6 <https://github.com/OpenSMFS/FRETBursts/commit/a5b7d61f5d53ce65f3b9d9d9e8a50e891a968abf>`__,
  `c73188 <https://github.com/OpenSMFS/FRETBursts/commit/c731881ee25d287835ef9f3a3459740b2e62e6d5>`__)

Analysis:

- Background computation improvements: more robust, faster, better error messages
  (`4fbf33 <https://github.com/OpenSMFS/FRETBursts/commit/4fbf333e148df4663890277af1475f82400c83d5>`__,
  `7a3c17 <https://github.com/OpenSMFS/FRETBursts/commit/7a3c17d450c9010f4ef0faf4c774a3d4fca85367>`__,
  `5a68d0 <https://github.com/OpenSMFS/FRETBursts/commit/5a68d096fa6b61dd4dec7ffb4437d68a9f77869d>`__,)

Other:

- New documentation theme (docs live at the same address `fretbursts.readthedocs.io <https://fretbursts.readthedocs.io>`__)
- A myriad of small improvements and bug and regression fixes (see git log for details)


Version 0.6.5 (Aug. 2017)
-------------------------
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.848292.svg
   :target: https://doi.org/10.5281/zenodo.848292


This is a minor release with an important bug fix for histograms plots
and other tweaks mostly for PAX. New "short notebooks" for common tasks
have also been added.

Bug fixes:

- Fix histograms offset by half bin when using matplotlib 2.x.
  (see commit `d3102e <https://github.com/OpenSMFS/FRETBursts/commit/d3102e65e5c79c7a95c357d7d55ee273dc3ce87f>`__).
- Fix `BurstsGap` giving an error when being sliced
  (see `#62 <https://github.com/tritemio/FRETBursts/pull/64>`__).

Other changes:

- Kinetics: better handling of time_zero in moving_window functions
  (see `c25b68 <https://github.com/OpenSMFS/FRETBursts/commit/c25b682a191a72fe2a6835d49bafc47acd57bc36>`__).
- Multispot: Add argument `skip_ch` to `Data.collapse` and to `dplot`.
- Plots: use `vmin=1` by default in `alex_jointplot` and `hexbin_alex`.
- PAX: rewrote burst size and correction factors to be more clear and general
  (see :meth:`Data.burst_sizes_pax_ich <fretbursts.burstlib.Data.burst_sizes_pax_ich>`)
- Plots: spread burst labels to reduce overlapping when plotting burst
  info with :func:`timetrace <fretbursts.burst_plot.timetrace>`.
  See the new example notebook for timetrace plotting.
- New notebooks:
    - `Example - Plotting timetraces with bursts <https://github.com/OpenSMFS/FRETBursts/blob/master/notebooks/Example%20-%20Plotting%20timetraces%20with%20bursts.ipynb>`__
    - `Example - Selecting FRET populations <https://github.com/OpenSMFS/FRETBursts/blob/master/notebooks/Example%20-%20Selecting%20FRET%20populations.ipynb>`__
    - `Example - FRET histogram fitting <https://github.com/OpenSMFS/FRETBursts/blob/master/notebooks/Example%20-%20FRET%20histogram%20fitting.ipynb>`__


Version 0.6.4 (Jul. 2017)
--------------------------
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.825897.svg
   :target: https://doi.org/10.5281/zenodo.825897

This release adds support for *periodic acceptor excitation* (PAX)
measurements. PAX is similar to μs-ALEX, with the difference that only the
A laser is alternated (see references [pax]_ and [48spot]_).
There are also a few minor bug fixes and better support
for 48-spot data.

To update to the latest version type `conda install fretbursts -c conda-forge`.
For installation instructions see :doc:`Getting Started <getting_started>`.

The list of changes include:

- Added PAX support
- Workaround for a `numpy.histogram issue <https://github.com/numpy/numpy/issues/7503>`__ when input contains NaNs
- :func:`bext.burst_data() <fretbursts.burstlib_ext.burst_data>`: bugfix, add tests and improve handling of multispot data
- Added ``apionly`` argument to ``init_notebook()`` for setting up the notebook
  plots without changing any plot style (see `958824 <https://github.com/OpenSMFS/FRETBursts/commit/958824123152fd618d6811153bfbed64722fffd7>`__).
- Support "empty" channels in multispot data.
- Improve plots for 48-spot data.
- Refactoring of :func:`alex_jointplot <fretbursts.burst_plot.alex_jointplot>`.
    * Allow using custom ``Data`` fields for E and S in ``alex_jointplot``.
    * Remove rarely used arguments
    * Set axis limits by default
- Added `a new notebook <http://nbviewer.jupyter.org/github/tritemio/FRETBursts_notebooks/blob/master/notebooks/Example%20-%20Customize%20the%20us-ALEX%20histogram.ipynb>`__
  showing how to customize :func:`alex_jointplot <fretbursts.burst_plot.alex_jointplot>` plots.
- Improved normalization of exponential curve representing the
  fitted background in :func:`hist_bg <fretbursts.burst_plot.hist_bg>`
  (see `Issue 61 <https://github.com/tritemio/FRETBursts/issues/61>`__).
  Many thanks to Danielis Rutkauskas for reporting the issue.
- Removed shortcut (underscore) syntax for single-spot. Code like
  ``d.E_`` needs to be changed to ``d.E[0]``.
  This syntax was causing difficulties during developing new features for PAX.
  Please report if you would like for the syntax to be reintroduced.

.. [pax] Doose *et al.* European Biophysics Journal 36(6) p.669-674, **2007**.
         DOI:`10.1007/s00249-007-0133-7 <https://doi.org/10.1007/s00249-007-0133-7>`__
.. [48spot] Ingargiola *et al.* bioRxiv 156182, **2017**.
         DOI:`10.1101/156182 <https://doi.org/10.1101/156182>`__


Version 0.6.3 (Apr. 2017)
--------------------------

A few more small fixes in this release. If you have any installation
issue please report it on github.

- Import `OpenFileDialog` when FRETBursts is imported (as in versions < 0.6.2)
- Fix loading SM files with numpy 1.12
- Use `phconvert` to decode SM files


Version 0.6.2 (Apr. 2017)
--------------------------
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.495817.svg
   :target: https://doi.org/10.5281/zenodo.495817

This is a technical release that removes the hard dependency on QT
and solves some installation issues due to QT pinning on conda-forge.


Version 0.6.1 (Apr. 2017)
--------------------------
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.439688.svg
   :target: https://doi.org/10.5281/zenodo.439688

For this version of FRETBursts, conda packages are distributed for
python 2.7, 3.5, 3.6 and numpy 1.11 and 1.12. FRETBursts still works
with python 3.4 but conda packages are not provided anymore.
Python 2.7 is now deprecated. Support for python 2.7 will be removed
in a future version.

The current release includes the following changes:

- SangYoon Chung (@chungjjang80) found that the `L` argument in
  burst search was ignored and submitted a fix to the problem in
  `PR #57 <https://github.com/tritemio/FRETBursts/pull/57>`__.
  Tests were added to avoid future regressions.
- Fix access to the deprecated background attributes (introduced in 0.6).
  See `b850a5 <https://github.com/OpenSMFS/FRETBursts/commit/b850a595033c27cc66f8f4a748b1d0bf68366750>`__.
- Add plot wrapper for 16-ch data.
- Improved example notebook showing how to export burst data.
  See `Exporting Burst Data <https://github.com/OpenSMFS/FRETBursts/blob/49a45dd815b40602c5e754a162c66a837bbd2477/notebooks/Example%20-%20Exporting%20Burst%20Data%20Including%20Timestamps.ipynb>`__.
- Re-enable background rate caching.
  See `PR #53 <https://github.com/tritemio/FRETBursts/pull/53>`__.
- Support Path objects as filename in `loader.photon_hdf5()`.
  See `201b5c <https://github.com/OpenSMFS/FRETBursts/commit/201b5c089eca0f0867ceb453c3c111c54a21704d>`__.
- Improve `Ph_sel` string representation, added factory method `Ph_sel.from_str`
  and added new tests.
  See `3dc5f0 <https://github.com/OpenSMFS/FRETBursts/commit/3dc5f078c678ca3c806f49b27223a2e1cd6df64a>`__.


Version 0.6 (Jan. 2017)
-----------------------
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.239229.svg
   :target: https://doi.org/10.5281/zenodo.239229

.. module:: fretbursts.burstlib

- Improvements to the layout of 48-spot plots.
- Simplify background computation avoiding useless recomputations.
  This results in 3x speed increase in background computation
  for measurement loaded with `ondisk=True` and 30% speed increase
  when using `ondisk=False`.
  Now all background rates are stored in the dictionary :attr:`Data.bg`,
  while the mean background rate in the dictionary :attr:`Data.bg_mean`.
  The old attributes `Data.bg_*` and `Data.rate_*` have been deprecated
  and will be removed in a future release (see below).
- Fix loading files with `ondisk=True`. With this option timestamps are not
  kept in RAM but loaded spot-by-spot when needed. This option has no effect
  on single-spot measurements but will save RAM in multi-spot measurements.
- Add new plot functions
  `hist_interphoton <http://fretbursts.readthedocs.io/en/latest/plots.html#fretbursts.burst_plot.hist_interphoton>`__
  and `hist_interphoton_single <http://fretbursts.readthedocs.io/en/latest/plots.html#fretbursts.burst_plot.hist_interphoton_single>`__
  to plot the interphoton delay distribution. In previous versions the
  function `hist_bg` (and `hist_bg_single`) did the same plot but required
  the background to be fitted. `hist_interphoton*` do not require any prior
  background fit and also have a cleaner and improved API.
- Detect and handle smFRET files (no ALEX) with counts not only in D or A channels
  (`f0e33d <https://github.com/OpenSMFS/FRETBursts/commit/f0e33d855d6dfb31c89f282b249f80d845472124>`__).
- Better error message when a burst filtering function fails
  (`c7826d <https://github.com/OpenSMFS/FRETBursts/commit/c7826d5190a034578b1fdb9c4325f8fbfe2c01d4>`__).

Backward-incompatible changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Effect on burst search
""""""""""""""""""""""
Version 0.6 introduced a small change in how the auto-threshold
for background estimation is computed. This results in slightly different
background rates. As a consequence, burst searches setting a threshold
as function of the background, will set a slightly different threshold and
will find different number of bursts. The difference is not dramatic,
but can result in slight numeric changes in estimated parameters.

Details of auto-threshold changes
"""""""""""""""""""""""""""""""""
The refactor included a change in how the background is computed when using
`tail_min_us='auto'`. As before, with this setting, the background is
estimated iteratively in two steps. A first raw estimation with a fixed
threshold (250us), and second estimation with a threshold function of the
rate computed in the first step. Before version 0.6, the first step estimated
a single rate for the whole measurement. Now the first-step estimation is
performed in each background period separately. As before, the second step
computes the background separately in each background period.
This change was motivated by the need to simplify the internal logic
of background estimation, and to increase the computation efficiency
and accuracy.

Background attributes
"""""""""""""""""""""
The background refactor resulted in an incompatible change in the
:attr:`Data.bg` attribute. Users upgrading to version 0.6, may need to replace
`Data.bg` with `Data.bg[Ph_sel('all')]` in their notebooks. Note that
no official FRETBursts notebook was using `Data.bg`, so most users will not be
affected.

Compatibility layer
"""""""""""""""""""
All the old background-related attributes (bg_dd, bg_ad, bg_da, bg_aa,
rate_dd, rate_ad, rate_da, rate_aa, rate_m) are still present but deprecated.
The same data is now contained in the dictionaries
:attr:`Data.bg` and :attr:`Data.bg_mean`.
When using the deprecated attributes, a message will indicate the new syntax.
If you see the deprecation warning, please update the notebook
to avoid future errors.

Details of changed attributes
"""""""""""""""""""""""""""""

Before version 0.6, `Data.bg` contained background rates
fitted for **all-photons** stream. `Data.bg` was a list of arrays:
one array per spot, one array element per background period.
In version 0.6+, `Data.bg` contains the background rates for **all** the fitted
photon streams. `Data.bg` is now a dict using `Ph_sel` objects as keys.
Each dict entry is a list of array, one array per spot and one array element
per background period. For more details please refer to the following
documentation :attr:`Data.bg` and :attr:`Data.bg_mean`.


Version 0.5.9 (Sep. 2016)
-------------------------

- Added support for pyqt and qt 5+.
- Fix burst selection with multispot data.
  See `this commit <https://github.com/OpenSMFS/FRETBursts/commit/f05e807cbd032e748580af9cc310585bcde97e40>`__.

There may still be some glitches when using
the QT5 GUIs from the notebook, but installing (and importing) FRETBursts
does not require QT4 anymore (QT5 is the current default in anaconda).
Please report any issue.


Version 0.5.7 (Sep. 2016)
-------------------------

Refactoring and expansion of gamma and beta corrections.
Briefly, in all the places where corrected burst sizes are being computed,
we removed the `gamma1` argument and added a flag `donor_ref`.
Additionally, the values `Data.S` are now beta corrected.

These changes affected
several components as described below.

Data Class
^^^^^^^^^^

- Methods `Data.burst_sizes_ich` and `Data.burst_sizes` now accept the
  arguments ``gamma``, ``beta`` and ``donor_ref``. The argument ``gamma1``
  was removed.
  The two conventions of corrected burst sizes are chosen with the boolean
  flag ``donor_ref``.
  See the `burst_sizes_ich docs <http://fretbursts.readthedocs.io/en/latest/data_class.html?highlight=get_naa#fretbursts.burstlib.Data.burst_sizes_ich>`__
  for details.

- New method `get_naa_corrected` returns the array of `naa` burst counts
  corrected with the passed ``gamma`` and ``beta`` values. Like for the burst
  size, the argument ``donor_ref`` selects the convention for the correction.
  See the `get_naa_corrected docs <http://fretbursts.readthedocs.io/en/latest/data_class.html?highlight=get_naa#fretbursts.burstlib.Data.get_naa_corrected>`__
  for details.

- A new `Data` attribute ``beta`` (default: 1) stores a beta value that is used
  to compute the corrected S. This value is never implicitly used to compute
  corrected burst sizes or naa (for these a `beta` arguments needs to be
  passed explicitly).


Plot functions
^^^^^^^^^^^^^^

Plot functions `hist_size` and `hist_brightness` accept the new arguments
for corrected burst size (``gamma``, ``beta`` and ``donor_ref``).

Burst selection
^^^^^^^^^^^^^^^

Burst selection by `size` and `naa` accept the new arguments
for corrected burst size (``gamma``, ``beta`` and ``donor_ref``).

Burst Weights
^^^^^^^^^^^^^

Functions that accept weights don't accept the gamma1 argument anymore,
but they don't (yet) support the arguments `donor_ref` and `beta`.
As a result, for the purpose of weighting, there is only one expression
for corrected burst size (``na + gamma*nd``), with the option to add ``naa``
but without beta correction.


All these changes are covered by unit tests.

Installation via conda-forge
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since version 0.5.6 we started distributing conda packages for FRETBursts
through the `conda-forge <https://conda-forge.github.io/>`__ channel
(a community supported repository, as opposed to a private channel we were using before).
To install or update FRETBursts you should now use::

    conda install fretbursts -c conda-forge

Using the conda-forge channel simplifies our release process since
their infrastructure automatically builds packages for multiple
platforms and python versions. Please report any issues in installing
or upgrading FRETBursts on the
`GitHub Issues <https://github.com/OpenSMFS/FRETBursts/issues>`__ page.

For more detailed installation instructions see the
`Getting Started <http://fretbursts.readthedocs.io/en/latest/getting_started.html>`__
documentation.


Version 0.5.6
-------------

For older release notes see  `GitHub Releases Page <https://github.com/tritemio/FRETBursts/releases/>`__.
