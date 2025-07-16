import os
import re
import subprocess
from typing import Union

# import pypandoc

# --trace
# --template=assets/toc.tex

class PandocFormatter:
    def __init__(self, base_path: str, exclude: Union[None, str] = None, toc_depth: int = 3):
        self.base_path = base_path
        self.exclude = exclude
        self.toc_depth = toc_depth

    def _generator_(self, template: str) -> Union[bool, Exception]:
        try:
            match_MDs = list()
            files_path = os.path.join(self.base_path, '_files.txt')
            with open(files_path, 'w', encoding='utf-8') as file:
                for filename in os.listdir(self.base_path):
                    excl_match = None
                    if self.exclude: excl_match = re.match(
                        pattern=self.exclude, string=filename, 
                        flags=re.IGNORECASE)
                    if not excl_match and filename.endswith('.md'):
                        match_MDs.append(filename)
                        file.write(filename + '\n')
                        # печатать команду для каждого MD файла
                        # print(f'{template_in}{filename} -o out/{filename.replace(".md", ".pdf")}')
            command = f'pandoc {template} -s {" ".join(match_MDs)}'
            print(command)
            result = subprocess.run(command, shell=True, cwd=self.base_path,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)
            print(f'\tstderr:\n{result.stderr}')
            print(f'\tstdout:\n{result.stdout}')
            if result.returncode == 0: return True
            else: raise Exception(f'Error: {result.stderr}')
        except Exception as e: return e


    def gen_pdf(self) -> Union[object, Exception]:
        # --pdf-engine=xelatex
        # --pdf-engine=lualatex
        # -V mainfont="Arial"
        template = '-f markdown ' + \
            '--pdf-engine=xelatex ' + \
            '--number-sections ' + \
            f'--toc --toc-depth={self.toc_depth} ' + \
            '--lua-filter=assets/page_break.lua ' + \
            '-V mainfont="Arial" ' + \
            '' + \
            '-o out/out.pdf'
        self._generator_(template)
        return os.path.join(self.base_path, 'out', 'out.pdf')

    def gen_docx(self) -> Union[object, Exception]:
        # --reference-doc=assets/reference.docx
        template = '-f markdown ' + \
            '--number-sections ' + \
            f'--toc --toc-depth={self.toc_depth} ' + \
            '--lua-filter=assets/page_break.lua ' + \
            '--reference-doc=assets/reference.docx ' + \
            '' + \
            '-o out/out.docx'
        self._generator_(template)
        return os.path.join(self.base_path, 'out', 'out.docx')

