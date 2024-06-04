function information = package_info(request)
%PACKAGE_INFO returns information about the package.
%
%   ***********************************************************************
%   Authors:    Tom M. RAGONNEAU (tom.ragonneau@polyu.edu.hk)
%               and Zaikun ZHANG (zaikun.zhang@polyu.edu.hk)
%               Department of Applied Mathematics,
%               The Hong Kong Polytechnic University
%
%   Dedicated to the late Professor M. J. D. Powell FRS (1936--2015).
%   ***********************************************************************

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Attribute: private (not supposed to be called by users)
%
% TODO: None
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% package_info starts

% Who is calling this function? Is it a correct invoker?
invoker_list = {'pdfo'};
callstack = dbstack;
funname = callstack(1).name; % Name of the current function
if (length(callstack) == 1 || ~ismember(callstack(2).name, invoker_list))
    % Private/unexpected error
    error(sprintf('%s:InvalidInvoker', funname), ...
    '%s: UNEXPECTED ERROR: %s should only be called by %s.', funname, funname, mystrjoin(invoker_list, ', '));
else
    invoker = callstack(2).name; % Name of the function who calls this function
end

about = 'PDFO (Powell''s Derivative-Free Optimization solvers) is a cross-platform package providing interfaces for using the late Professor M. J. D. Powell''s derivative-free optimization solvers, including UOBYQA, NEWUOA, BOBYQA, LINCOA, and COBYLA.';

author = 'Tom M. Ragonneau and Zaikun Zhang';

email= 'tom.ragonneau@polyu.edu.hk and zaikun.zhang@polyu.edu.hk';

url = 'www.pdfo.net';

maintainer = 'Tom M. Ragonneau and Zaikun Zhang';

credits = {'Tom M. Ragonneau', 'Zaikun Zhang'};

license = '3-Clause BSD';

version = '2.2.0';

date = 'February, 2024';

status = 'Production';

message = 'Dedicated to the late Professor M. J. D. Powell FRS (29 July 1936--19 April 2015).';

copyright = sprintf('Copyright 2020--%d, Tom M. Ragonneau and Zaikun Zhang', year(datetime));

switch lower(request)
case 'about'
    information = about;
case 'author'
    information = author;
case 'email'
    information = email;
case 'url'
    information = url;
case 'maintainer'
    information = maintainer;
case 'credits'
    information = credits;
case 'copyright'
    information = copyright;
case 'license'
    information = license;
case 'version'
    information = version;
case 'date'
    information = date;
case 'status'
    information = status;
case 'message'
    information = message;
case {'info', 'information'}
    information = struct('about', about, 'author', author, 'email', email, 'url', url, 'maintainer', maintainer, 'credits', [], 'copyright', copyright, 'license', license, 'version', version, 'date', date, 'status', status, 'message', message);
    % information = struct(..., 'credits', credits, ...) will produce
    % a cell array of size 1x2, which is not desired. Thus we fist
    % define information with information.credits = [], and then assign
    % the following value:
    information.credits = credits;
otherwise % Public/expected error
    error(sprintf('%s:UnrecognizedString', invoker), '%s: unrecognized string received.', invoker);
end

% package_info ends
return
