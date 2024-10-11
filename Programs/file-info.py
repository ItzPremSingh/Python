import pathlib

fileEntenDict = {
        # Text Files
        ".txt"   : "Plain Text",
        ".docx"  : "Microsoft Word",
        ".doc"   : "Microsoft Word",
        ".rtf"   : "rich text format",
        ".pdf"   : "Portable Document Format",

        # Image Files
        ".png"   : "Portable Network Graphics",
        ".gif"   : "Graphics Interchange Format",
        ".bmp"   : "Bitmap",
        ".jpeg"  : "JPEG Image",
        ".jpg"   : "JPG Image",

        # Audio Files
        ".mp3"   : "MPEG-3 Audio",
        ".wav"   : "Waveform Audio",
        ".wma"   : "Windows Media Audio",
        ".aac"   : "Advanced Audio Coding",

        # Video Files
        ".mp4"   : "MPEG-4 video",
        ".avi"   : "Audio Video Interleave",
        ".mov"   : "QuickTime video",
        ".wmv"   : "Windows Media video",

        # Compressed Files
        ".zip"   : "Compressed archive",
        ".rar"   : "RAR archive",
        ".tar.gz": "Compressed archive with gzip",

        # Programming Files
        '.as'    : 'ActionScript',
        '.ada'   : 'Ada',
        '.adb'   : 'Ada',
        '.ads'   : 'Ada',
        '.asm'   : 'Assembly',
        '.s'     : 'Assembly',
        '.awk'   : 'AWK',
        '.c'     : 'C',
        '.cpp'   : 'C++',
        '.cc'    : 'C++',
        '.cxx'   : 'C++',
        '.h'     : 'C++',
        '.hpp'   : 'C++',
        '.cs'    : 'C#',
        '.clj'   : 'Clojure',
        '.cljs'  : 'Clojure',
        '.cljc'  : 'Clojure',
        '.cob'   : 'COBOL',
        '.cbl'   : 'COBOL',
        '.ccp'   : 'COBOL',
        '.cobol' : 'COBOL',
        '.coffee': 'CoffeeScript',
        '.cfm'   : 'ColdFusion',
        '.d'     : 'D',
        '.dart'  : 'Dart',
        '.ex'    : 'Elixir',
        '.exs'   : 'Elixir',
        '.erl'   : 'Erlang',
        '.hrl'   : 'Erlang',
        '.f'     : 'Fortran',
        '.for'   : 'Fortran',
        '.f90'   : 'Fortran',
        '.f95'   : 'Fortran',
        '.go'    : 'Go',
        '.groovy': 'Groovy',
        '.gradle': 'Groovy',
        '.hs'    : 'Haskell',
        '.lhs'   : 'Haskell',
        '.html'  : 'HTML',
        '.htm'   : 'HTML',
        '.java'  : 'Java',
        '.js'    : 'JavaScript',
        '.jl'    : 'Julia',
        '.kt'    : 'Kotlin',
        '.kts'   : 'Kotlin',
        '.lisp'  : 'Lisp',
        '.lsp'   : 'Lisp',
        '.cl'    : 'Lisp',
        '.lua'   : 'Lua',
        '.m'     : 'MATLAB',
        '.mm'    : 'Objective-C',
        '.pas'   : 'Pascal',
        '.pl'    : 'Perl',
        '.pm'    : 'Perl',
        '.php'   : 'PHP',
        '.php3'  : 'PHP',
        '.php4'  : 'PHP',
        '.php5'  : 'PHP',
        '.php7'  : 'PHP',
        '.ps1'   : 'PowerShell',
        '.psm1'  : 'PowerShell',
        '.psd1'  : 'PowerShell',
        '.py'    : 'Python',
        '.pyc'   : 'Python',
        '.pyd'   : 'Python',
        '.pyo'   : 'Python',
        '.pyw'   : 'Python',
        '.pyz'   : 'Python',
        '.r'     : 'R',
        '.R'     : 'R',
        '.rb'    : 'Ruby',
        '.rs'    : 'Rust',
        '.scala' : 'Scala',
        '.scm'   : 'Scheme',
        '.ss'    : 'Scheme',
        '.sh'    : 'Shell',
        '.bash'  : 'Shell',
        '.zsh'   : 'Shell',
        '.st'    : 'Smalltalk',
        '.sql'   : 'SQL',
        '.swift' : 'Swift',
        '.ts'    : 'TypeScript',
        '.vbs'   : 'VBScript',
        '.vb'    : 'Visual Basic',
        '.xml'   : 'XML',
        '.yaml'  : 'YAML',
        '.yml'   : 'YAML'
        }
    
def fileinfo(fullFileName):
    fileObject     = pathlib.Path(fullFileName)
    fileExten      = fileObject.suffix
    fileName       = fileObject.stem
    fileSize       = fileObject.stat().st_size

    return fileName, fileExten, fileSize

if __name__ == "__main__":
    import os
    _listOfScan = os.listdir()
    for name in _listOfScan:
        print(*fileinfo(name), sep=", ")
