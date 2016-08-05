# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# Add color if it exists
if [ -f ~/.bash_color ]; then
        . ~/.bash_color
fi

# Add aliases if it exists
if [ -f ~/.bash_aliases ]; then
        . ~/.bash_aliases
fi


# User specific environment and startup programs
export USER_MODULES="emacs"
module load ${USER_MODULES}

# Store more commands in your command history
HISTFILESIZE=100000

# Short aliases for listing directories and clearing the screen
alias ls="ls -GFh"
alias cls="clear; ls"
alias clsh="clear; ls -hal"
alias c="clear"

# Counts the number of files in a directory
alias count="ls -1 | wc -l"

# Detailed list of all your jobs on the LPC
# Make sure to add your LPC username to this alias
alias bjobs="bjobs -u USERNAME -w"

# Aliases for bcount and bnames scripts
# This assumes that you've placed bcount and bnames
# in the ~/tools/ directory
alias bcount="python ~/tools/bcount.py"
alias bnames="python ~/tools/bnames.py"

# grep your command history
alias hgrep="history | grep"

# List the status of the lab's job queues
alias bqueues="bqueues | head -1; bqueues | grep moore"

# For compiling C++ programs
module load mpc/1.0.2 mpfr/3.1.2 gmp/6.0.0
