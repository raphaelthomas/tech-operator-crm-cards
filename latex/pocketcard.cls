\ProvidesClass{pocketcard}
\LoadClass[11pt]{article}
\RequirePackage[a5paper,
    margin=5mm,
    headheight=0pt,
    footskip=0pt,
    includeheadfoot
]{geometry}

\setlength{\parindent}{0pt}

\RequirePackage{fontspec}
\setmainfont{B612}

\RequirePackage{tabularx}
\RequirePackage{enumitem}
\RequirePackage{ragged2e}
\RequirePackage{xcolor}
\RequirePackage{hyperref}

\pagestyle{empty}

% Command to define a structured section on the card
\newcommand{\cardsection}[1]{
    \vspace{0.5\baselineskip} % Add a little space before the section
    \noindent\textbf{\uppercase{#1}} % Bold and uppercase title
    \hrule
    \vspace{0.2\baselineskip}
}

% Command for sub-sections
\newcommand{\subsectiontitle}[1]{
    \noindent\textbf{\textit{#1}}
    \vspace{0.1\baselineskip}
}

% Make itemized lists compact
\setlist[itemize]{
    noitemsep,          % Remove space between items
    topsep=0pt,         % Remove space before the list
    partopsep=0pt,
    parsep=0pt,
    leftmargin=4mm
}

\endinput
