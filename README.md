## Sistema de Reconhecimento Facial com conexão com plataforma de nuvem para IoT

Sistema desenvolvido como Trabalho de Conclusão de Curso para obtenção do grau de Bacharela em Ciência da Computação pela URI. 
A finalidade deste projeto foi desenvolver um sistema de monitoramento de ambientes no contexto de Internet das Coisas. Foi utilizada uma plataforma de nuvem IoT, que permite controlar o acesso do ambiente monitorado à partir de qualquer dispositivo com conexão à internet. 

![Demonstração com interface gráfica](https://i.imgur.com/58l9wvB.png "Demonstração com interface gráfica")

------------

### Instruções de execução

Reconhecedor facial desenvolvido na linguagem de programação Python, baseado no código oficial disponibilizado por [Adam Geitgey](https://github.com/ageitgey "Adam Geitgey"), criador da biblioteca Face Recognition, utilizada no sistema.

Este código foi baseado no código [facerec_from_webcam_faster](https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py "facerec_from_webcam_faster") de Adam Geitgey.  Para mais informações sobre funcionamento e instalação, acessar o código oficial. 

#### Requisitos:
- Raspberry Pi 3 model B (usada neste projeto) conectada à internet;
- Python instalado;
- Bibliotecas [OpenCV](https://github.com/opencv/opencv "OpenCV") e [Face Recognition](https://github.com/ageitgey/face_recognition/ "Face Recognition") instaladas;
- Dispositivo para captura de imagens (módulo de câmera para Raspberry Pi com conexão CSI baseado no módulo OV5647);
- Canal na plataforma [ThingSpeak](https://thingspeak.com "ThingSpeak").

------------

Como o reconhecedor facial funciona utilizando a foto do indivíduo conhecido, deverá ser armazenada a imagem do indivíduo escolhido na pasta em que o programa está localizado.

##### Fazer as devidas alterações nos nomes das pessoas conhecidas nas variáveis e no arquivo *.jpg* (linhas 9 a 16). 

A linha 25 define a URL da API da plataforma ThingSpeak para o canal que foi utilizado para a execução do projeto em que o sistema foi desenvolvido. Neste caso, deve-se proceder com a criação de um canal na plataforma ThingSpeak e substituição da chave de escrita no link do programa. 

Com os requisitos cumpridos, executar o programa reconhecedor_facial.py em linhas de comando ou com uma IDE específica.

------------

Neste projeto, para fins de desempenho, o sistema não possui interface gráfica (como a encontrada no código oficial). Ao realizar a detecção de um rosto, a identificação atribuída para o indivíduo reconhecido ou a identificação referente a "desconhecido" será escrita no retorno do programa e poderá ser conferida no canal criado na plataforma de nuvem.

A biblioteca OpenCV oferece visualização em vídeo dos reconhecimentos faciais e esta opção de visualização, além de toda a documentação sobre a biblioteca Face Recognition, pode ser encontrada na [página oficial](https://github.com/ageitgey/face_recognition/ "página oficial") da biblioteca.
