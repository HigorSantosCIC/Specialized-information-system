## Sistema Especialista para auxiliar no diagnostico entre dengue, zika e chikungunya

Alunos Participantes: 
- Higor Gabriel - 170012387
- Leonardo Rodrigues - 
  
  
Necessario a instalação da biblioteca Pyke:
http://pyke.sourceforge.net/

Para a instalação no Pyton3, versão utilizada para o desenvolvimento baixe o conteudo do repositorio: 
https://github.com/evertrol/pyke3

Clone o repositorio do 'pre_2to3_r1' do mercurial:

    $ hg clone \
      http://pyke.hg.sourceforge.net:8000/hgroot/pyke/pre_2to3_r1 \
      pyke3

Execute o script que roda 2to3 no codigo fonte baixado

    $ cd pyke3
    $ ./run_2to3 > /dev/null

Você pode tambem colocar o Pyke3 no seu PYTHONPATH e instalar.

Inserindo o pyke3 no seu PYTHONPATH:

    $ pwd > ~/.local/lib/python3.1/site-packages/pyke3.pth

Ou para instalar o Pyke:

    $ python3.1 setup.py install
      

Para executar o software:

python3 main.py


