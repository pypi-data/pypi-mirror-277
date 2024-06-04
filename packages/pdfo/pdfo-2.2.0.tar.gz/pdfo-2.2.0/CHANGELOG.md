# Changelog
All notable changes to the PDFO project will be documented in this file.

## v0.9 - 2020-04-19

Public beta release of PDFO.

## v1.0 - 2020-06-01

### Added
- Add the `honour_x0` option when the solver is BOBYQA to indicate whether the user-provided `x0` can be changed.
- Include `rosenbrock_example` to illustrate the usage.
- Python version: `Bounds`, `LinearConstraint` and `NonlinearConstraint` more flexible with `None` and `[]`.
- Python version: the `constr_value` output when there are constraints other than bounds.
- MATLAB version: add `uninstall` and `clean` options to `setup.m`.

### Changed
- Licence modified from GNU GPLv3+ to GNU LGPLv3+.
- The Fortran source code is refactored to remove the obsolete non-block `DO` loops and comparison operators.
- All constraint violations are computed absolutely (instead of relatively)
- Modify the scaling behavior. Scaling is performed only if all variables have both upper and lower bounds.
- Change the default `rhobeg` to `0.5` when the problem is scaled.
- Change the default `rhobeg` to `min(ub-lb)/4` when the solver is BOBYQA.
- Previously, if `rhobeg` is revised to be different from the default value, then `rhoend` is set to `min(rhobeg\*rhoend_default/rhobeg_default, rhoend)`, where `rhobeg_default = 1` and `rhoend_default = 1e-6`; now it is set to `min(0.1\*rhobeg, rhoend)`.
- Revise `x0` or `rhobeg` for BOBYQA to make sure that the distance between `x0` and inactive bounds is at least `rhobeg`.
- Python version: make PDFO available on PyPI.
- Python version: test files for PDFO have been added as a subpackage of `pdfo`.
- MATLAB version: improve the interfaces of `prepdfo` and `postpdfo`.

### Removed
- Warning about scaling.
- The `fhist` output when PDFO receives a feasibility problem.
- Python version: `numpy.set_printoptions` statement in `__init__.py`.
- MATLAB version: interactions when modifying the user's startup script.

### Fixed
- In last version, the linear constraints passed to the Fortran backend can have zero gradients due to reduction when some variables are fixed by the bound constraints. Constraint validation and reduction are merged in order to avoid such a situation.
- In last version, the user-specified `npt`, `rhobeg`, and `rhoend` are ignored if the solver selection function is invoked. They are taken into account now.
- Python version: previously, the nonlinear constraints defined as a dictionary cannot include NumPy functions of type `<ufunc>`. It is fixed now.

## v1.1 - 2021-08-13

### Added
- Python version: the linear equality constraints are now eliminated explicitly using a QR factorization with column pivoting (or an SVD factorization if SciPy is not installed).
- Python version: wheel distributions of the package are now available on PyPI to ease the installation. The wheel distributions are generated automatically using GitHub Actions.

### Changed
- If `rhobeg` is not provided but `rhoend` is available, the default value of `rhobeg` is set to `10\*rhoend`. Previously, it was `rhoend`.
- Python version: undefined constraint bounds for `Bounds`, `LinearConstraint`, and `NonlinearConstraint` can now be declared as `numpy.inf` with an appropriate sign.

### Removed
- Python version: Replaced deprecated `numpy.bool` calls by `numpy.bool_`.

### Fixed
- Python version: the call to the objective function during the debugging mechanism did not include the extra arguments, which are added now.

## v1.3 - 2023-04-25

### Changed
- The license is changed from GNU LGPLv3+ to the 3-clause BSD license.
- Python version: compilation of the Fortran backend is now performed using Meson instead of `numpy.distutils`.
- Python version: the `uobyqa`, `newuoa`, `bobyqa`, `lincoa`, and `cobyla` functions are deprecated. Only the `pdfo` function is now supported.

## v2.0 - 2023-11-xx

### Added
- Python version: Python 3.12 is now supported.

### Changed
- The `rhobeg` and `rhoend` options now become `radius_init` and `radius_final`, respectively.
- Python version: the package does not provide the `Bounds`, `LinearConstraint`, and `NonlinearConstraint` classes anymore. Only those provided by the `scipy.optimize` module are now supported.
- Python version: the `pdfo` function now returns an instance of `scipy.optimize.OptimizeResult`. The names of the returned fields are changed, and are now documented.
- Python version: `scipy>=1.10.0` is now required and Python 3.7 is not supported anymore.