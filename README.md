<h1>Sistema de Reconhecimento Facial com conexão com plataforma de nuvem para IoT </h1>

<p>Sistema desenvolvido como Trabalho de Conclusão de Curso para obtenção do grau de Bacharela em Ciência da Computação pela URI. 
A finalidade deste projeto foi desenvolver um sistema de monitoramento de ambientes no contexto de Internet das Coisas. Foi utilizada uma plataforma de nuvem IoT, que permite controlar o acesso do ambiente monitorado à partir de qualquer dispositivo com conexão à internet. </p>

<img width="auto" src="https://i.imgur.com/58l9wvB.png">

<p align="center">
 <a href="#instrucoes">Instruções de Execução</a> •  <a href="#requisitos">Requisitos</a> •  <a href="#alteracoes">Alterações necessárias</a> •  <a href="#informacoes">Informações gerais</a> 
</p>

------------
<h3 id=#instrucoes>Instruções de execução</h3>
<p>Reconhecedor facial desenvolvido na linguagem de programação Python, baseado no código oficial disponibilizado por <a href="https://github.com/ageitgey">Adam Geitgey</a>, criador da biblioteca Face Recognition, utilizada no sistema.</p>

<p>Este código foi baseado no código <a href="https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py">facerec_from_webcam_faster</a> de Adam Geitgey. Para mais informações sobre funcionamento e instalação, acessar o código oficial. </p>

------------

<h3 id=#requisitos>Requisitos</h3>
- Raspberry Pi 3 model B (usada neste projeto) conectada à internet;
- Python instalado;
- Bibliotecas <a href="https://github.com/opencv/opencv">OpenCV</a> e <a href="https://github.com/ageitgey/face_recognition/">Face Recognition</a> instaladas;
- Dispositivo para captura de imagens (módulo de câmera para Raspberry Pi com conexão CSI baseado no módulo OV5647);
- Canal na plataforma <a href="https://thingspeak.com">Thingspeak</a>.

------------
<h3 id=#alteracoes>Alterações necessárias</h3>
<p>Como o reconhecedor facial funciona utilizando a foto do indivíduo conhecido, deverá ser armazenada a imagem do indivíduo escolhido na pasta em que o programa está localizado.</p>

<h5>Fazer as devidas alterações nos nomes das pessoas conhecidas nas variáveis e no arquivo *.jpg* (linhas 9 a 16 do projeto). </h5>

```python
foto_pessoa = face_recognition.load_image_file("pessoa.jpg")
cod_rosto_pessoa = face_recognition.face_encodings(foto_pessoa)[0]

cod_rostos_conhecidos = [
    cod_rosto_pessoa
]
cod_rostos_nomes = [
    '2' #ID para usuario "Pessoa"
]
```

A linha 25 do programa define a URL da API da plataforma ThingSpeak para o canal que foi utilizado para a execução do projeto em que o sistema foi desenvolvido. Neste caso, deve-se proceder com a criação de um canal na plataforma ThingSpeak e substituição dos <b>X</b> pela chave de escrita no programa. 

```python
url = 'https://api.thingspeak.com/update?api_key=XXXXXXXXXXXXXXXX&field1=' 
```

Com os requisitos cumpridos, executar o programa reconhecedor_facial.py em linhas de comando ou com uma IDE específica.

------------
<h3 id=#informacoes>Informações gerais</h3> 
<p>Neste projeto, para fins de desempenho, o sistema não possui interface gráfica (como a encontrada no código oficial). Ao realizar a detecção de um rosto, a identificação atribuída para o indivíduo reconhecido ou a identificação referente a "desconhecido" será escrita no retorno do programa e poderá ser conferida no canal criado na plataforma de nuvem.</p>

<p>A biblioteca OpenCV oferece visualização em vídeo dos reconhecimentos faciais e esta opção de visualização, além de toda a documentação sobre a biblioteca Face Recognition, pode ser encontrada na <a href="https://github.com/ageitgey/face_recognition/">página oficial </a> da biblioteca.</p>

<h5>Este projeto foi finalizado em dezembro de 2018.</h5>
