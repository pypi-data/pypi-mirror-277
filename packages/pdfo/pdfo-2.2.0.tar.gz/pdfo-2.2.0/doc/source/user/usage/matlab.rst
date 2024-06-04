.. _usage-matlab:

Usage for MATLAB
================

General information
-------------------

PDFO provides a MATLAB function ``pdfo``, which can solve general constrained or unconstrained optimization problems without using derivatives.

The ``pdfo`` function can automatically identify the type of your problem and then call one of Powell's solvers, namely COBYLA, UOBYQA, NEWUOA, BOBYQA, and LINCOA.
The user can also specify the solver by setting the ``solver`` field of the options passed to ``pdfo``.

The ``pdfo`` function is designed to be compatible with the ``fmincon`` function available in the `Optimization Toolbox <https://www.mathworks.com/products/optimization.html>`_ of MATLAB.
You can call ``pdfo`` in the same way as calling ``fmincon``.
In addition, ``pdfo`` can be called in some flexible ways that are not supported by ``fmincon``, which will be illustrated in the example below.

For detailed syntax of ``pdfo``, use the standard ``help`` command of MATLAB.
For example, run

.. code-block:: matlab

    help pdfo

An example
----------

The following code illustrates how to minimize the chained Rosenbrock function :eq:`chrosen` subject to various constraints.

.. code-block:: matlab

    function rosenbrock_example()

    fprintf('\nMinimize the chained Rosenbrock function with three variables subject to various constraints:\n');
    x0 = [0; 0; 0];  % starting point

    fprintf('\n1. Nonlinear constraints --- ||x||_2^2 = 1, x(i)^2 >= x(i+1) >= 0.5*x(i) >= 0 for i = 1, 2:\n');
    % linear inequality constraints A*x <= b
    A = [0.5, -1, 0; 0, 0.5, -1];
    b = [0; 0];
    % linear equality constraints Aeq*x = beq
    Aeq = [];
    beq = [];
    % bound constraints lb <= x <= ub
    lb = [0; 0; 0];
    ub = [];  % ub = [inf; inf; inf] works equally well
    % nonlinear constraints
    nonlcon = @nlc;  % see function nlc given below
    % The following syntax is identical to fmincon:
    [x, fx, exitflag, output] = pdfo(@chrosen, x0, A, b, Aeq, beq, lb, ub, nonlcon)
    % Alternatively, the problem can be passed to pdfo as a structure:
    %p.objective = @chrosen; p.x0 = x0; p.Aineq = A; p.bineq = b; p.lb = lb; p.nonlcon = @nlc;
    %[x, fx, exitflag, output] = pdfo(p)

    fprintf('\n2. Linear constraints --- sum(x) = 1, x(i+1) <= x(i) <= 1 for i = 1, 2:\n');
    A = [-1, 1, 0; 0, -1, 1];
    b = [0; 0];
    Aeq = [1, 1, 1];
    beq = 1;
    ub = [1; 1; 1];
    [x, fx, exitflag, output] = pdfo(@chrosen, x0, A, b, Aeq, beq, [], ub)

    fprintf('\n3. Bound constraints --- -0.5 <= x(1) <= 0.5, 0 <= x(2) <= 0.25:\n');
    lb = [-0.5; 0; -inf];
    ub = [0.5; 0.25; inf];
    [x, fx, exitflag, output] = pdfo(@chrosen, x0, [], [], [], [], lb, ub)

    fprintf('\n4. No constraints:\n');
    [x, fx, exitflag, output] = pdfo(@chrosen, x0)
    return

    function f = chrosen(x)  % objective function
    f = sum((x(1:end-1)-1).^2 + 4*(x(2:end)-x(1:end-1).^2).^2);
    return

    function [cineq, ceq] = nlc(x)  % nonlinear constraints
    % The same as fmincon, nonlinear constraints cineq(x) <= 0 and ceq(x) = 0 are specified
    % by a function with two return values, the first being cineq and the second being ceq.
    cineq = x(2:end) - x(1:end-1).^2;
    ceq = x'*x - 1;
    return

Options
-------

When calling ``pdfo``, we may specify some options by passing a structure to ``pdfo`` as the last input.
Here are several useful options.

#. ``solver``: a string indicating which solver to use; default: ``'uobyqa'`` for unconstrained problems with at most 8 variables, ``'newuoa'`` for unconstrained problems with 9 or more variables, ``'bobyqa'`` for bound-constrained problems, ``'lincoa'`` for linearly constrained problems, and ``'cobyla'`` for nonlinearly constrained problems.
   If you want to choose a solver, note that UOBYQA and NEWUOA can solve unconstrained problems, NEWUOA being preferable except for rather small problems; BOBYQA can solve unconstrained and bound-constrained problems; LINCOA can solve unconstrained, bound-constrained, and linearly constrained problems; COBYLA can solve general nonlinear optimization problems.
   We observe that LINCOA sometimes outperforms NEWUOA on unconstrained problems.
   It is also worth noting that BOBYQA evaluates the objective function only at feasible points, while LINCOA and COBYLA may explore infeasible points.
#. ``maxfun``: maximal number of function evaluations; default: ``500*length(x0)``.
#. ``ftarget``: target function value; pdfo terminates once it finds a feasible point with a function value at most ``ftarget``; default: ``-inf``.
#. ``scale``: a boolean value indicating whether to scale the problem according to bound constraints; if it is ``true`` and if all the variables have both lower and upper bounds, then the problem will be scaled so that the bound constraints become :math:`-1 \le x \le 1`; default: ``false``.
#. ``radius_init``: initial trust-region radius; typically, ``radius_init`` should be in the order of one tenth of the greatest expected change to a variable; ``radius_init`` should be positive; default: ``1`` if the problem will not be scaled, and ``0.5`` if the problem will be scaled; in case of scaling, ``radius_init`` will be used as the initial trust-region radius of the scaled problem.
#. ``radius_final``: final trust-region radius; ``radius_final`` reflects the precision of the approximate solution obtained by ``pdfo``; ``radius_final`` should be positive and not larger than ``radius_init``; default: ``1e-6``; in case of scaling, ``radius_final`` will be used as the final trust-region radius of the scaled problem.

For instance, to minimize the aforementioned chained Rosenbrock function without constraints by LINCOA with at most :math:`50` function evaluations and a target function value :math:`10^{-2}`, it suffices to replace ``pdfo(@chrosen, x0)`` in the above example with

.. code-block:: matlab

    pdfo(@chrosen, x0, struct('solver', 'lincoa', 'maxfun', 50, 'ftarget', 1e-2))
