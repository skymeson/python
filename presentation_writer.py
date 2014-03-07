#! /usr/bin/env python

import os

out_file = open("my_presentation.tex", 'wb' )

header = """\documentclass[10pt,   squeeze, compress, usenames, dvipsnames, pdflatex, xcolor=pdftex, table]{beamer}
\usepackage{graphicx}
\usepackage{epstopdf}
\\newcommand{\\rp}{\mbox{$\\not \hspace{-0.15cm} R_p$}}
\usepackage{color}
\usepackage{comment}
\usepackage{multicol}
\usetheme[]{Madrid}
\setbeamerfont{normal text}{size=scriptsize}
\def\myfigwidth{4cm}
\def\my3figwidth{4cm}

% Stop page numbering in backup slides                                                                                                                                                             
\\newcommand{\\beginbackup}{
  \\newcounter{framenumbervorappendix}
  \setcounter{framenumbervorappendix}{\\value{framenumber}}
}
\\newcommand{\\backupend}{
  \\addtocounter{framenumbervorappendix}{-\\value{framenumber}}
  \\addtocounter{framenumber}{\\value{framenumbervorappendix}}
}

\\title[UCR Group Meeting]{Measurement of Dielectrons in $p$ + $p$ collisions}
\subtitle[]{PHENIX Experiment}
\\author[Sky Rolnick]{ }
\institute[UC Riverside]{}
\date[\\today]{\\today}

\\begin{document}

%%%%%%%%%%%%%%%%                                                                                                                                                                                   

\\begin{frame}
\\titlepage
\end{frame}

\\begin{frame}
\\frametitle{Table of Contents}
\\begin{center}
\\begin{multicols}{2}
  \\tableofcontents[section]
\end{multicols}
\end{center}
\end{frame}

%%%%%%%%%%%%%%%%                                                                                                                                                                                   

\section{Explaination}
\\begin{frame}
  \\frametitle{Explanation}
  \\begin{center}
    \\begin{itemize}
    \item Plot dump from VBF W analysis framework
    \item Each and every distribution is shown here
    \item Progression of cutflows is shown
    \item 3 Slides per distribution
    \item Layout:
      \\begin{itemize}
      \item 1st Slide - inclusive Jet plots
      \item 2nd Slide - 2 Jet Bin
      \item 3rd Slide - 3 Jet Bin
      \end{itemize}
    \end{itemize}
    \\vspace{0.5cm}
    \\begin{tabular}{c c c}
      & \\bf{Slide Layout} & \\\\
      \\vspace{0.1cm}
      W + Jets Phase Space & $\\rightarrow$ & Jet $P_{T}$ cuts applied $\\rightarrow$\\\\
      \\vspace{0.2cm}
      $\\rightarrow$ Dijet Mass cut applied & $\\rightarrow$ & Vetoes Applied\\\\
      & & (Full VBF Phase Space) \\\\
    \end{tabular}
    \\begin{itemize}
    \item There is then a final slide showing the exclusive 2 and 3 jet bin control regions for each distribution
    \end{itemize}
  \end{center}
\end{frame}
"""

out_file.write( header )

Sections = [ "Lepton", "Jets", "Boson", "MET", "Other", "Angles" ]

SubSections = {}
PlotTitles = {}
LinLog = {}

SubSections[ "Lepton" ] = ["Lepton $\phi$", "Lepton $\eta$", "Lepton $P_{T}$" ]
PlotTitles[ "Lepton" ] = [ "LEPTON_PHI", "LEPTON_ETA", "LEPTON_PT" ]
LinLog[ "Lepton" ] = [ "lin", "log", "log" ]

SubSections[ "Jets" ] = [ "$N_{Jets}$", "All Jets $P_T$", "All Jets $\eta$", "Leading Jet $P_{T}$", "Leading Jet $\eta$", "Sub-Leading Jet $P_{T}$", "Sub-Leading Jet $\eta$ 3", "Dijet Mass" ]
PlotTitles[ "Jets" ] = [ "N_JETS", "JET_PT", "JET_ETA", "JET_PT_1", "JET_ETA_1", "JET_PT_2", "JET_ETA_2", "M_JJ" ]
LinLog[ "Jets" ] = [ "log", "log", "log", "log", "log", "log", "log", "log" ]

SubSections[ "Boson" ] = [ "$M_T$" ]
PlotTitles[ "Boson" ] = [ "MT" ]
LinLog[ "Boson" ] = [ "log" ] 

SubSections[ "MET" ] = ["MET"]
PlotTitles[ "MET" ] = [ "MET" ]
LinLog[ "MET"] = [ "log" ]

SubSections[ "Other" ] = [ "Average Interactions Per Xing", "$P_T$ Balance" ]
PlotTitles[ "Other" ] = [ "MU", "PTBALANCE" ]
LinLog[ "Other" ] = [ "lin", "log" ]
           
SubSections[ "Angles" ] = [ "$\Delta \phi (W,jj)$", "$\Delta R (lepton, J_1)$", "$\Delta R (lepton,J_3)$", "$\Delta \eta (J_1,J_2)$", "$\Delta R (J_1,J_3)$", "$\Delta R (J_2,J_3)$" ]
PlotTitles[ "Angles" ] = [ "DPWJJ", "DRLJ1", "DRLJ3", "DEJ1J2", "DRJ1J3", "DRJ2J3" ]
LinLog[ "Angles" ] = [ "lin", "lin", "lin", "lin", "lin", "lin" ]

for sec in Sections:

    out_file.write( "\section{" + sec + "} \n" )
    i = 0
    for subsec in SubSections[ sec ]:
        
        out_file.write( """\subsection{""" + subsec + """}

\\begin{frame}
  \\frametitle{""" + subsec + """ inclusive jets}
  \\begin{center}
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_inc_""" + LinLog[sec][i] + """}
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_jet_cut_""" + LinLog[sec][i] + """}
    \\\\
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_dijet_cut_""" + LinLog[sec][i] + """}
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_""" + LinLog[sec][i] + """}
  \end{center}
\end{frame}
\\begin{frame}
  \\frametitle{""" + subsec + """ 2 jet bin}
  \\begin{center}
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_inc_jet_2_""" + LinLog[sec][i] + """}
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_jet_cut_jet_2_""" + LinLog[sec][i] + """}
    \\\\
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_dijet_cut_jet_2_""" + LinLog[sec][i] + """}
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_jet_2_""" + LinLog[sec][i] + """}
  \end{center}
\end{frame}
\\begin{frame}
  \\frametitle{""" + subsec + """ 3 jet bin}
  \\begin{center}
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_inc_jet_3_""" + LinLog[sec][i] + """}
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_jet_cut_jet_3_""" + LinLog[sec][i] + """}
    \\\\
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_dijet_cut_jet_3_""" + LinLog[sec][i] + """}
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_jet_3_""" + LinLog[sec][i] + """}
  \end{center}
\end{frame}
\\begin{frame}
  \\frametitle{""" + subsec + """ Control Regions}
    \\begin{center} 
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_CJV_control_""" + LinLog[sec][i] + """}
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_CJV_control_jet_3_""" + LinLog[sec][i] + """}
    \\\\
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_ILV_control_jet_2_""" + LinLog[sec][i] + """}
    \includegraphics[width=0.48\linewidth]{""" + PlotTitles[sec][i] + """_ILV_control_jet_3_""" + LinLog[sec][i] + """}
  \end{center}
\end{frame} 
    
""" )

        
        i += 1
        pass
    pass

out_file.write( "\end{document}" )

out_file.close
