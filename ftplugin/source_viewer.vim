" --------------------------------
" Add our plugin to the path
" --------------------------------
python import os
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! SourceCode()
python << endOfPython

from source_viewer import source_signature

def open_source_file(file_path, line_number):
    
    vim.command(':BufOnly')
    vim.command(':split {0}'.format(file_path))
    vim.command(':set number!')
    vim.command(':{0}'.format(line_number)) 
    
file_name, line_number = source_signature(vim.current.line, os.environ['SOURCE_VAR'])
if len(file_name):
   open_source_file(file_name, line_number)


endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! Sc call SourceCode()
