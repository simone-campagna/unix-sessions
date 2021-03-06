export ZAPPER_HOME_DIR="@ZAPPER_HOME_DIR@"
export ZAPPER_RC_DIR="$HOME/@ZAPPER_RC_DIR_NAME@"
ZAPPER_REQUIRED_COMPLETION_VERSION="@ZAPPER_COMPLETION_VERSION@"

function zapper {
    typeset _filename
    typeset _tmpdir=${TMPDIR:-/tmp}
    unset _filename
    while [[ -f ${_filename:="$_tmpdir/bash.$$.$RANDOM"} ]] ; do
        unset _filename
    done
    env ZAPPER_TARGET_TRANSLATOR="bash:${_filename}" PYTHONPATH="${PYTHONPATH}:${ZAPPER_HOME_DIR}/lib/python" ${ZAPPER_HOME_DIR}/bin/zapper "$@"
    if [[ -f ${_filename} ]] ; then
        #echo "---> $_filename"
        #cat "$_filename"
        . "$_filename"
    fi
}

export -f zapper

# set bash completion file:
bash_completion_file="${ZAPPER_RC_DIR}/completion.bash"
bash_completion_version_file="${bash_completion_file}.version"
if [[ ! -f ${bash_completion_version_file} ]] ; then
    rm -f "$bash_completion_file"
else
    . "$bash_completion_version_file"
    if [[ $ZAPPER_CURRENT_COMPLETION_VERSION != $ZAPPER_REQUIRED_COMPLETION_VERSION ]] ; then
        rm -f "$bash_completion_version_file"
        rm -f "$bash_completion_file"
    fi
fi
unset ZAPPER_CURRENT_COMPLETION_VERSION
if [[ ! -f ${bash_completion_file} ]] ; then
    export ZAPPER_ENABLE_BASH_COMPLETION_OPTION=True
    zapper completion "$bash_completion_file"
    unset ZAPPER_ENABLE_BASH_COMPLETION_OPTION
fi
if [[ -f ${bash_completion_file} ]] ; then
    . ${bash_completion_file}
fi
unset bash_completion_file

# zapper update
export ZAPPER_QUIET_MODE=True
zapper session sync --quiet
unset ZAPPER_QUIET_MODE
