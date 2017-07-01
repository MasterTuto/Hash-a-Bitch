# Hash a Bitch v. 2.0

### PT-BR
É uma ferramenta que procura hashes MD5 em uma lista de base de dados.

### EN-US
It's a tool that searchs for the md5 hash in many online databases.

## Novidades da versão (New in this version):

### PT-BR
Desta vez, há suporte há algumas outras bases de dados, e ainda mais, essa nova versão é uma modificação do Find My Hash, um projeto como o meu que foi descontinuado há alguns anos. Lembrando que quando eu fiz o Hash a Bitch eu nem ainda conhecia o Find my Hash.

### EN-US
This time, there are many online databases available, and further more! This new version is a modification of Find My Hash, a project that was descontinued many years ago. Rememebering that when I first created Hash a Bitch, I haven't even knew Find My Hash.

## Requerimentos (Requirements)

### PT-BR
Bibliotecas:
* BeautifulSoup;
* Requests
* base64

### EN-US
Libraries:
* BeautifulSoup;
* Requests
* base64

## Como usar (How to use)

### PT-BR

Para executar deve-se entrar com os seguintes dados:

```
python hashabitch.py <ALGORITMO> -H <HASH PARA SER CRACKEADA>
```
**OBS.:** *Algoritmo* deve ser, por enquanto, MD5, isso por que somente é suportado o algoritmo MD5.

*-H*: Indica que uma Hash foi entrada. O próximo argumento deve ser uma única HASH.

### EN-US

In order to run the program without problems, you must input the following parameters:

```
python hashabitch.py <ALGORITHM> -H <HASH TO BE CRACKED>
```
**OBS.:** *Algorithm* must be, for now, "MD5", that's why this tool only supports MD5 algorithm.

*-H*: It indicates that a hash is being input, so the next argument must be a unique HASH.
